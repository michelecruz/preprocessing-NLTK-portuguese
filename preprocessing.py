import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import RSLPStemmer
from unidecode import unidecode

def pre_processing(text):

    ptstopwords = nltk.corpus.stopwords.words("portuguese")
    #print("\n STOP WORDS:",ptstopwords)
    stemmer = nltk.stem.RSLPStemmer()
    filtered_text = [t.lower() for t in text] # deixa o texto em minúsculo
    filtered_text = [t for t in filtered_text if not t in ptstopwords] # remove as stopwords do texto
    filtered_text = [str(stemmer.stem(t)) for t in filtered_text] # aplica o processo de stemming no texto
    return filtered_text
 
text = """Brasil!
Mostra tua cara
Quero ver quem paga
Pra gente ficar assim
Brasil!
Qual é o teu negócio?
O nome do teu sócio?
Confia em mim"""
tokenizer = RegexpTokenizer(r'\w+') #remove os caracteres especiais
result = tokenizer.tokenize(unidecode(text)) # remove os acentos
print(pre_processing(result))

