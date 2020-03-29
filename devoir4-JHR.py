#coding: utf-8

### MERCI ALEXANDRA! VOICI QUELQUES COMMENTAIRES SUR TON SCRIPT, TOUJOURS EN MAJ. PRÉCÉDÉS DE 3#

#ici, j'importe csv, le module spacy et counter pour compter les fréquences
import csv, spacy
from collections import Counter
#j'identifie ensuite mon fichier sous le nom martino
# martino = "martino.csv"
martino = "../martino.csv" ### JE CHANGE LE CHEMIN POUR QUE ÇA MARCHE SUR MON ORDI.
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
    print(article[1]) ### J'IMPRIME LA DATE 
    doc = tal(article[3]) #il y a 4 éléments dans ma liste, et je veux le dernier élément (texte) donc je mets le #3 ### EXCELLENT
    # for token in doc:
        # print(token.text)
    # lemmes = [token.lemma_ for token in doc] #je lemmatise mon texte ### C'EST BIEN, MAIS TU LE FAIS AUSSI DANS TON BLOC DE CODE QUI SUIT
    # print(lemmes)
    # print(len(lemmes))

    # mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False and token.text == "islam" and token.text == "muslim"] #ici, j'enlève les mots vides (token.is_stop), j'enlève la ponctuation (token.is_punct) et je garde tous les mots contenant "islam" et "muslim" (token.text)
    ### TON APPROCHE EST INTÉRESSANTE; POUR QU'ELLE FONCTIONNE, IL AURAIT FALLU LA MODIFIER AINSI:
    # mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False and ("islam" in token.lemma_ or "musulm" in token.lemma_)] ### LA DIFFÉRENCE EST QUE CE CODE TIENT DEMANDE SI LA CHAÎNE DE CARACTÈRE «ISLAM*» OU «MUSULM*» EST INCLUSE DANS LE MOT LEMMATISÉ, ALORS QUE TON CODE DEMANDAIT SI CE MOT ÉTAIT ABSOLUMENT «ISLAM» OU «MUSLIM» (POURQUOI «MUSLIM», D'AILLEURS?)
    ### MAIS CETTE APPROCHE FAIT EN SORTE QUE TU PERDS TOUS LES MOTS QUI VIENNENT AVANT OU APRÈS «ISLAM» OU «MUSULM»; IL EST IMPORTANT DE LES CONSERVER (ON FERA LE TRI APRÈS), DONC, ON VA PLUTÔT ÉCRIRE CE CODE:
    mots = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    # print(mots)
    print(len(mots))

    for mot in mots:
        tousMots.append(mot) #ceci est ma grande liste avec tous les mots résultants de la boucle
        # print(tousMots)

    for x, y in enumerate(mots[:-1]):
        ### C'EST ICI QU'ON PEUT FAIRE LE TRI ET NE CONSERVER QUE LES MOTS QUI CONTIENNENT "ISLAM" OU "MUSULM"
        if "islam" in mots[x] or "musulm" in mots[x]:
            bigrams.append("{} {}".format(mots[x],mots[x+1])) #avec ça, je peux faire des paires de mots, afin de voir plus tard quelle paire de mots est la plus utilisée dans les textes ### TON CODE ÉTAIT BON; IL NE MANQUAIT QUE LA CONDITION DE LA LIGNE PRÉCÉDENTE
    # print(bigrams)
    print(len(bigrams)) ### SIMPLE AFFICHAGE POUR SAVOIR OÙ ON EST RENDU
    print("🌈"*40) ### PETIT SÉPARATEUR DANS L'AIR DU TEMPS

freq = Counter(bigrams) 
print(freq.most_common(50)) #je peux finalement obtenir les cinquantes paires de mots les plus utilisées dans les textes de Richard Martineau.

#Malheureusement, ça ne fonctionne pas. Je sais que c'est au niveau de la ligne 26 que ça bloque, mais je ne sais pas comment régler le problème, même si je cherche sur internet. Je ne suis pas certaine que "token.text == "muslim" " est la bonne formule. Par contre, je ne saurais pas comment cibler ces deux mots autrement avec spacy. 
### EN ESPÉRANT QUE MES COMMENTAIRES AUX LIGNES 43 ET 45 AIENT PU T'AIDER À COMPRENDRE CE QUI SE PASSAIT :)