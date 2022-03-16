## DL4CV Mid-Term Project (Spring, 2022)
###### Gerald McCollam

### Requirements
This project has been developed to run as a Google Colab notebook. No dependencies beyond what Colab supplies should be required. The notebook will run to completion without error by following these instructions. If a library is missing it may be installed in Colab with the following:  

```bash
!pip install <library>
```

If an error occurs it is likely due to the input data not being available in the required form. The class instructors provide no guidance regarding how the GTSRB datasets should be made available for this assignment; it has been left to the student to determine this. 

#### Data Loading
The notebook will attempt to load three data files:

    zip_path_train = gdrive_path + 'data/Final_Training.zip'
    zip_path_val = gdrive_path + 'data/Final_Validation.zip'
    zip_path_test = gdrive_path + 'data/Final_Test.zip'

Two of these (Final_Training.zip, Final_Test.zip) have been created by downloading from the GTSRB download site: 

https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html

The file 'Final_Validation.zip' was created by using images 00000\*, 00001\* and 00002\* from each class. There are 23,220 files in the augmented validation set and 3,900 in the unaugmented set.   

#### Features

1. Spatial Transformer Networks: [STN](http://torch.ch/blog/2015/09/07/spatial_transformers.html)
2. Adam Optimizer
3. BatchNorm
4. Dropout
5. Data Augmentation and Transforms

<h2>Methods used</h2>

<ul>
<li>CNN and Spatial transformer network: CNN with 3 layers, 2 fully connected layers and 1 spatial transformer network layer with two convolutional layers and one fully connected layer (CNN feature maps: 3 -> 100 -> 150 -> 250 -> 350, filter size: [5, 3 ,3], spatial transformer network feature maps: 3 -> 8 -> 10 -> 32, spatial transformer network filter size: [7,5])</li>

<li>Data augmentation: Both training time and test time data augmentation proved to be beneficial. The manipulations applied were shearing, translating, image jittering in terms of brightness, hue, saturation and contrast, center cropping, rotating and horizontal and vertical flipping. These extent of these manipulations was applied after study of the training images - for instance, images were rotated only up to +/-15 degrees since that is the range of slant that some of the signs were found to be at. Similarly image brightness was manipulated liberally in both directions to both correct for the darkness that distorted some images and to create further examples of such badly distorted images for training. Test time augmentation involved the exact same manipulations as the train time augmentation. All images were normalized after manipulations. The final model had 392,090 images for training, about 10 times the original dataset size, through data augmentation.</li></ul>


#### Training 


#### Validation


#### Commands to interact with AWS instance:

ssh -i "gtsrb.pem" ubuntu@ec2-18-119-140-152.us-east-2.compute.amazonaws.com

scp -i "gtsrb.pem" [file] ubuntu@ec2-18-119-140-152.us-east-2.compute.amazonaws.com:~/.

#### Design inspired by https://github.com/abursuc/dldiy-gtsrb
