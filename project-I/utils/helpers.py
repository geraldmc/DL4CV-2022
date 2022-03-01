# Project1_utilities -----------------------------

import os
import csv
import glob
import shutil
import pandas as pd

import bz2
import _pickle as cPickle
from collections import defaultdict, namedtuple
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Compress and pickle a file 
def compress_pickle(filename, data):
  with bz2.BZ2File(filename + '.pbz2', 'w') as f: cPickle.dump(data, f)

# Load a compressed pickle file
def decompress_pickle(file):
  data = bz2.BZ2File(file, 'rb')
  data = cPickle.load(data)
  return data

def getImagesLabels(path):
    '''
    Read in the images and the corresponding class ids.
    Adapted from: https://benchmark.ini.rub.de/gtsrb_dataset.html#Codesnippets
    '''
    images = [] # images
    labels = [] # corresponding labels
    # loop over all classes (42)
    for c in range(0,43):
        prefix = path + '/' + format(c, '05d') + '/' # subdirectory for class
        gtFile = open(prefix + 'GT-'+ format(c, '05d') + '.csv') # annotations file
        gtReader = csv.reader(gtFile, delimiter=';') # csv parser for annotations file
        next(gtReader)
        # loop over all images in current annotations file
        for row in gtReader:
            images.append(plt.imread(prefix + row[0])) # 1st column is the filename
            labels.append(row[7]) # 8th column is the label
        gtFile.close()
    return images, labels

def getMetaInfo(path):
    '''
    Read in the meta data for all files.
    '''
    attribute_list = []
    
    for c in range(0,43):
        prefix = path + '/' + format(c, '05d') + '/' # class subdirectory
        gtAttributes = pd.read_csv(prefix + 'GT-'+ format(c, '05d') + '.csv', sep=';') # a dataframe
        attribute_list.append(gtAttributes.to_dict('index')) # a dictionary
    return attribute_list # a list of dictionaries

# Dictionary for class labels
def make_class_dict(path):
    ''' path='data/signnames.csv'
    '''
    classes = pd.read_csv(path)
    return dict(zip(classes.ClassId, classes.SignName))

def renameImageFiles(path):
    '''
    Copy and rename all files under the supplied GTSRB/Final_Training/Images dir.
    - i.e. for the directory '00000' rename all contained files from
    00000_00000.ppm to 00000_00000_00000.ppm (append the class directory name to 
    the file) such that:
    00000/00000_00000.ppm becomes 00000_00000_00000.ppm,
    00001/00000_00000.ppm becomes 00001_00000_00000.ppm,
    etc.
    
    This allows placing all files and a single csv annotations file under one directory!
    
    NOTE: This executes from whereever the utilities.py file is, all paths are relative. 
    FIXME: This function is should only run once. Check to see if it's already been done. 
    '''
    import os
    import csv
    import glob
    import shutil

    rel_root_dir = '../../../..'
    src_dir = os.getcwd()+'/data/GTSRB/Final_Training/Images/'
    dest_dir = '../../../../Training/'
    subdirectories = ['00000','00001','00002','00003','00004','00005','00006','00007','00008',
                      '00009','00010','00011','00012','00013','00014','00015','00016','00017',
                      '00018','00019','00020','00021','00022','00023','00024','00025','00026',
                      '00027','00028','00029','00030','00031','00032','00033','00034','00035',
                      '00036','00037','00038','00039','00040','00041','00042']

    for idx in range(len(subdirectories)):
        txt = subdirectories[idx]+'_'
        os.chdir(src_dir+'/'+subdirectories[idx])
        files = [i for i in sorted(glob.glob('*.{}'.format('ppm')))]
        for item in files:
            shutil.copy(item, dest_dir+txt+item)
        os.chdir(rel_root_dir)
        
def combine_CSV(path):
    
    import os
    import csv
    import glob
    import shutil
    
    cwd = os.getcwd()
    
    all_csv_filenames = []
    src_dir = os.getcwd()+'/data/GTSRB/Final_Training/Images/'
    dest_dir = '../../../../Training/' # relative to the above
    
    subdirectories = ['00000','00001','00002','00003','00004','00005','00006','00007','00008',
                      '00009','00010','00011','00012','00013','00014','00015','00016','00017',
                      '00018','00019','00020','00021','00022','00023','00024','00025','00026',
                      '00027','00028','00029','00030','00031','00032','00033','00034','00035',
                      '00036','00037','00038','00039','00040','00041','00042']
    
    for idx in range(len(subdirectories)):
        all_csv_filenames.append('GT-'+subdirectories[idx]+'.csv')
    for idx in range(len(subdirectories)):    
        os.chdir('data/GTSRB/Final_Training/Images/'+subdirectories[idx])
        shutil.copy(all_csv_filenames[idx], dest_dir)
        os.chdir(cwd)

    # combine all into one.
    combined_csv = pd.concat([pd.read_csv(f, sep=';') for f in all_csv_filenames ])
    
    # export to project root.
    combined_csv.to_csv( "GT_Training.csv", index=False, encoding='utf-8-sig')
    
def show_framed_img(img, img_frame):
    fig, ax = plt.subplots(1)
    ax.imshow(img)
    rect = patches.Rectangle((img_frame[0][1],img_frame[1][1]),
                             img_frame[2][1]-img_frame[0][1],
                             img_frame[3][1]-img_frame[1][1],
                             linewidth=1, edgecolor='#00ff00',facecolor='none')
    ax.add_patch(rect)
    plt.show()
    
    
'''
for idx in range(len(subdirectories)):
    os.chdir(subdirectories[idx])
    subdir_list.append(os.getcwd()[-5:])
    os.chdir('..')
'''