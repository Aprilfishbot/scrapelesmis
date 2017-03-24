import nltk
import codecs
import xlwt

from nltk.tag import pos_tag

# have to use codecs to open the file because it's encoded in utf
f = codecs.open("C:/Users/Florence/135-0.txt", 'r', 'utf-8-sig')
# nltk.download()
# f= open("C:/Users/Florence/135-0.txt", "rU")
raw = f.read()
tokens = nltk.word_tokenize(raw)
lm = nltk.Text(tokens)
lm_tagged = pos_tag(lm)

tags = [ 'CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT',
         'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO',
         'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']

wb = xlwt.Workbook()


for t in tags:
    fd = nltk.FreqDist(word.lower() for (word, tag) in lm_tagged if (tag == t and word[0] <> '_'))
    ws = wb.add_sheet(t)
    for num, name in enumerate(fd.most_common(3000), start=0):
        ws.write(num, 0, name[0])

wb.save("C:/Users/Florence/Documents/Dropbox/lmwordslmwords_v5.xls")
