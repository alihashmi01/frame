import frame


FILENAME = "./frame/testtext.txt"
# format 11
# each document on new line

NUMTOPICS = 5
#number of frames/topics you want to generate 

ITERATIONS = 100
# ITERATIONS: The number of sampling iterations, a trade off between the time taken to complete sampling & the quality of the topic model.
# The # of iterations increases quality of the topic model

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
# extract grammar

frame.generateTopicsParams(FILENAME,NUMTOPICS,ITERATIONS, ALPHA, BETA, OUTPUTJSONFILE, GRAM)
