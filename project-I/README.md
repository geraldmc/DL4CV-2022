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

#### Training 


#### Validation

As the model trains, model checkpoints are saved to files such as `model_x.pth` to the current working directory.
You can take one of the checkpoints and run:

```
python evaluate.py --data [data_dir] --model [model_file]
```

#### Commands to interact with AWS instance:

ssh -i "gtsrb.pem" ubuntu@ec2-18-119-140-152.us-east-2.compute.amazonaws.com

scp -i "gtsrb.pem" [file] ubuntu@ec2-18-119-140-152.us-east-2.compute.amazonaws.com:~/.

#### Design inspired by https://github.com/abursuc/dldiy-gtsrb
