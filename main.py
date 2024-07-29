from text_extraction import *
from cosine import *
import os

import os
file_name = "invoice1.pdf" #test file name from the test folder

#---------getting all the files from the train directory----------
files = os.listdir("./train")
db = {}
#--------calculate cosine similarity with all the train files-------
for trainfile in files:
    db[trainfile] = cosinesim(pdfextract("./test/"+file_name),pdfextract("./train/"+trainfile))

best_match = max(db.values()) #best match is the highest cosine similarity value in the hash map

#------find the key of the value---------
for keys in db:
    if db[keys]==best_match:
        output = keys
#------if cosine similarity is < 0.2 then no match----------
if best_match>0.2:
    print(file_name+" matches with "+keys+" with a Cosine similarity of "+ str(best_match))
else:
    print("Nothing Matches with "+keys+", with " + file_name+" having the largest Cosine similarity of "+str(best_match))



