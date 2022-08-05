import spacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Ich heisse Liv. Vertrauen ist gut, Kontrolle ist besser. Das Schiffchen fliegt, der Webstuhl kracht.")


leftRoot = False
auxToken = "ROOT"
leftRootToken = None
for sent in doc.sents:
    for token in sent:
        if token.dep_ == auxToken:
            if (leftRootToken is not None) and \
                    (token.is_space is False) and \
                    (token.is_punct is False):
                leftRoot = True
                break
            auxToken = token.dep_
        leftRootToken = token

leftCj = False
auxToken = "cj"
leftCjToken = None
for sent in doc.sents:
    for token in sent:
        if token.dep_ == auxToken:
            if (leftCjToken is not None) and \
                    (token.is_space is False) and \
                    (token.is_punct is False):
                leftCj = True
                if leftRoot is True and leftCj is True:
                    if leftCjToken.dep_ == leftRootToken.dep_:
                        print(token.sent, leftRootToken)
                        print(token.sent, leftCjToken)
                        break
            auxToken = token.dep_
        leftCjToken = token









