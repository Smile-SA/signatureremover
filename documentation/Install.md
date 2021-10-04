## Installation steps
Step 1: 

Clone the package.

Step 2:

Build the docker image with the following command:

`sudo docker build -t signatureremover .`

Step 3: 

Run the docker image with the following command:

`sudo docker run -p 8080:8080 signatureremover`

### Usage
Signature removal code is accessible at port 8080. The input text for which the signature has to be removed needs to be passed alongside the body of the request. 

```
curl -X POST -i 'http://127.0.0.1:8080/analyze' --data 'Bonjour,


Je te fais un ticket en début d’am, peux-tu regarder s’il te plait ?
 
Merci à toi !

Cordialement,
XXX YYY
Développeur 
 
Tel : +33 (0)1 00 00 00 00
ABCTechnologies
100 Bis avenue de Bretagne
59000 Lille
 
xxx.yyy@org.fr  -  www.org.fr
@org'

```


### Results:

The program removes the signature portion from the text and share text portion and signature portion. The output looks as below.

**Text:**
```
Bonjour,


Je te fais un ticket en début d’am, peux-tu regarder s’il te plait ?

Merci à toi !
```


**Signature:**
```
Cordialement,
XXX YYY
Développeur 
 
Tel : +33 (0)1 00 00 00 00
ABCTechnologies
100 Bis avenue de Bretagne
59000 Lille
 
xxx.yyy@org.fr  -  www.org.fr
@org'

is identified as a signature and found to have 75.0% of matching with Signature patterns.
```
