library(stringi)
library(Matrix)
#library(iconv)
library(tm)

find_ngrams <- function(dat, n=1, verbose=FALSE) {
  library(pbapply)
  stopifnot(is.list(dat))
  stopifnot(is.numeric(n))
  stopifnot(n>0)
  if(n == 1) return(dat)
  pblapply(dat, function(y) {
    if(length(y)<=1) return(y)
    c(y, unlist(lapply(2:n, function(n_i) {
      if(n_i > length(y)) return(NULL)
      do.call(paste, unname(as.data.frame(embed(rev(y), n_i), stringsAsFactors=FALSE)), quote=FALSE)
    })))
  })
}



text_to_ngrams <- function(sents, n=2){
  tokens <- stri_split_fixed(sents, ' ')
  tokens <- find_ngrams(tokens, n=n, verbose=TRUE)
  token_vector <- unlist(tokens)
  bagofwords <- unique(token_vector)
  n.ids <- sapply(tokens, length)
  i <- rep(seq_along(n.ids), n.ids)
  j <- match(token_vector, bagofwords)
  M <- sparseMatrix(i=i, j=j, x=1L)
  colnames(M) <- bagofwords
  return(M)
}


clean <- function(docs) {
  docs <- removeNumbers(docs)
  docs <- removePunctuation(docs)
  docs <- stripWhitespace(docs)
  docs <- stemDocument(docs)
  
  return(docs)
}

decode <- function(text) {
  t1 <- iconv(text, from = "UTF-8", to = "ASCII")
  return(t1)
}

