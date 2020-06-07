from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from src.train import NamedEntityRecognizer


# TODO: Check if model directory/model file exists exists
# TODO: Add assertion for model output

# LOAD NAMED ENTITY RECOGNIZER
LOAD_PATH = "model/ner_model.gz"
ner = NamedEntityRecognizer()
ner.load(LOAD_PATH)


def test_single_input():
    """# TAG SINGLE SENTENCE

    Arguments:
        ner {NamedEntityRecognizer} -- NER model
    """
    
    test_input = ["EU", "rejects", "German", "call", "to", "boycott", "British", "lamb", "."]
    output = ner.tag(test_input)

    assert len(test_input) == len(output), "Number of tags not matched with number of tokens"

    return

def test_multiple_input():
    """# TAG SINGLE SENTENCE

    Arguments:
        ner {NamedEntityRecognizer} -- NER model
    """
    
    test_input = [
                ["EU", "rejects", "German", "call", "to", "boycott", "British", "lamb", ".",],
                ["BayerVB", "sets", "C$", "100", "million", "six-year", "bond", "."],
            ] 

    output = ner.tag_sents(test_input)

    assert len(test_input) == len(output), "Number of inputs not matched with number of outputs"
    
    return