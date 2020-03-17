#coding: utf-8
#ici, j'importe csv, le module spacy et counter pour compter les fréquences
import csv, spacy
from collections import Counter
#j'identifie ensuite mon fichier sous le nom martino
martino = "martino.csv"
#ici je lis mon fichier
f = open(martino)
articles = csv.reader(f)
next(articles)
#j'installe mon modèle qui permet d'analyse le français
tal = spacy.load("fr_core_news_md")
#ici, je crée deux listes que je vais utiliser plus tard compter les lignes de mon fichier
tousMots = []
bigrams = []
#j'ouvre ensuite ma bouche principale
for article in articles:
    # print(article)
    doc = tal(article[3]) #il y a 4 éléments dans ma liste, et je veux le dernier élément (texte) donc je mets le #3
    # for token in doc:
        # print(token.text)
    lemmes = [token.lemma_ for token in doc] #je lemmatise mon texte
    # print(lemmes)
    # print(len(lemmes))

    mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False and token.text == "islam" and token.text == "muslim"] #ici, j'enlève les mots vides (token.is_stop), j'enlève la ponctuation (token.is_punct) et je garde tous les mots contenant "islam" et "muslim" (token.text)
    # print(mots)
    # print(len(mots))

    for mot in mots:
        tousMots.append(mot) #ceci est ma grande liste avec tous les mots résultants de la boucle
        # print(tousMots)

    for x, y in enumerate(mots[:-1]): 
        bigrams.append("{} {}".format(mots[x],mots[x+1])) #avec ça, je peux faire des paires de mots, afin de voir plus tard quelle paire de mots est la plus utilisée dans les textes
    # print(bigrams)

freq = Counter(bigrams) 
print(freq.most_common(50)) #je peux finalement obtenir les cinquantes paires de mots les plus utilisées dans les textes de Richard Martineau.

#Malheureusement, ça ne fonctionne pas. Je sais que c'est au niveau de la ligne 26 que ça bloque, mais je ne sais pas comment régler le problème, même si je cherche sur internet. Je ne suis pas certaine que "token.text == "muslim" " est la bonne formule. Par contre, je ne saurais pas comment cibler ces deux mots autrement avec spacy. 