import pandas as pd
import numpy as np
import torch
from torchvision.transforms import *

# Transformations
class PreProccessing:
    def __init__(self,to_tensor:bool,random_vertical_flip:bool,color_jitter:bool=True,random_grayscale:bool=True,random_horizontal_flip:bool=True,random_rotation:bool=True) -> None:
        self.color_jitter=color_jitter
        self.random_grayscale=random_grayscale
        self.random_horizontal_flip = random_horizontal_flip
        self.random_rotation=random_rotation
        self.random_vertical_flip=random_vertical_flip
        self.to_tensor = to_tensor
        self.compose_list = []
    
    def color_jitter_pp(self):
        self.compose_list.append(ColorJitter(0.125,0.125,0.125,0.125))
    def random_grayscale_pp(self):
        self.compose_list.append(RandomGrayscale())
    def random_horizontal_flip_pp(self):
        self.compose_list.append(RandomHorizontalFlip())
    def random_rotation_pp(self):
        self.compose_list.append(RandomRotation(180))
    def random_vertical_flip_pp(self):
        self.compose_list.append(RandomVerticalFlip())
    def to_tensor_pp(self):
        self.compose_list.append(ToTensor())
