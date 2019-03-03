# Data Download and Preprocessing from GDC Data Portal

## Installing requirements

```
pip install -r requirements.txt
```

## Data download
- Data has been downloaded from [GDC Data Portal](https://portal.gdc.cancer.gov/)
- We have downloaded [cancer data for head and neck](https://portal.gdc.cancer.gov/exploration?filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22Other%20and%20unspecified%20major%20salivary%20glands%22%2C%22Other%20and%20unspecified%20parts%20of%20tongue%22%2C%22Larynx%22%2C%22Other%20and%20ill-defined%20sites%20in%20lip%2C%20oral%20cavity%20and%20pharynx%22%2C%22Floor%20of%20mouth%22%2C%22Nasopharynx%22%2C%22Tonsil%22%2C%22Other%20and%20unspecified%20parts%20of%20mouth%22%2C%22Base%20of%20tongue%22%2C%22Gum%22%2C%22Oropharynx%22%2C%22Hypopharynx%22%2C%22Trachea%22%2C%22Palate%22%2C%22Lip%22%5D%7D%7D%5D%7D) in the form of .maf files from [GDC Portal](https://portal.gdc.cancer.gov/)
- The step-by-step approach for data download:
  - Downloading GDC client tool for data transfer. GDC client tool can be downloaded from [here](https://gdc.cancer.gov/access-data/gdc-data-transfer-tool)
  - The next step is to download the correspoding manifest file for head and neck cancer data. How to download the manifest file for head and neck cancer data is illustrated in visul below:
  
  ![](media/dd.gif)
  
  - The next step is to download data using [GDC data transfer client]() and the manifest file you downloaded in the previous step. Start data download by running GDC data transfer client using following command:
```
# An example
./gdc-client download -m gdc_manifest.2019-03-03.txt
```

- In directory __data__ can be found data downloaded using __data/gdc_manifest.2019-03-01.txt__ manifest file.
  - Out of 27 files from gdc_manifest.2019-03-01.txt : successfully downloaded: 12 and failed downloads: 15.
- In directory __data_hn__ can be found (head and neck cancer) data downloaded using __data_hn/gdc_manifest.2019-03-03.txt__ manifest file.
  - Out of 318 files from gdc_manifest.2019-03-03.txt : successfully downloaded: 132 and failed downloads: 186.
 

## Data preprocessing and running 

- Data selected, as illustrated above in animated figure, has been downloaded and it is available in shared Google Drive folder (__data_hn__). 
- Files (.maf) in this directory have been used as input data from __dd_gdc/dd_gdc.py__ script.
This script can be run using the following command:
  - __data_hn/__: directory with input .maf files
  - __.maf.gz__: file extension of input files
  - __all__: all files from input directory (data_hn)
  - __out_dir_hn__: directory with output files
```
python dd_gdc/dd_gdc.py data_hn/ .maf.gz all out_dir_hn
```
- The script bascially does some basic file manipulation and runs the [delmh](https://github.com/xqrongm/delmh) microhomology tool on the .maf files in:
  - __data__ directory and outputs results to __out_dir__
  - __data_hn__ directory and outputs results to __out_dir_hn__
  
## Reproducing results and general comments and suggestions
- It would be easier to reproduce results if README.md file in [delmh](https://github.com/xqrongm/delmh) repository contains more information about following things:
  - What type of input files it accepts?
  - What are input files besides .maf files
  - Description of algorithm [delmh](https://github.com/xqrongm/delmh) maybe in the form of some kind of flowchart (an example of that in __docs/mh_diagram.jpg__)
  - The sentence "The .maf files used were downloaded from the Genomic Data Commons Data Portal (https://
portal.gdc.cancer.gov/)." could be a bit more detailed in terms of how actually data is downloaded. Maybe a written description of the animated gif I provided above where information about the exact path of how data is downloaded.
  - Command provided in the current README.md file is not informative enough and it could be potentially reduced
  - In the long run this algorithm could be converted to a web-based application or an executable program
