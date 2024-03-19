# NLP Gensim: most common and most important words

AIM: Determine the most common words and the most important words in a set of documents

### Read the wiki articles from direcotry then pre-process data
* Read files
* Convert to lower case
* Tokenize the text
* Retain alphabetic words: alpha_only
* Remove all stop words: no_stops

### Creating a corpus with gensim
* Create a Dictionary from the articles
* Create a Corpus

### Gensim bag-of-words
* Use the gensim corpus and dictionary to see the most common terms in the 5th document
* Use the gensim corpus and dictionary to see the most common terms in all documents. 

### Determine the most important words in each document in the corpus using TF-IDF


The directory structure: 

```
├── README.md          
├── data
    ├── Wikipedia articles
        ├──
        ├──
├── notebooks
    ├── NLP_Gensim_most_common_and_most_important_words.ipynb
├── src
    ├── utility.py        
├── requirements.txt   

```
