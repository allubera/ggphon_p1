import sys 

lex = {}
typelex = {}
tokenlex = {}
'''
#Use for fake lexicons -- edit out other file opening#
import random 

with open('real_German_lexfreq.txt') as f:
	for line in f:
		tok = line.split()
		lex[tok[0]] = tok[1]
		

#Values for German: Fem = 8452 obs ; Masc = 6603 obs ; Neut = 3392 obs
import random
keys = list(lex.keys())
random.shuffle(keys)
#keys = keys[:8452]
#keys = keys[:6603]
keys = keys[:3392]

for key in keys:
	if key not in tokenlex:
		tokenlex[key] = lex[key]
	else:
		tokenlex[key] += lex[key]
		
typelex = {key: 1 for key in tokenlex}
'''

print("Type Analysis\n")
'''
with open('real_Gerlex_Fem.txt') as f:
	for line in f:
		tok = line.split()
		typelex[tok[0]] = 1
'''
'''
with open('real_Gerlex_Masc.txt') as f:
	for line in f:
		tok = line.split()
		typelex[tok[0]] = 1
'''
with open('real_Gerlex_Neut.txt') as f:
	for line in f:
		tok = line.split()
		typelex[tok[0]] = 1



#entropy code
import math

def eta(data, unit='natural'):
    base = {
        'shannon' : 2.,
        'natural' : math.exp(1),
        'hartley' : 10.
    }

    if len(data) <= 1:
        return 0
    ent = 0
    probs = [float(c) / sum(data.values()) for c in data.values()]
    for p in probs:
        if p > 0.:
            ent -= p * math.log(p, base[unit])

    return ent
	
unarytypelex = typelex.copy()
bigramtypelex = typelex.copy()
trigramtypelex = typelex.copy()

typelex = {k:float(v) for k, v in typelex.items()}

#unigrams 
iterkeys = list(unarytypelex.keys())	
for oldkey in iterkeys:
	newkey = oldkey[:1]
	if newkey not in unarytypelex:
		unarytypelex[newkey] = unarytypelex[oldkey]
	else:
		unarytypelex[newkey] += unarytypelex[oldkey]
	del unarytypelex[oldkey]
	
#bigrams
iterkeys = list(bigramtypelex.keys())	
for oldkey in iterkeys:
	newkey = oldkey[:2]
	if newkey not in bigramtypelex:
		bigramtypelex[newkey] = bigramtypelex[oldkey]
	else:
		bigramtypelex[newkey] += bigramtypelex[oldkey]
	del bigramtypelex[oldkey]


#trigrams
iterkeys = list(trigramtypelex.keys())	

for oldkey in iterkeys:
	newkey = oldkey[:3]
	if newkey not in trigramtypelex:
		trigramtypelex[newkey] = trigramtypelex[oldkey]
	else:
		trigramtypelex[newkey] += trigramtypelex[oldkey]
	del trigramtypelex[oldkey]


#print("The values for the real fem German lexicon are...")
#print("The values for the real masc German lexicon are...")
print("The values for the real neut German lexicon are...")
#print("The values for the fake fem German lexicon are...")
#print("The values for the fake masc German lexicon are...")
#print("The values for the fake neut German lexicon are...")

print(len(unarytypelex))
print(len(bigramtypelex))
print(len(trigramtypelex))
print(eta(unarytypelex))
print(eta(bigramtypelex))
print(eta(trigramtypelex))


####start analysis of final segments####

unarytypefinal = typelex.copy()
bigramtypefinal = typelex.copy()
trigramtypefinal = typelex.copy()

typelex = {k:int(v) for k, v in typelex.items()}

#unigrams 
iterkeys = list(unarytypefinal.keys())	
for oldkey in iterkeys:
	newkey = oldkey[-1]
	if newkey not in unarytypefinal:
		unarytypefinal[newkey] = unarytypefinal[oldkey]
	else:
		unarytypefinal[newkey] += unarytypefinal[oldkey]
	del unarytypefinal[oldkey]
	
#bigrams
iterkeys = list(bigramtypefinal.keys())	
for oldkey in iterkeys:
	newkey = oldkey[-2:]
	if newkey not in bigramtypefinal:
		bigramtypefinal[newkey] = bigramtypefinal[oldkey]
	else:
		bigramtypefinal[newkey] += bigramtypefinal[oldkey]
	del bigramtypefinal[oldkey]

#trigrams
iterkeys = list(trigramtypefinal.keys())	

for oldkey in iterkeys:
	newkey = oldkey[-3:]
	if newkey not in trigramtypefinal:
		trigramtypefinal[newkey] = trigramtypefinal[oldkey]
	else:
		trigramtypefinal[newkey] += trigramtypefinal[oldkey]
	del trigramtypefinal[oldkey]


#print("The values for the final segments in real fem German lexicon are...")
#print("The values for the final segments in real masc German lexicon are...")
print("The values for the final segments in real neut German lexicon are...")
#print("The values for the final segments in fake fem German lexicon are...")
#print("The values for the final segments in fake masc German lexicon are...")
#print("The values for the final segments infake neut German lexicon are...")

print(len(unarytypefinal))
print(len(bigramtypefinal))
print(len(trigramtypefinal))
print(eta(unarytypefinal))
print(eta(bigramtypefinal))
print(eta(trigramtypefinal))

print("\n")
print("Token analysis\n")
'''
with open('real_Gerlex_Femfreq.txt') as f:
	for line in f:
		tok = line.split()
		tokenlex[tok[1]] =  tok[0]
'''
'''
with open('real_Gerlex_Mascfreq.txt') as f:
	for line in f:
		tok = line.split()
		tokenlex[tok[1]] =  tok[0]
'''

with open('real_Gerlex_Neutfreq.txt') as f:
	for line in f:
		tok = line.split()
		tokenlex[tok[1]] =  tok[0]



tokenlex = {k:float(v) for k, v in tokenlex.items()}

unarytokenlex = tokenlex.copy()
bigramtokenlex = tokenlex.copy()
trigramtokenlex = tokenlex.copy()

#unigrams 
iterkeys = list(unarytokenlex.keys())	
for oldkey in iterkeys:
	newkey = oldkey[:1]
	if newkey not in unarytokenlex:
		unarytokenlex[newkey] = unarytokenlex[oldkey]
	else:
		unarytokenlex[newkey] += unarytokenlex[oldkey]
	del unarytokenlex[oldkey]
	
#bigrams
iterkeys = list(bigramtokenlex.keys())	
for oldkey in iterkeys:
	newkey = oldkey[:2]
	if newkey not in bigramtokenlex:
		bigramtokenlex[newkey] = bigramtokenlex[oldkey]
	else:
		bigramtokenlex[newkey] += bigramtokenlex[oldkey]
	del bigramtokenlex[oldkey]


#trigrams
iterkeys = list(trigramtokenlex.keys())	

for oldkey in iterkeys:
	newkey = oldkey[:3]
	if newkey not in trigramtokenlex:
		trigramtokenlex[newkey] = trigramtokenlex[oldkey]
	else:
		trigramtokenlex[newkey] += trigramtokenlex[oldkey]
	del trigramtokenlex[oldkey]

#print("The values for initial segments in the fem German lexicon are...")
#print("The values for initial segments in the real masc German lexicon are...")
print("The values for initial segments in the real neut German lexicon are...")
#print("The values for initial segments in the fake fem German lexicon are...")
#print("The values for initial segments in the fake masc German lexicon are...")
#print("The values for initial segments in the fake neut German lexicon are...")

print(len(unarytokenlex))
print(len(bigramtokenlex))
print(len(trigramtokenlex))
print(eta(unarytokenlex))
print(eta(bigramtokenlex))
print(eta(trigramtokenlex))


#final segment analysis#
unarytokenfinal = tokenlex.copy()
bigramtokenfinal = tokenlex.copy()
trigramtokenfinal = tokenlex.copy()

#final unary
iterkeys = list(unarytokenfinal.keys())	
for oldkey in iterkeys:
	newkey = oldkey[-1]
	if newkey not in unarytokenfinal:
		unarytokenfinal[newkey] = unarytokenfinal[oldkey]
	else:
		unarytokenfinal[newkey] += unarytokenfinal[oldkey]
	del unarytokenfinal[oldkey]
	
#final bigrams
iterkeys = list(bigramtokenfinal.keys())	
for oldkey in iterkeys:
	newkey = oldkey[-2:]
	if newkey not in bigramtokenfinal:
		bigramtokenfinal[newkey] = bigramtokenfinal[oldkey]
	else:
		bigramtokenfinal[newkey] += bigramtokenfinal[oldkey]
	del bigramtokenfinal[oldkey]

#final trigrams
iterkeys = list(trigramtokenfinal.keys())	

for oldkey in iterkeys:
	newkey = oldkey[-3:]
	if newkey not in trigramtokenfinal:
		trigramtokenfinal[newkey] = trigramtokenfinal[oldkey]
	else:
		trigramtokenfinal[newkey] += trigramtokenfinal[oldkey]
	del trigramtokenfinal[oldkey]

#print("The values for the final segments in the real fem German lexicon are...")
#print("The values for the final segments in the real masc German lexicon are...")
print("The values for the final segments in the real neut German lexicon are...")
#print("The values for  the final segments in the fake fem German lexicon are...")
#print("The values for the final segments in the fake masc German lexicon are...")
#print("The values for  the final segments in the fake neut German lexicon are...")

print(len(unarytokenfinal))
print(len(bigramtokenfinal))
print(len(trigramtokenfinal))
print(eta(unarytokenfinal))
print(eta(bigramtokenfinal))
print(eta(trigramtokenfinal))


x = [len(unarytypelex), len(bigramtypelex), len(trigramtypelex), eta(unarytypelex), eta(bigramtypelex), eta(trigramtypelex), len(unarytypefinal), len(bigramtypefinal), len(trigramtypefinal), eta(unarytypefinal), eta(bigramtypefinal), eta(trigramtypefinal), len(unarytokenlex), len(bigramtokenlex), len(trigramtokenlex), eta(unarytokenlex), eta(bigramtokenlex), eta(trigramtokenlex), len(unarytokenfinal), len(bigramtokenfinal), len(trigramtokenfinal), eta(unarytokenfinal), eta(bigramtokenfinal), eta(trigramtokenfinal)]
x = ';'.join([str(x)])
print(x)
'''
with open('german_fake_neut_values.txt', 'a') as file:
	file.write(x + '\n')

#bash code: for n in {1..2000}; do python german_entropy_values.py; done
'''

