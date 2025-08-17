import numpy as np
import itertools as itools
from encoding.DataSequence import DataSequence

DEFAULT_BAD_WORDS = frozenset(["sentence_start", "sentence_end", "br", "lg", "ls", "ns", "sp"])

def make_word_ds(grids, trfiles, bad_words=DEFAULT_BAD_WORDS):
    """Creates DataSequence objects containing the words from each grid, with any words appearing
    in the [bad_words] set removed.
    """
    ds = dict()
    stories = grids.keys()
    for st in stories:
        grtranscript = grids[st].tiers[-1].make_simple_transcript()
        ## Filter out bad words
        goodtranscript = [x for x in grtranscript
                          if x[2].lower().strip("{}").strip() not in bad_words]
        d = DataSequence.from_grid(goodtranscript, trfiles[st][0])
        ds[st] = d

    return ds

def make_semantic_model(ds, lsasm):
    newdata = []
    for w in ds.data:
        try:
            v = lsasm[w]
        except KeyError as e:
            v = np.zeros((lsasm.data.shape[0],))
        newdata.append(v)
    return DataSequence(np.array(newdata), ds.split_inds, ds.data_times, ds.tr_times)