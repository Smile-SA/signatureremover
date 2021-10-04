from anonymization import Anonymization, SignatureAnonymizer
from src.config import signature_pattern_initialization
from src.matcher_pattern_extractor import matcher_extract_ner, nltk_ner_evaluation


#Main Signature evalution function
def signature_ner_evaluation(nlp,nltk,content):
    signature_anomizer=SignatureAnonymizer(Anonymization('fr_FR'),'fr_core_news_sm')
    sigature_elements={"ner":None,"phoneno":None,"email":None,"address":None}

    email_pattern,phoneno_pattern,address_pattern,ner_pattern=signature_pattern_initialization()
    sigature_elements["email"]=signature_anomizer.anonymize(content,email_pattern) 
    sigature_elements["phoneno"]=signature_anomizer.anonymize(content,phoneno_pattern) 
    sigature_elements["address"]=signature_anomizer.anonymize(content,address_pattern)
    sigature_elements["ner"]=matcher_extract_ner(content,nlp,ner_pattern)
    if not [i for i in sigature_elements["ner"] if i.find("PER")!= -1]:
        sigature_elements["ner"]=nltk_ner_evaluation(nltk,content)
    #print("Signature patterns identified are: \n ",sigature_elements)
    return sigature_elements