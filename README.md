
# Installation

## Create a conda environment
```
conda create --name nlp-spacy-tests python=3.8
conda activate nlp-spacy-tests
pip install -r requirements.txt 
python -m spacy download fr_core_news_sm
```


## Test the model & save it to disk 

> cd src && python model.py


## Package the model 

> cd .. && python -m spacy package models/my_model models/packaged --name=custom_packaged_spacy --version=0.0.1 --code=src/my_pipelines.py
	

