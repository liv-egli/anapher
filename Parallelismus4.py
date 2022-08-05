import spacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Vertrauen ist gut, Kontrolle ist besser. Das Schiffchen fliegt, der Webstuhl kracht.")

def leftCj():
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
                auxToken = token.dep_
            leftCjToken = token
    if leftCj is True:
        return True
    else:
        return False

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
                if leftRoot is True and leftCj() is True:
                    if leftCjToken.dep_ == leftRootToken.dep_:
                        print(token.sent, leftRootToken, leftCjToken)
                    break
            auxToken = token.dep_
        leftRootToken = token









