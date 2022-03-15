import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from PIL import Image

from loader.transforms import base_transform

# See: https://debuggercafe.com/custom-dataset-and-dataloader-in-pytorch/

class GTSRB_Test(Dataset):

    def __init__(self, root_dir, test=True):
        """
        """
        self.root_dir = root_dir
        if test:
            self.sub_directory = 'Final_Test/Images/'
            self.csv_file_name = 'GT-final_test.csv'
        self.transform = base_transform
        self.frame = None

        csv_file_path = os.path.join(self.root_dir, 
                                     self.sub_directory, 
                                     self.csv_file_name)
        
        self.csv_data = pd.read_csv(csv_file_path, sep=';')

    def __len__(self):
        return len(self.csv_data)

    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, 
                                self.sub_directory,
                                self.csv_data.iloc[idx, 0])
        img_frame_coords = (    self.csv_data.iloc[idx, 3:7]) # Roi.X1, Roi.Y1, Roi.X2, Roi.Y2
        
        img = Image.open(img_path)
        class_id = self.csv_data.iloc[idx, 7]

        if self.transform is not None:
            img = self.transform(img)

        return img, class_id