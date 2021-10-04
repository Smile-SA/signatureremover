import nltk,spacy
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

def nlp_package_initialization(model_name):

    #Download Spacy NLP model
    nlp = spacy.load(model_name)
    #Download NLTK package 
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('maxent_ne_chunker')
    nltk.download('words')
    return nlp,nltk

def signature_pattern_initialization() : 
    
    email_pattern = [[{"LIKE_EMAIL": True}]]

    phoneno_pattern = [[{"ORTH": "+33"},{"OP": "?"},{"SHAPE": "d"},{"OP": "?"},{"SHAPE": "dd"},
                            {"OP": "?"},{"SHAPE": "dd"},{"OP": "?"},{"SHAPE": "dd"},{"OP": "?"},{"SHAPE": "dd"}],
                        [{"ORTH": "+33"},{'ORTH': '('}, {'TEXT':{'REGEX':'[0]\)*'}},{"SHAPE": "dd"},
                            {"OP": "?"},{"SHAPE": "dd"},{"OP": "?"},{"SHAPE": "dd"},{"OP": "?"},{"SHAPE": "dd"}],
                        [{'TEXT':{'REGEX':'[0][0-9]{9}'}}],
                        [{"OP": "?"},{"SHAPE": "dd"},{"OP": "?"},{"SHAPE": "dd"},{"OP": "?"},{"SHAPE": "dd"},
                            {"OP": "?"},{"SHAPE": "dd"},{"OP": "?"},{"SHAPE": "dd"}],
                        [{'TEXT':{'REGEX':'[0][0-9]\.[0-9]{2}\.[0-9]{2}\.[0-9]{2}\.[0-9]{2}'}}]]
    
    address_pattern= [[{"TEXT": {"REGEX": "^(?:[0-8]\d|9[0-8])\d{3}$"}}],[{"LOWER": "rue"}],
                      [{"LOWER": "avenue"}],[{"LOWER": "boulevard"}],[{"LOWER": "chemin"}],
                      [{"LOWER": "bureaux"}],[{"LOWER": "batiement"}],[{"LOWER": "bat"}]]

    ner_pattern = [{"label": "ORG", "pattern": [{"LOWER": "www.alterway.fr"}], "id": "alterway"},
            {"label": "ORG", "pattern": [{"LOWER": "@alterway"}], "id": "alterway"},
            {"label": "LOC", "pattern": [{"LOWER": "saint-cloud"}], "id": "saint-cloud"}
           ]
    return email_pattern,phoneno_pattern,address_pattern,ner_pattern