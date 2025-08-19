import os
import numpy as np
import json
import config
from encoding.stimulus_utils import TRFile, load_textgrids, load_simulated_trfiles
from encoding.dsutils import make_word_ds, make_semantic_model
from encoding.interpdata import lanczosinterp2D
from encoding.utils import make_delayed

SKIP_WORDS = {}
SKIP_WORDS["story"] = frozenset(["sentence_start", "sentence_end", "br", "lg", "ls", "ns", "sp"])
SKIP_WORDS["movie"] = frozenset(["", "sp", "uh"])

def get_wordseqs(stimuli, modality):
    """loads words and word times of stimuli
    """
    if modality == "story": pad = 5
    else: pad = 0
    base = os.path.join(config.DATA_DIR, "derivative/TextGrids")
    grids = load_textgrids(stimuli,base)
    with open(os.path.join(config.DATA_DIR, "derivative/respdict.json"), "r") as f:
        respdict = json.load(f)
    trfiles = load_simulated_trfiles(respdict, pad = pad)
    wordseqs = make_word_ds(grids, trfiles, bad_words = SKIP_WORDS[modality])
    return wordseqs

def get_stim(stimuli, modality, features, tr_stats = None):
    """extract quantitative features of stimuli
    """
    word_seqs = get_wordseqs(stimuli, modality)
    word_vecs = {stim : features.make_stim(word_seqs[stim].data) for stim in stimuli}
    word_mat = np.vstack([word_vecs[stim] for stim in stimuli])
    word_mean, word_std = word_mat.mean(0), word_mat.std(0)
    ds_vecs = {stim : lanczosinterp2D(word_vecs[stim], word_seqs[stim].data_times, word_seqs[stim].tr_times) 
            for stim in stimuli}
    if modality == "story": ds_mat = np.vstack([ds_vecs[stim][5+config.STRIM:-config.STRIM] for stim in stimuli])
    if modality == "movie": ds_mat = np.vstack([ds_vecs[stim][config.MTRIM:-config.MTRIM] for stim in stimuli])
    if tr_stats is None: 
        r_mean, r_std = ds_mat.mean(0), ds_mat.std(0)
        r_std[r_std == 0] = 1
    else: 
        r_mean, r_std = tr_stats
    ds_mat = np.nan_to_num(np.dot((ds_mat - r_mean), np.linalg.inv(np.diag(r_std))))
    del_mat = make_delayed(ds_mat, config.STIM_DELAYS)
    if tr_stats is None: return del_mat, (r_mean, r_std), (word_mean, word_std)
    else: return del_mat

def get_stim_lexical(stimuli, modality, model, tr_stats = None):
    """extract quantitative features of stimuli using lexical embedding space
    """
    word_seqs = get_wordseqs(stimuli, modality)
    word_vecs = {stim : make_semantic_model(word_seqs[stim], model).data for stim in stimuli}
    word_mat = np.vstack([word_vecs[stim] for stim in stimuli])
    word_mean, word_std = word_mat.mean(0), word_mat.std(0)
    ds_vecs = {stim : lanczosinterp2D(word_vecs[stim], word_seqs[stim].data_times, word_seqs[stim].tr_times) 
            for stim in stimuli}
    if modality == "story": ds_mat = np.vstack([ds_vecs[stim][5+config.STRIM:-config.STRIM] for stim in stimuli])
    if modality == "movie": ds_mat = np.vstack([ds_vecs[stim][config.MTRIM:-config.MTRIM] for stim in stimuli])
    if tr_stats is None: 
        r_mean, r_std = ds_mat.mean(0), ds_mat.std(0)
        r_std[r_std == 0] = 1
    else: 
        r_mean, r_std = tr_stats
    ds_mat = np.nan_to_num(np.dot((ds_mat - r_mean), np.linalg.inv(np.diag(r_std))))
    del_mat = make_delayed(ds_mat, config.STIM_DELAYS)
    if tr_stats is None: return del_mat, (r_mean, r_std), (word_mean, word_std)
    else: return del_mat

def get_roi_features(resp, roi_voxels, rois, tr_stats = None):
    """extract average response from each region
    """
    features = []
    for roi in rois:
        features.append(resp[:, roi_voxels[roi]].mean(1))
    features = np.array(features).T
    if tr_stats is None: 
        r_mean, r_std = features.mean(0), features.std(0)
        r_std[r_std == 0] = 1
    else: 
        r_mean, r_std = tr_stats
    features = np.nan_to_num(np.dot((features - r_mean), np.linalg.inv(np.diag(r_std))))
    if tr_stats is None: return features, (r_mean, r_std)
    else: return features

def predict_word_rate(resp, roi_voxels, wr_decoders):
    """predict word rate at each acquisition time
    """
    mean_rate = []
    for wr_decoder in wr_decoders:
        resp_roi = get_roi_features(resp, roi_voxels, wr_decoder['rois'], tr_stats = wr_decoder['tr_stats'])
        delresp = make_delayed(resp_roi, config.RESP_DELAYS)
        mean_rate.append(((delresp.dot(wr_decoder['weights']) + wr_decoder['mean'])).reshape(-1))
    return np.round(np.mean(mean_rate, axis = 0).clip(min = 0)).astype(int)

def predict_word_times(word_rate, resp, starttime = 0, tr = 2):
    """predict evenly spaced word times from word rate
    """
    half = tr / 2
    trf = TRFile(None, tr)
    trf.soundstarttime = starttime
    trf.simulate(resp.shape[0])
    tr_times = trf.get_reltriggertimes() + half
    word_times = []
    for mid, num in zip(tr_times, word_rate):  
        if num < 1: continue
        word_times.extend(np.linspace(mid - half, mid + half, num, endpoint = False) + half / num)
    return np.array(word_times), tr_times