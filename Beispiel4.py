import spacy

nlp = spacy.load("de_core_news_sm")
f = open('Text_Anapher.txt', 'r')
content = f.read()
docFaust = nlp(content)


def findAnapher(doc):
    counter = 0
    previousToken = "."
    firstToken = None
    for token in doc:
        if token.is_space is False:
            if previousToken == ',' or previousToken == ';' or previousToken == ':' or previousToken == '.' or previousToken == '!' or previousToken == '?' or previousToken == "_":
                if (firstToken is not None) and \
                        (token.is_space is False) and \
                        (firstToken.is_space is False) and \
                        (token.is_punct is False) and \
                        (firstToken.is_punct is False) and \
                        (token.dep_ == firstToken.dep_) and \
                        (token.lower_ == firstToken.lower_) and \
                        (token.lemma_ == firstToken.lemma_):
                    counter = counter + 1
                    print("0", token.text)
                    print("1", firstToken.sent)
                    print("2", token.sent)
                firstToken = token
            previousToken = token.text
    return counter


result = findAnapher(docFaust)

print("found", result, "anapher")
