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
## Data preprocessing

- Data selected, as illustrated above in animated figure, has been downloaded and it is available in shared Google Drive folder (data_hn)


## Reproducing results

- Reproducing analysis by running the dd_gdc.py script
```
python dd_gdc/dd_gdc.py data_hn/ .maf.gz all out_dir_hn
```


## General comments and suggestions

## Data download:
- Successfully downloaded: 12
- Failed downloads: 15



