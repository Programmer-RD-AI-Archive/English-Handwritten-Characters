import pandas as pd
import numpy as np
import torch
from torchvision.transforms import *

# Transformations
class PreProccessing:
    def __init__(self,color_jitter,random_grayscale) -> None:
        self.color_jitter=color_jitter
        self.random_grayscale=random_grayscale
        self.compose_list = []
    
    def color_jitter_pp(self):
        self.compose_list.append(RandomGrayscale(0.125,0.125,0.125,0.125))
    def random_grayscale_pp(self):
        self.compose_list.append(ColorJitter(0.125,0.125,0.125,0.125))
    def color_jitter_pp(self):
        self.compose_list.append(ColorJitter(0.125,0.125,0.125,0.125))
    def color_jitter_pp(self):
        self.compose_list.append(ColorJitter(0.125,0.125,0.125,0.125))
    