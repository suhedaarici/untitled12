from __future__ import unicode_literals

from django.db import models

# Create your models here.

import collections
class Category(models.Model):
    name = models.CharField(max_length = 50)

    amount = models.DecimalField(max_digits = 10,decimal_places = 2,default = 0)
filename="dosya.txt"

# WordCount
def WordCount(file):
    wrdcnt=0
    for line in file:
        words=line.split()
        wrdcnt=wrdcnt+len(words)
    return wrdcnt
file=open(filename,"r")
print("Number of words in %s is %d" % (filename, WordCount(file)))

#WordFrequency
file=open(filename,"r")
wordcountfrequency={}
for word in file.read().split():
    if word not in wordcountfrequency:
        wordcountfrequency[word] = 1
    else:
        wordcountfrequency[word] += 1
for a,b in wordcountfrequency.items():
    print (a,b)