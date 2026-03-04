source("fast-ngrams.R")
con <- file("scripts_clean_2.csv", "r") 
data <- readLines(con, encoding = 'UTF-8')
close(con)

data <- clean(data)
onegram <- text_to_ngrams(decode(data), 1)
bigram <- text_to_ngrams(decode(data), 2)
trigram <- text_to_ngrams(decode(data), 3)

# How to calculate ngrams for a term
#sum(blogs_ngram[,colnames(onegram) == 'term'])
