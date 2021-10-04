## Introduction

This document explains motivations and needs for an email signatures removal system. 

Signature is an important part of any email, as it lists different modes of contacts for its sender. Since they are present in every single emails, signatures can become troublesome in few cases : 
- email chains or web services message content. For example, when the communication chain grows multiple signatures will be present in content of conversations, which are recurrent and may provide unwanted information, as well as making the emails gain in weight. 
- data analysis. Furthermore, this ```signature``` content will be present when emails content is used for data processing. 
- anonymization. Also, ```signature``` holds private information which requires to be removed prior using third party data analysis services or publishing datasets.

## Technical Motivation

Current NLP tools are limited in their ability to build up custom ontologies made of simple ontologies. Moreover and considering email signatures, their structure always change from one individual to an another : in content, content type and number of information. In a way, every signature has its own pattern. 

In this project we explored how to set up an NLP pipeline, iteratively filtering the input text content to dynamically identify subsets of it ; these subsets are then proposed to a classifier, accepting or revoking the subset as a candidate. In our case a ```signature``` candidate.

In our tests, our ([Redmine Advise similarity](https://gitlab.com/alter-way-rnd/redmine-advise-plugin)) plugin gets a 10% improvement over its results by not considering Signature information in it.