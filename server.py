import os,json
from flask import request

from src.app import create_app
from src.config import nlp_package_initialization
from src.dontknow_class_evaluation import classify_unknown
from src.preprocessing import content_spliting
from src.signature_evaluation import signature_ner_evaluation

app = create_app() 
nlp,nltk=nlp_package_initialization("fr_core_news_sm")
print('Program is ready')

#Main funtion which analyze signature evalution results and decides block of text as signature or not
def main(nlp,complete_signature):
    signature_results=[]
    nonsignature_results=[]
    undecidedsignature_results=[]
    issue,signature=content_spliting(nlp,complete_signature,'Cordialement')
    if signature:
        for sign in signature:
            refined_sign=sign.splitlines()
            if len(refined_sign)>10:
                sign=os.linesep.join([s for s in refined_sign[:10] if s])
                issue[0]=issue[0]+ " "+os.linesep.join([s for s in refined_sign[11:] if s])
            
            signature_eval=signature_ner_evaluation(nlp,nltk,str(sign))
            patern_found=0
            
            for k, v in signature_eval.items():
                if v:
                    patern_found+=1
            if (patern_found ==0):
                #nonsignature_results.append((sign,patern_found,'F'))
                print("\n Suspected signature:  \n ------------------------------------------------------------------------ \n",sign," \n ------------------------------------------------------------------------ \n is not a signature and found to have ",(patern_found*100/4)," % matching with Signature pattern.")
                if classify_unknown(nlp,sign) =='T':
                    signature_results.append((sign,1,'T'))
                elif classify_unknown(nlp,sign) =='F':
                    nonsignature_results.append((sign,patern_found,'F'))
                else:
                    undecidedsignature_results.append((sign,patern_found,'U'))
            elif (len(refined_sign)<=5 and patern_found==1):
                signature_results.append((sign,patern_found,'T'))
                print("\n Suspected signature:  \n ------------------------------------------------------------------------  \n",sign,"\n ------------------------------------------------------------------------ \n is identified as signature and found to have ",(patern_found*100/4)," % matching with Signature pattern.")
            elif (len(refined_sign)>5 and patern_found<2):
                #nonsignature_results.append((sign,patern_found,'F'))
                print("\n Suspected signature:  \n ------------------------------------------------------------------------  \n ",sign,"\n ------------------------------------------------------------------------ \n is not a signature and found to have ",(patern_found*100/4)," % matching with Signature pattern.")
                if classify_unknown(nlp,sign) =='T':
                    signature_results.append((sign,1,'T'))
                elif classify_unknown(nlp,sign) =='F':
                    nonsignature_results.append((sign,patern_found,'F'))
                else:
                    undecidedsignature_results.append((sign,patern_found,'U'))
            else:
                signature_results.append((sign,patern_found,'T'))
                print("\n Suspected signature: \n ------------------------------------------------------------------------ \n ",sign,"\n ------------------------------------------------------------------------ \n is identified as signature and found to have ",(patern_found*100/4)," % matching with Signature pattern.")
        print("\n Issue: \n ------------------------------------------------------------------------ \n ",issue[0],"\n ------------------------------------------------------------------------ \n ")
    else:
        issue=complete_signature
    return issue,signature_results,nonsignature_results,undecidedsignature_results
    

@app.route('/analyze', methods=['POST'])
def analyze():
    complete_issue = request.data.decode("utf-8")
    #print(request_data)
    issue,signature_results,nonsignature_results,undecidedsignature_results=main(nlp,complete_issue)
    results= {
        "issue":issue,
        "signature":signature_results,
        "nonsignature":nonsignature_results,
        "undecidedsignature":undecidedsignature_results
    }
    #print("\n Issue part: \n",issue,"\n Identified Signature part: \n",signature_results,"\n Rejected Signature part: \n",nonsignature_results)
    return json.dumps(results)


@app.route('/healthcheck')
def healthcheck():
    return 'ok', 200


