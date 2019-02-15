with open('real_FRlex_Fem.txt') as f:
    lex = f.read().splitlines()

#to find average word length 
# x = []
#for item in lex:
	#value = len(item)
	#if value:
		#x.append(value)
#y = sum(x)/len(x)
#print(y)
	
unarylex = []
bigramlex = []
trigramlex = []
quadgramlex = []
pentgramlex = []

for item in lex: 
	word = item[0:1]
	if word:
		unarylex.append(word)	

for item in lex: 
	word = item[0:2]
	if word:
		bigramlex.append(word)	
		
for item in lex: 
	word = item[0:3]
	if word:
		trigramlex.append(word)	
		
for item in lex: 
	word = item[0:4]
	if word:
		quadgramlex.append(word)	

for item in lex: 
	word = item[0:5]
	if word:
		pentgramlex.append(word)	

len(unarylex)
len(bigramlex)
len(trigramlex)
len(quadgramlex)
len(pentgramlex)

from collections import Counter

#print(Counter(unarylex))
#print(Counter(bigramlex))
#print(Counter(trigramlex))
#print(Counter(quadgramlex))

unarylen = Counter(unarylex)
bigramlen = Counter(bigramlex)
trigramlen = Counter(trigramlex )
quadgramlen = Counter(quadgramlex)
pentgramlen = Counter(pentgramlex) ### all words unique 

print("The values for the real fem French lexicon are...")
print(len(unarylen))
print(len(bigramlen))
print(len(trigramlen))
print(len(quadgramlen))
print(len(pentgramlen))

#starting backwards strings




###writing out to a file#####
#with open('your_file.txt', 'w') as f:
  #  for item in my_list:
    #    f.write("%s\n" % item)

#creating a trie from file 
#from lexpy.trie import Trie
#trie.add_all('C:/Users/amber/Desktop/prelim_corpora/realFRlex_Masc.txt')
#or 
#rom lexpy.utils import build_trie_from_file
#trie = build_trie_from_file('C:/Users/amber/Desktop/prelim_corpora/realFRlex_Masc.txt')

#len(trie) #number of nodes in trie 

#daw.add_all


#entropy code
import math
from collections import Counter

def eta(data, unit='natural'):
    base = {
        'shannon' : 2.,
        'natural' : math.exp(1),
        'hartley' : 10.
    }

    if len(data) <= 1:
        return 0

    counts = Counter()

    for d in data:
        counts[d] += 1

    ent = 0

    probs = [float(c) / len(data) for c in counts.values()]
    for p in probs:
        if p > 0.:
            ent -= p * math.log(p, base[unit])

    return ent
	
print(eta(unarylex))
print(eta(bigramlex))
print(eta(trigramlex))
print(eta(quadgramlex))
print(eta(pentgramlex))


def rever(strings):
	return [x[::-1] for x in strings]


unaryback = []
bigramback = []
trigramback = []
quadgramback = []
pentgramback = []

backlex = [x[::-1] for x in lex][::-1]
for item in backlex: 
	word = item[0:1]
	if word:
		unaryback.append(word)	

for item in backlex: 
	word = item[0:2]
	if word:
		bigramback.append(word)	
		
for item in backlex: 
	word = item[0:3]
	if word:
		trigramback.append(word)	
		
for item in backlex: 
	word = item[0:4]
	if word:
		quadgramback.append(word)	

for item in backlex: 
	word = item[0:5]
	if word:
		pentgramback.append(word)	

len(unaryback)
len(bigramback)
len(trigramback)
len(quadgramback)
len(pentgramback)

from collections import Counter

#print(Counter(unarylex))
#print(Counter(bigramlex))
#print(Counter(trigramlex))
#print(Counter(quadgramlex))

unarybacklen = Counter(unaryback)
bigrambacklen = Counter(bigramback)
trigrambacklen = Counter(trigramback)
quadgrambacklen = Counter(quadgramback)
pentgrambacklen = Counter(pentgramback) ### all words unique 

print("The values for the backwards real fem French lexicon are...")
print(len(unarybacklen))
print(len(bigrambacklen))
print(len(trigrambacklen))
print(len(quadgrambacklen))
print(len(pentgrambacklen))

print(eta(unaryback))
print(eta(bigramback))
print(eta(trigramback))
print(eta(quadgramback))
print(eta(pentgramback))



### thoughts before bed.... now I run the random lexicons a bunch of times and hope that the entropy/ # of options going forwards is increased and the entropy/ # of options going backwards is decreased compared to the random lexicons