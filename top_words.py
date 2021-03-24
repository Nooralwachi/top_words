import re
from collections import defaultdict
import string

def top_words1(file, counter):
	seen = defaultdict(int)
	pattern  = r'\w+'
	exceptions = ['a', 'the','in','of','has','been','is','and','an']
	with open (file, 'r') as file:
		for lines in file:
			lines = re.findall(pattern,lines)
			for word in lines:
			#for word in lines.split():
				#word = word.strip(string.punctuation)
				if word.lower() not in exceptions:
					seen[word.lower()] += 1
	wordlist = sorted(seen.items(), key= lambda x:x[1], reverse= True)
	for x,y in wordlist[:counter]:
		print(x,y)

top_words1('words.txt', 10)	

#####################################################################




#!/usr/bin/python

"""Simple solution.

Assumes each line in the input_file can fit into memory with the set of
distinct words and counts.
"""

import collections
import string
import sys


def segment_line(line):
  return line.split()


def normalise(segment):
  return segment.strip(string.punctuation)


def read_file(file_name):
  with open(file_name) as f:
    for line in f:
      for segment in segment_line(line):
        yield normalise(segment)


input_file = 'words.txt'
stopwords_file = 'exceptions.txt'

stopwords = set(read_file(stopwords_file))

counts = collections.defaultdict(int)

for word in read_file(input_file):
  if word not in stopwords:
    counts[word] += 1

print(" ".join(
    sorted(counts.keys(), key=lambda x: counts[x], reverse=True)[:10]))



#####################################################################

from collections import defaultdict
def replace_punctuation(word):
	symbols = [',', '.', ';', ':','?', '!' ]
	for  x in symbols:
		word = word.replace(x, '')
		#print(word)
	return word

def top_words2(filename):
	words = defaultdict(int)
	excluded = ['the', 'if','it','is', 'a', 'of', 'an', 'and']
	with open(filename, 'r') as file:
		for line in file:
			line = line.strip()
			if line:
				words_list= line.split()
				for item in words_list:
					item =replace_punctuation(item.lower())
					if item not in excluded :
						words[item] +=1
	sorted_words = sorted(words.items(), key = lambda x:x[1], reverse = True)
	print(sorted_words)
	for (item, count) in sorted_words[:10]:
		print(item)

top_words2('words.txt')


#####################################################################



import re
from collections import defaultdict
def common_words(commonfile):
	with open (commonfile, 'r') as file:
		for line in file:
			common.extend(line.split())

def max_count(filename, count):
	word_dict=defaultdict(int)
	#pattern  = '^[a-zA-z]* $[a-zA-z]'
	pattern  = r'\w+'
	with open (filename, 'r') as file:
		for line in file:
			line = line.strip()
			if line :
				words= re.findall(pattern, line)
				for word in words :
					if word.lower() not in common:
						word_dict[word.lower()] +=1
	sorted_words=sorted(word_dict.items(), key = lambda x:x[1], reverse =True)
	for (word,count) in sorted_words[:count]:
		print(word,count)
		#print(sorted_words)

common=[]
common_words('exceptions.txt')
max_count('words.txt', 10)




# exception.txt file contains: 
# a the in of has been is and an

# words.txt file contains:
#1 What is Lorem Ipsum Lorem Ipsum is simply dummy, text of the
# 2 printing and typesetting industry Lorem Ipsum has been the
# 3 industry's Standard dummy text ever since the 1500s when an
# 4 unknown printer took a galley of type and scrambled it to
# 5 make a type 

# 6 what Is lorem Ipsum Lorem ipsum is simply dummy, text of 
# 7 the printing and typesetting industry Lorem Ipsum has 
# 8 been the industry's standard dummy text ever since the 
# 9 1500s when an unknown printer took a galley of type and 
# 10 scrambled it to make a type
# 11 What is lorem, Ipsum Lorem Ipsum is simply dummy text of 
# 12 the What is Lorem Ipsum Lorem Ipsum is simply dummy text 
# 13 of the What is Lorem Ipsum Lorem Ipsum is simply dummy 
# 14 text of the What is Lorem Ipsum Lorem Ipsum is simply 
# 15 dummy, text of the What is Lorem Ipsum Lorem Ipsum is 
# 16 simply dummy text of the What is Lorem Ipsum Lorem 
# 17 Ipsum is simply dummy, text, of, the 