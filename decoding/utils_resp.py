import os
import numpy as np
import h5py
import config

def get_resp(subject, stimuli, modality, stack = True, voxels = None):
    """loads response data
    """
    subject_dir = os.path.join(config.DATA_DIR, "derivative/preprocessed_data", subject)
    resp = {}
    for stim in stimuli:
        resp_path = os.path.join(subject_dir, "%s.hf5" % stim)
        hf = h5py.File(resp_path, "r")
        resp[stim] = np.nan_to_num(hf["data"][:])
        if voxels is not None:
            resp[stim] = resp[stim][:, voxels]
        hf.close()
    if stack: return np.vstack([resp[stim] for stim in stimuli]) 
    else: return resp
    
def get_resp_test(subject, voxels = None, repeat = "first"):
    """loads test response data
    """
    subject_dir = os.path.join(config.DATA_DIR,  "derivative/preprocessed_data", subject)
    #subject_dir = os.path.join(DATA_TEST_DIR, "test_response", subject)
    resp_path = os.path.join(subject_dir, "wheretheressmoke.hf5")
    hf = h5py.File(resp_path, "r")
    resp = np.nan_to_num(hf["individual_repeats"][:5])
    if voxels is not None:
        resp = resp[:, :, voxels]
    hf.close()
    if repeat == "first": 
        return resp[0]
    elif repeat == "mean":
        return np.mean(resp, axis = 0)
    else: 
        return resp