import spacy

nlp = spacy.load("de_core_news_sm")
f = open('Text_Parallelismus.txt', 'r')
content = f.read()
docFaust = nlp(content)


# Articles only count as Anapher tokens if they are used in the same manner, i.e. if they have the same dependency
# For other words we assume that the dependency field is not important => return True
def has_same_dependency(first_tkn, tkn):
    # the lemma_ of "der", "die" or "das" is always "der"
    if tkn.lemma_ == "der":
        if tkn.dep_ == first_tkn.dep_:
            return True
        else:
            return False
    else:
        return True


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
                        has_same_dependency(token, firstToken) and \
                        (token.lower_ == firstToken.lower_) and \
                        (token.lemma_ == firstToken.lemma_) and \
                        token.text is not firstToken.sent and token.text is not token.sent:
                    counter = counter + 1
                    print("0", token.text)
                    print("1", firstToken.sent)
                    print("2", token.sent)
                firstToken = token
            previousToken = token.text
    return counter


result = findAnapher(docFaust)

print("found", result, "anapher")