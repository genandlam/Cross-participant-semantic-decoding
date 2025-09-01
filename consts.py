# subject
SUBJECTS = ["UTS02", "UTS03",  "UTS09"]
CLUSTER_SUBJECTS = ["UTS01", "UTS05", "UTS06", "UTS07"]
NUM_VOXELS = dict(zip(["UTS02", "UTS03", "UTS09"], [94251, 95556, 98336]))

# stimuli
MOVIES = [
    ["laluna", "float", "lifted", "wind", "theblueumbrella", "walle", "sintel", "up", "partlycloudy", "bao", "piper", "toystory2", "presto"]
]
STORIES = [
    ["alternateithicatom", "souls", "avatar", "legacy", "odetostepfather"], 
    #["undertheinfluence", "howtodraw", "myfirstdaywiththeyankees", "naked", "life"], 
    #["stagefright", "tildeath", "sloth", "exorcism"], 
    #["haveyoumethimyet", "adollshouse", "inamoment", "theclosetthatateeverything", "adventuresinsayingyes", "buck"], 
    #["swimmingwithastronauts", "thatthingonmyarm", "eyespy", "itsabox", "hangtime"],
    #["breakingupintheageofgoogle", "treasureisland", "shoppinginchina", "onlyonewaytofindout", "penpal"], 
    #["goingthelibertyway", "kiksuya", "thepostmanalwayscalls", "backsideofthestorm", "sweetaspie", "thetiniestbouquet"],
    #["lifeanddeathontheoregontrail", "thefreedomridersandme", "thumbsup", "becomingindian", "waitingtogo"],
    #["singlewomanseekingmanwich", "whenmothersbullyback", "superheroesjustforeachother", "gpsformylostidentity", "catfishingstrangerstofindmyself", "christmas1940"],
    #["stumblinginthedark", "forgettingfear", "bluehope", "lifereimagined", "ifthishaircouldtalk", "againstthewind"]
]

# regions
ROI_FRONTAL = ["superiorfrontal", "rostralmiddlefrontal", "caudalmiddlefrontal", "parsopercularis", "parstriangularis", "parsorbitalis", "lateralorbitofrontal", "medialorbitofrontal", "precentral", "paracentral", "frontalpole"] + ["rostralanteriorcingulate", "caudalanteriorcingulate"]
ROI_PARIETAL = ["superiorparietal", "inferiorparietal", "supramarginal", "postcentral", "precuneus"] + ["posteriorcingulate", "isthmuscingulate"]
ROI_TEMPORAL = ["superiortemporal", "middletemporal", "inferiortemporal", "bankssts", "fusiform", "transversetemporal", "entorhinal", "temporalpole", "parahippocampal"]
ROI_OCCIPITAL = ["lateraloccipital", "lingual", "cuneus", "pericalcarine"]
ROI = ROI_FRONTAL + ROI_PARIETAL + ROI_TEMPORAL + ROI_OCCIPITAL
ABLATE_REGIONS = ["lh_anterior", "lh_posterior", "rh_anterior", "rh_posterior", "concrete", "social", "place", "temporal", "people"]