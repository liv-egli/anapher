import spacy

nlp = spacy.load("de_core_news_sm")
f = open('Raeuber.txt', 'r')
content = f.read()
doc = nlp(content)


rightRoot = False
depTokenR = None
auxRootToken = None
testR = None
rightRootToken = None
rightCj = False
depTokenC = None
auxCjToken = None
testC = None
rightCjToken = None
leftRoot = False
leftRootToken = None
auxTokenR = "ROOT"
leftDepTokenR = None
leftCj = False
auxTokenC = "cj"
leftDepTokenC = None
leftCjToken = None
for sent in doc.sents:
    for token in sent:
        if auxRootToken is not None:
            if depTokenR == "ROOT":
                rightRoot = True
                rightRootToken = token
                testR = auxRootToken
            depTokenR = token.dep_
        auxRootToken = token

        if auxCjToken is not None:
            if depTokenC == "cj":
                rightCj = True
                rightCjToken = token
                testC = auxCjToken
            depTokenC = token.dep_
        auxCjToken = token

        if token.dep_ == auxTokenR:
            if (leftDepTokenR is not None) and \
                    (token.is_space is False) and \
                    (token.is_punct is False):
                leftRoot = True
                leftRootToken = leftDepTokenR
            auxTokenR = token.dep_
        leftDepTokenR = token

        if token.dep_ == auxTokenC:
            if (leftDepTokenC is not None) and \
                    (token.is_space is False) and \
                    (token.is_punct is False):
                leftCj = True
                leftCjToken = leftDepTokenC
            auxTokenC = token.dep_
        leftDepTokenC = token


    if leftRoot is True and leftCj is True:
        if rightCj is True and rightRoot is True:
            if leftDepTokenC.dep_ == leftDepTokenR.dep_:
                if rightCjToken.dep_ == rightRootToken.dep_:
                    if testR.pos_ == testC.pos_:
                        print(leftDepTokenC.sent)
                        print(leftRootToken.dep_, testR.pos_, rightRootToken.dep_, leftCjToken.dep_, testC.pos_, rightCjToken.dep_)








# if rightCj is True and rightRoot is True:
#     if auxRootToken.pos_ == auxCjToken.pos_:
#         if rightCjToken.dep_ == rightRootToken.dep_:
#             print(rightCjToken.sent, rightCjToken, rightRootToken)

# if leftRoot is True and leftCj is True:
#     if leftCjToken.dep_ == leftRootToken.dep_:
#         if auxRootToken.pos_ == auxCjToken.pos_:
#             print(leftCjToken.sent, leftCjToken, leftRootToken)







