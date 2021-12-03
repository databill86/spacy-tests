"""
python -m spacy download -d fr_core_news_lg-3.2.0

"""
import pathlib

import spacy
import logging as logger

import my_pipelines  # noqa

nlp = spacy.load("fr_core_news_lg", exclude=["ner", "parser", "attribute_ruler"])

nlp.add_pipe("custom_attr_ruler")
nlp.add_pipe("custom_sent")


text = "Ce n'est  pas logique! Envoyé depuis mon iPhone..."

doc = nlp(text)
for token in doc:
    print(token, token.pos_)
for sent in doc.sents:
    logger.info(sent)

save = True
if save:
    path_model = "../models/my_model"
    pathlib.Path(path_model).mkdir(parents=True, exist_ok=True)
    logger.info(f"Saving custom model to {path_model}")
    nlp.to_disk(path_model)

    path_model_packaged = "../models/packaged"
    pathlib.Path(path_model_packaged).mkdir(parents=True, exist_ok=True)


