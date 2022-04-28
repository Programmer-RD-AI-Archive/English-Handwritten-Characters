import pandas as pd
import numpy as np
import torch
from torchvision.transforms import *

# Transformations
class PreProccessing:
    def __init__(self,color_jitter) -> None:
        self.color_jitter=color_jitter
        self.compose_list = []
    
    def color_jitter_pp(self):
        self.compose_list.append()
