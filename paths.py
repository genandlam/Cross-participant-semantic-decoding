import os
import config

# semantic clusters
CLUSTER_EM = os.path.join(config.RESULT_DIR, "clustering/%s/em.npy") # subject
CLUSTER_ID = os.path.join(config.RESULT_DIR, "clustering/%s/clusters.npy") # subject

# cortex data
ALIGNED_CORRS = os.path.join(config.RESULT_DIR, "cortex/aligned_bscorrs/%s.npy") # subject
ROI = os.path.join(config.RESULT_DIR, "cortex/roi/%s/%s.npy") # subject, region

# reference data
EM = os.path.join(config.RESULT_DIR, "encoding/%s/em.npy") # subject
WR = os.path.join(config.RESULT_DIR, "encoding/%s/wr.npy") # subject
NULL = os.path.join(config.RESULT_DIR, "encoding/%s/null.npy") # subject

# reconstruction results
RESULTS_REFERENCE = os.path.join(config.RESULT_DIR, "reconstruction/reference/%s.npy") # subject
RESULTS_MULTI = os.path.join(config.RESULT_DIR, "reconstruction/multi/%s/%s.npy") # modality, goal
RESULTS_SINGLE = os.path.join(config.RESULT_DIR, "reconstruction/single/%s/%s/%s.npy") # modality, goal, reference
RESULTS_SCALING_CROSS = os.path.join(config.RESULT_DIR, "reconstruction/scaling/cross/%s/%s/%s/%s.npy") # modality, minutes, sample, goal
RESULTS_SCALING_WITHIN = os.path.join(config.RESULT_DIR, "reconstruction/scaling/within/%s/%s/%s/%s.npy") # modality, minutes, sample, goal
RESULTS_ABLATION = os.path.join(config.RESULT_DIR, "reconstruction/ablation/%s/exclude_%s/%s.npy") # modality, roi, goal

# alignment results
ALIGNMENT = os.path.join(config.RESULT_DIR, "alignment/%s/%s/%s.npy") # modality, region, reference
ALIGNMENT_SCALING = os.path.join(config.RESULT_DIR, "alignment_scaling/%s/%s/%s/%s.npy") # modality, minutes, sample, reference