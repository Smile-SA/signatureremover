## Configuration 

Signatures are constructed with multiple components like `Name, Designation, Email, Phone Number, Address`, at the bare minimum with name alone or with all components. In order to ensure dynamic identification, system is built upon following invidual components. 

- Named Entity Recognition (Name and Designation)
- Spacy Token attributes Email 
- Regex method Phone number 
- Spacy Patten identification Address 

### Composition

As our system generates only _French data_, solution developed to identify _**French signatures**_ in it. Algorithm uses **Spacy french predefined model**(`fr_core_news_sm`) and **NLTK packages**(`punkt,maxent_ne_chunker,words,averaged_perceptron_tagger`). Targeted French patterns are used in Postal code, Phone number and address identification. 

### Usage

The french word `Cordialement` is used as an identifier at **Level-0** to split issue with suspected signature portion of text. If needed, this can be enhanced by adding further identifiers. Adapting this algorithm for different language identifiers has to be changed accordingly.  In **Level-1** where the suspected portion is confirmed on signature or not with above listed components.  

**Named Entity Recognition (NER):**

NER identifies a given token (word in spacy context) as person or organization. Sometimes Spacy NLP models fail to identify the names so the tokens are futher analyzed with NLTK method to find words with "PERSON" as label. This is NER minimum requirement to categorize a block of text as ```signature```.

**Spacy Token attribute Email:**

"IS_EMAIL" is token attribute used to identify given token as Email or No. It returns 'True' if it is email. 

**Regex Method for Phone numbers:**

Phone numbers change according to the geo-location. Since our dataset uses only French data, French Phone numbers are represented in multiple ways  +33 0N NN NN NN NN or 0N NN NN NN NN or +33 N NN NN NN NN (N is individual digit). A pattern is created comprising most posibilities and used here.

**Spacy Patten Identifying address:**

Address in signature is mostly French so we had Regex patten to identify French postalcode and locate most commonly used words to identify streets like _rue, avenue, chemin_. 

When a suspected portion matches each patterns it increases similarity score of the suspected block of text. 

**Level-2** is the next level of validation on the block of text which is rejected by previous stage. The token is analysized for grammatical forms ("gender, person") with Spacy morphing technique. If it identifies them the tokens are maked as ```signature```.

### Customize for your needs

As a pretrained French model is used it supports the languages of French variants for Canada, Switzerland, Luxembourg, Belgium. To make this code more suitable for other languages and countries below options has to be customized.

1. Change the models with respective language in 

    a. `Dockerfile`

    b. `server.py`
    
    c. `signature_ner_evaluation.py`


2. Change phone number regex pattern for respective countries in `signature_pattern_initialization()` function of `config.py` file .
3. Change the Postal code pattern and street identifier words for respective country in `signature_pattern_initialization()` function of `config.py` file.

By customizing above three things the code can identify ```signature``` blocks of respective language and country. 