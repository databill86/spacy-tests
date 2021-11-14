from spacy import Language
from spacy.lang.fr import French


@French.factory("custom_sent")  # doesn't work for packaging
# @Language.factory("custom_sent")  # work
def my_senter(nlp, name):
    return CustomSenter(nlp)


class CustomSenter:
    def __init__(self, nlp):
        pass

    def __call__(self, doc):
        for tok in doc:
            tok.is_sent_start = False
        doc[0].is_sent_start = True
        return doc

