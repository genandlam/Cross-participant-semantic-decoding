import os
import numpy as np

def save_data(save_path, data):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    np.save(save_path, data)

def flatten_list(l):
    return [item for sublist in l for item in sublist]

def nsort(l):
    return np.sort(list(set(l)))

def mean_wt(wt):
    """average weights across FIR delays
    """
    return np.mean(np.split(wt, 4, axis = 0), axis = 0)

def tr2min(t):
    """get minutes for each story
    """
    return 2 * (t - 10) / 60

def list2str(l):
    """get id for list of stories
    """
    return '_'.join(sorted(l))

def get_subsets(pool, respdict, target_mins, samples = 10):
    """create subsets of stimuli 
    """
    np.random.seed(42)
    total_mins = np.sum([tr2min(respdict[stim]) for stim in pool])
    target_probs = (target_mins / total_mins).clip(0.01, 0.99)
    duplicates = set()
    subsets = {}
    for tm, tp in zip(target_mins, target_probs):
        for sample in range(samples):
            added = False
            while not added:
                index = np.array([np.random.random() < tp for _ in range(len(pool))])
                checkstr = list2str(pool[index])
                if np.sum(index) >= 1 and checkstr not in duplicates:
                    duplicates.add(checkstr)
                    added = True
            subsets[tm, sample] = sorted(pool[index])
    return subsets