from .model_zoo import get_model
from .model_store import get_model_file
from .base import *
from .fcn import *
from .psp import *
from .encnet import *
from .danet import *
from .danetPSP import *
from .danet_kp import *

def get_segmentation_model(name, **kwargs):
    from .fcn import get_fcn
    models = {
        'fcn': get_fcn,
        'psp': get_psp,
        'encnet': get_encnet,
        'danet': get_danet,
        'danetpsp': get_danetpsp,
        'danet_kp': get_danet_kp,
    }
    return models[name.lower()](**kwargs)
