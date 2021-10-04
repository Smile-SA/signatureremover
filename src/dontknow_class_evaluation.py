import os

#Validate for Dont know Class 
def classify_unknown(nlp,sign):
    refined_sign=sign.splitlines()
    if len(refined_sign)>1:
        name_portion=os.linesep.join([s for s in refined_sign[1:2] if s])
        signature_portion=os.linesep.join([s for s in refined_sign[:2] if s])
        doc = nlp(str(name_portion).strip()) #refined_sign[1:2]
        print("\n Signature is futher analyzed to find unknown signature \n ************************************* \n")
        if len(doc)<=4:
            if len(doc)==0:
                print("\n ",sign ,"\n unable to decide it as signature. \n ************************************* \n")
                return 'U'
            for token in doc:
                if token.morph.get("Gender") or token.morph.get("Person") or token.pos_ in ('ADJ'):
                    print("\n ",signature_portion  ,"\n is Signature \n ************************************* \n")
                    return 'T'
                elif len(doc)==1 and token.pos_ in ('PROPN','NOUN'):
                    print("\n ",signature_portion ,"\n unable to decide it as signature. \n ************************************* \n")
                    return 'F'
        else:
            print("\n ",signature_portion,"\n is not signature \n ************************************* \n")
            return 'F'
    else:
        print("\n ",sign,"\n is not signature \n ************************************* \n")
        return 'F'
                