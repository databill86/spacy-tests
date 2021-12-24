from spacy import Language
from spacy.lang.fr import French
from spacy.pipeline import AttributeRuler


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


@French.factory("custom_attr_ruler")  # doesn't work for packaging
# @Language.factory("custom_sent")  # work
def my_custom_attr_ruler(nlp, name):
    return CustomAttributeRuler(nlp)


class CustomAttributeRuler(AttributeRuler):

    def __init__(self, nlp: Language,
                 name="attr_ruler"):

        self.nlp = nlp

        super(CustomAttributeRuler, self).__init__(vocab=nlp.vocab, name=name, validate=True)

        self.add_rules_fix_bug_segmentation()

    def add_rules_fix_bug_segmentation(self):
        pattern = {'attrs': {'DEP': '', 'HEAD': 0, 'SENT_START': 0},
                   'index': 0,
                   'patterns': [[{}]]}
        self.add(patterns=pattern.get("patterns"), attrs=pattern.get("attrs"))

