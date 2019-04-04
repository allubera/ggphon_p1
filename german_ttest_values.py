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

import random 
lex = {}
sublex = {}
'''
#comment in for fem values ; change append
with open('real_Gerlex_Femfreq.txt') as f:
	for line in f:
		tok = line.split()
		lex[tok[1]] =  tok[0]
'''
'''

#comment in for masc values ; change append
with open('real_Gerlex_Mascfreq.txt') as f:
	for line in f:
		tok = line.split()
		lex[tok[1]] =  tok[0]
'''
'''
#comment in for neut values ; change append
with open('real_Gerlex_Neutfreq.txt') as f:
	for line in f:
		tok = line.split()
		lex[tok[1]] =  tok[0]
'''

#Comment in for fake values. Double check append status
with open('real_German_lexfreq.txt') as f:
	for line in f:
		tok = line.split()
		lex[tok[0]] = tok[1]


lex = {k:float(v) for k, v in lex.items()}
#Getting randomized value 
keys = list(lex.keys())
random.shuffle(keys)
keys = keys[:2500]

for key in keys:
    if key not in sublex:
        sublex[key] = lex[key]
    else:
        sublex[key] += lex[key]

u_lex = sublex.copy()
b_lex = sublex.copy()
t_lex = sublex.copy()

#unigrams 
iterkeys = list(u_lex.keys())	
for oldkey in iterkeys:
	newkey = oldkey[:1]
	if newkey not in u_lex:
		u_lex[newkey] = u_lex[oldkey]
	else:
		u_lex[newkey] += u_lex[oldkey]
	del u_lex[oldkey]
	
#bigrams
iterkeys = list(b_lex.keys())	
for oldkey in iterkeys:
	newkey = oldkey[:2]
	if newkey not in b_lex:
		b_lex[newkey] = b_lex[oldkey]
	else:
		b_lex[newkey] += b_lex[oldkey]
	del b_lex[oldkey]


#trigrams
iterkeys = list(t_lex.keys())	
for oldkey in iterkeys:
	newkey = oldkey[:3]
	if newkey not in t_lex:
		t_lex[newkey] = t_lex[oldkey]
	else:
		t_lex[newkey] += t_lex[oldkey]
	del t_lex[oldkey]
	
print(len(u_lex))
print(len(b_lex))
print(len(t_lex))
print(eta(u_lex))
print(eta(b_lex))
print(eta(t_lex))

#final segment analysis#
u_fin = sublex.copy()
b_fin = sublex.copy()
t_fin = sublex.copy()

#uniphones
iterkeys = list(u_fin.keys())	
for oldkey in iterkeys:
	newkey = oldkey[-1]
	if newkey not in u_fin:
		u_fin[newkey] = u_fin[oldkey]
	else:
		u_fin[newkey] += u_fin[oldkey]
	del u_fin[oldkey]
	
#biphones
iterkeys = list(b_fin.keys())	
for oldkey in iterkeys:
	newkey = oldkey[-2:]
	if newkey not in b_fin:
		b_fin[newkey] = b_fin[oldkey]
	else:
		b_fin[newkey] += b_fin[oldkey]
	del b_fin[oldkey]


#triphones
iterkeys = list(t_fin.keys())	
for oldkey in iterkeys:
	newkey = oldkey[-3:]
	if newkey not in t_fin:
		t_fin[newkey] = t_fin[oldkey]
	else:
		t_fin[newkey] += t_fin[oldkey]
	del t_fin[oldkey]

print(len(u_fin))
print(len(b_fin))
print(len(t_fin))
print(eta(u_fin))
print(eta(b_fin))
print(eta(t_fin))


x = [len(u_lex), len(b_lex), len(t_lex), eta(u_lex), eta(b_lex), eta(t_lex), len(u_fin), len(b_fin), len(t_fin), eta(u_fin), eta(b_fin), eta(t_fin), 'Fake', 'N']

x = ';'.join([str(x)])

print(x)

with open('Ger_ttest_data', 'a') as file:
	file.write(x + '\n')

print(len(sublex))

#bash code: for n in {1..2000}; do python german_ttest_values.py; done
