# Getting Started

Create a conda environment using the conda config file `environment.yml`.
The conda config file works only on the OS it was generated on (MacOS for me).

```bash
conda create -f environment.yml
```
Install all dependencies using `conda install`.

```bash
cd name-of-model
```
Install all dependencies using `conda install`.

Access to DREAMER and [MAHNOB-HCI](https://mahnob-db.eu) is given only to .edu accounts on request.  
Once downloaded, add your datasets into `datasets/`.

### Training

```bash
python main.py --phase train
```

### Testing

```bash
python main.py --phase test
```
