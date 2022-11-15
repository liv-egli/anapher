import spacy

nlp = spacy.load("de_core_news_sm")
f = open("Raeuber.txt", "r")
content = f.read()
docFaust = nlp(content)


# Artikel zählen nur als Anapher wenn sie auf die gleiche Art und Weise gebraucht werden, also die gleiche Dependency haben.
# für alle anderen Wörter spielt die Abhängikeit keine Rolle => return True
def has_same_dependency(first_tkn, tkn):
    # das Lemma von "der", "die" or "das" ist immer "der"
    if tkn.lemma_ == "der":
        if tkn.dep_ == first_tkn.dep_:
            return True
        else:
            return False
    else:
        return True


def findAnapher(doc):
    # Funktion gibt die in jedem Dokument vorhandenen Anapher zurück
    counter = 0
    # previousToken = "."
    # das erste Wort in einem Dokument soll als Satzanfang beachtet werden, weshalb das vorherige ein Satzzeichen sein muss.
    firstToken = None
    for token in doc:
        # folgende Anweisungen werden für jedes Token im Dokument durchgeführt
        if token.is_space is False:
            # Leerschläge und Umschläge sollen nicht beachtet werden
            if token.is_sent_start:
                # nur wenn das previousToken ein Satzzeichen ist, wird das folgende Wort zum firstToken
                if (firstToken is not None) and \
                        (token.is_space is False) and \
                        (firstToken.is_space is False) and \
                        (token.is_punct is False) and \
                        (firstToken.is_punct is False) and \
                        has_same_dependency(token, firstToken) and \
                        (token.lower_ == firstToken.lower_) and \
                        (token.lemma_ == firstToken.lemma_) and \
                        token.text is not firstToken.sent and token.text is not token.sent:
                    # Leerschläge und Satzzeichen sollen nicht beachtet werden
                    # die zuvor erstellte Funktion wird hier ins Programm eingebaut
                    # zwei aufeinanderfolgende Token nach einem Satzzeichen sollen in der Grundform und ohne Beachtung der Gross- und Kleinschreibung miteinander verglichen werden.
                    counter = counter + 1
                    print("0", token.text)
                    print("1", firstToken.sent)
                    print("2", token.sent)
                firstToken = token
                # das Satzanfang-Token wird immer zum firstToken, um mit dem nächsten Satzanfang-Token verglichen werden zu können
    return counter


result = findAnapher(docFaust)

print("found", result, "anapher")