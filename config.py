import os
import numpy as np

# directories

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_LM_DIR = os.path.join(REPO_DIR, "data_lm")
parent_dir = os.path.abspath(os.path.join(__file__ ,"../.."))
DATA_DIR = os.path.join(parent_dir,'ds003020')
DATA_TRAIN_DIR = os.path.join(REPO_DIR, "data_train")
DATA_TEST_DIR = os.path.join(REPO_DIR, "data_test")
RESULT_DIR = os.path.join(REPO_DIR, "results")
FIGURE_DIR = os.path.join(REPO_DIR, "figures")

# encoding model parameters

STRIM = 5
MTRIM = 10
STIM_DELAYS = [1, 2, 3, 4]
RESP_DELAYS = [-4, -3, -2, -1]
ALPHAS = np.logspace(1, 3, 10)
ALPHAS_WR = np.logspace(-10, 10, 10)
NBOOTS = 50
VOXELS = 10000
CHUNKLEN = 40
GPT_LAYER = 9
GPT_WORDS = 5

# decoder parameters

RANKED = True
WIDTH = 200
NM_ALPHA = 2/3
LM_TIME = 8
LM_MASS = 0.9
LM_RATIO = 0.1
EXTENSIONS = 5

# evaluation parameters

NULL = 200
WINDOW = 20

# devices

GPT_DEVICE = "cuda"
EM_DEVICE = "cuda"
SM_DEVICE = "cuda"