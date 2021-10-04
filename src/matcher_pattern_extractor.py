
#Extract NER matched text
def matcher_extract_ner(content,nlp,patterns):
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(patterns)
    
    named_entities=[]
    doc=nlp(content)
    ents = list(doc.ents)
    for i in range(0,len(ents)): 
        if ents[i].label_ in ('PER','MISC','ORG'):
            named_entities.append(ents[i].text +" - "+ ents[i].label_)
    nlp.remove_pipe("entity_ruler")
    return named_entities

#Verify NER with NLTK
def nltk_ner_evaluation(nltk,content):
    ner_nltk = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(content)))
    return [i.label() for i in ner_nltk if hasattr(i, 'label') and i.label()=='PERSON']