## DL4CV Mid-Term Project (Spring, 2022)
###### Gerald McCollam

### Requirements
This project has been developed to run on Google Colab as an Jupyter notebook. No dependencies beyond what Colab supplies are required. It is recommended that the Colab runtime be set to 'GPU' and 'High Ram' but it will execute fine if these are unset. 

If a library is missing it may be installed into a Colab session with the following:  

```bash
!pip install <library>
```

If a runtime error occurs it is likely related to connection issues between Colab and Google Drive, or to input data not being available in the required form. The instructors have provided no guidance regarding how the GTSRB dataset should be made available for this assignment to run in a different environment; this has been left to the student to determine. 

#### Data Loading
First, if running Colab with Drive, create the directory 'DL4CV-2022' in your home directory and clone [this Github repository](git@github.com:geraldmc/DL4CV-2022.git) into DL4CV-2022. Your gdrive_path to the project should then look like the following:  

    gdrive_path = '/content/drive//MyDrive/DL4CV-2022/project-I/'

The notebook will attempt to load three zipped data files. 

    zip_path_train = gdrive_path + 'data/Final_Training.zip'
    zip_path_val = gdrive_path + 'data/Final_Validation.zip'
    zip_path_test = gdrive_path + 'data/Final_Test.zip'


Two of these (Final_Training.zip, Final_Test.zip) have been created by downloading from the GTSRB download site. The files used for the assignment are:

[GTSRB_Final_Training_Images.zip](https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip)

[GTSRB_Final_Test_Images.zip](https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Test_Images.zip)

The directory structure for the unzipped files is the following:

```
- Final_Training
  - Annotations
    - GT_Training.csv (this file is required)
    - GT-00000.csv
    - GT-00001.csv
  - Images
    - 00000
      - 00000_00000.ppm
      - 00000_00001.ppm
    - 00001
      - 00000_00000.ppm
      - 00000_00001.ppm
    - ...

- Final_Test
  - Images
    - 01089.ppm
    - 01090.ppm
    - ...
```
The file 'Final_Validation.zip' was created by using images 00000\*, 00001\* and 00002\* from each class in the training set. There are 23,220 files in the augmented validation set and 3,900 in the unaugmented set.   

#### Running 
Execute the Jupyter notebook `DL4CV-2022/project-I/main.ipynb`. It will run to completion using the `Run All` command in Colab.

#### Issues
If there are any questions please do not hesitate to text me at gerald.mccollam@gmail.com.