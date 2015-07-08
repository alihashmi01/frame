#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################################
# This code is available under the MIT License.
# Ali Hashmi, MIT Center for Civic Media
###################################################################################

import frame
# frame contains grammarmodule for extracting grammar
# frame contains testtext.txt, test file format (each document one line)
# frame contain corpusvector helper module
# frame __init__ = LDA represents documents as mixtures of topics 
# LDA topic modeling allows the users to discover frames of conversations  

FILENAME = "./frame/testtext.txt"
# format 11
# each document on new line

NUMTOPICS = 5
#number of frames/topics you want to generate 

ITERATIONS = 100
# ITERATIONS: The number of sampling iterations, a trade off between the time taken to complete sampling & the quality of the topic model.
# The # of iterations increases quality of the topic model


# See T. Griffiths and M. Steyvers: Finding scientific topics, Proc. of the National Academy of Sciences (2004) for choosing alpha/beta values

ALPHA = None 
# alpha_param = 0.5 default
# alpha = distributions for (per document) topic & beta = (per topic) word distributions
# smaller alpha = more sparse the distribution
# intuition: high alpha-value =  documents more similar in terms of what topics the docs contain

BETA = None
# beta_param = 0.5 default
# intuition: high beta-value  = topics more similar in terms of what words they contain

OUTPUTJSONFILE = "testtext.json"
# output file where data is saved

GRAM = 1
# 1, extract grammar
# this will clean the text

#usage
frame.generateTopicsParams(FILENAME,NUMTOPICS,ITERATIONS, ALPHA, BETA, OUTPUTJSONFILE, GRAM)

