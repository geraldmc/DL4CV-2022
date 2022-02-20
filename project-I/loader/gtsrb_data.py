import torch
import os
import pandas as pd
from torch.utils.data import Dataset
#from torchvision.io import read_image
import torchvision.transforms as transforms
import numpy as np
from PIL import Image


class GTSRB(Dataset):

    def __init__(self, root_dir, transform=None, train=True):
        """
        """
        self.root_dir = root_dir
        if train:
            self.sub_directory = 'Training'
            self.csv_file_name = 'GT_Training.csv'
        self.transform = transform

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
        img = Image.open(img_path)
        tensor_img = torch.from_numpy(np.array(img)) # see https://github.com/pytorch/vision/issues/2989
        #img = read_image(img_path)

        classId = self.csv_data.iloc[idx, 7]

        if self.transform is not None:
            img = self.transform(img)

        return img, classId