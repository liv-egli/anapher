import spacy

nlp = spacy.load("de_core_news_sm")
f = open('Faust.txt', 'r')
content = f.read()
doc = nlp(content)

counter = 0
rightRoot = False
rightDepTokenR = None
auxRootToken = None
finalAuxRoot = None
rightRootToken = None
rightCj = False
rightDepTokenC = None
auxCjToken = None
finalAuxCj = None
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
            if rightDepTokenR == "ROOT":
                rightRoot = True
                rightRootToken = token
                finalAuxRoot = auxRootToken
            rightDepTokenR = token.dep_
        auxRootToken = token

        if auxCjToken is not None:
            if rightDepTokenC == "cj":
                rightCj = True
                rightCjToken = token
                finalAuxCj = auxCjToken
            rightDepTokenC = token.dep_
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
            if leftCjToken.dep_ == leftRootToken.dep_:
                if rightCjToken.dep_ == rightRootToken.dep_:
                    if finalAuxRoot.pos_ == finalAuxCj.pos_:
                        if finalAuxRoot.dep_ == "ROOT":
                            if finalAuxCj.dep_ == "cj":
                                if rightRootToken.sent == leftCjToken.sent:
                                    counter = counter + 1
                                    print("0", rightRootToken.sent)
                                    print("1", leftRootToken.dep_, finalAuxRoot.pos_, rightRootToken.dep_, leftCjToken.dep_, finalAuxCj.pos_, rightCjToken.dep_)
                                    print("2", leftRootToken, finalAuxRoot, rightRootToken, leftCjToken, finalAuxCj, rightCjToken)

print("found", counter, "parallelismus")

# if rightCj is True and rightRoot is True:
#     if auxRootToken.pos_ == auxCjToken.pos_:
#         if rightCjToken.dep_ == rightRootToken.dep_:
#             print(rightCjToken.sent, rightCjToken, rightRootToken)

# if leftRoot is True and leftCj is True:
#     if leftCjToken.dep_ == leftRootToken.dep_:
#         if auxRootToken.pos_ == auxCjToken.pos_:
#             print(leftCjToken.sent, leftCjToken, leftRootToken)

# if leftRootToken.dep_ != "punct" and rightRootToken.dep_ != "punct":





