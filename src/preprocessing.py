import os,re
from spacy.matcher import Matcher
from bs4 import BeautifulSoup

#Extract paterns retuns matched docs
def matcher_extract(nlp,doc,patterns):
    matcher = Matcher(nlp.vocab)
    matcher.add("Matcherextracter", patterns)
    matches = matcher(doc)
    return matches

#Split issue and suspected signature
def content_spliting(nlp,complete_issue,identifier):
    complete_issue=BeautifulSoup(complete_issue,'html.parser').get_text()
    doc=nlp(complete_issue)
    pattern = [[{"TEXT": identifier}],[{"ORTH": identifier.lower()}]]
    issue=[]
    signature=[]
    matches=matcher_extract(nlp,doc,pattern)
    
    if len(matches) == 1:
        signature.append(doc[matches[0][1]:].text)
        issue.append(doc[:matches[0][1]].text)
    elif(len(matches) > 1):
        for i in range(0,len(matches)):
            if i+1<len(matches):
                if i==0:
                    issue.append(doc[:matches[i][1]].text)
                signature.append(doc[matches[i][1]:matches[i+1][1]].text)
            else: 
                signature.append(doc[matches[i][1]:].text)
                    
    return issue,signature_preprocessing(signature)
   
#Clean unnecessary tags
def signature_cleaner(text):
    rules = [ 
            {r'\*': u''},{r'>': u''}
            ]
    for rule in rules:
        for (k, v) in rule.items():
            regex = re.compile(k)
            text = regex.sub(v, text)
        text = text.rstrip()
    return text

#Preprocessing text
def signature_preprocessing(signature):
    #Clean up Signature
    eachlines=[]
    newlines=[]
    for i in range(0, len(signature)):
        signature[i]=signature_cleaner(signature[i])
        eachlines.append(BeautifulSoup(signature[i], 'html.parser').get_text())

    #Removing Extra blank lines
    for i in eachlines:
        newlines.append(os.linesep.join([s for s in str(BeautifulSoup(i, 'html.parser')).splitlines() if s]))
    return newlines
