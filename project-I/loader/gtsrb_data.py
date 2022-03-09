#import os
#import torch
#import torchvision
#from torch.utils.data import Dataset
#import torchvision.transforms as transforms
#import torch.nn as nn
#import torch.nn.functional as F
#import torch.optim as optim 
#import numpy as np
#import pandas as pd

import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from PIL import Image

# See: https://debuggercafe.com/custom-dataset-and-dataloader-in-pytorch/

class GTSRB(Dataset):

    def __init__(self, root_dir, transform=None, train=True):
        """
        """
        self.root_dir = root_dir
        if train:
            self.sub_directory = 'training'
            self.csv_file_name = 'GT_Training.csv'
        self.transform = transform
        self.frame = None

        csv_file_path = os.path.join(self.root_dir, 
                                     self.sub_directory, 
                                     self.csv_file_name)
        
        self.csv_data = pd.read_csv(csv_file_path, sep=';')
        
        #self.transform = transforms.Compose([transforms.Resize([256, 256]),
        #                                     #transforms.RandomCrop(224),
        #                                     #transforms.RandomHorizontalFlip(),
        #                                     transforms.ToTensor()])

    def __len__(self):
        return len(self.csv_data)

    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, 
                                self.sub_directory,
                                self.csv_data.iloc[idx, 0])
        img_frame_coords = (    self.csv_data.iloc[idx, 3:7]) # Roi.X1, Roi.Y1, Roi.X2, Roi.Y2
        
        img = Image.open(img_path)
        tensor_img = torch.from_numpy(np.array(img)) # see https://github.com/pytorch/vision/issues/2989
        #img = read_image(img_path)

        class_id = self.csv_data.iloc[idx, 7]

        if self.transform is not None:
            img = self.transform(img)

        return img, class_id, img_frame_coords