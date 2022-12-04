import spacy

nlp = spacy.load("de_core_news_sm")
doc = nlp("Die Kunst ist lang, kurz ist das Leben.")

# nlp = spacy.load("de_core_news_sm")
# f = open("Faust.txt", "r")
# content = f.read()
# doc = nlp(content)

# for sent_i, sent in enumerate(doc.sents):
#     for token in sent:
#         print("\n", token.i, "(token.i)", token.text, "(token.text)", "\n", "---", "\n", sent.text, "(sent.text)", sent.start, "(sent.start)", sent.end, "(sent.end)", "---", sent.end - token.i, len(sent))


for token in doc:
    print(token.text, token.dep_, token.pos_)
    print(len(token))

#
# for sent_i, sent in enumerate(doc.sents):
#     for token in sent:
#         print(sent_i, token.i, token.text)