from collections import Counter

with open('../data/extended_polymerization') as f:
    template = f.readline().strip()
    f.readline()
    lines = f.read().splitlines()
    pair_insertion_rules = [line.split(' -> ') for line in lines]

element_counts = dict.fromkeys(set(''.join([''.join(i) for i in pair_insertion_rules])),0)
rules ={}
pair_counts = {}
for rule in pair_insertion_rules:
    rules[rule[0]] = [rule[0][0]+rule[1],rule[1]+rule[0][1]]
    pair_counts[rule[0]] = 0
      
for element in template:
    element_counts[element]+=1

# Initialize dict from template
for i in range(len(template)-1):
    pairs = rules[template[i:i+2]]
    for pair in pairs:
        pair_counts[pair] += 1
    element_counts[pairs[0][1]] +=1
   
# Continue expanding polymer
# STEP 1
#num_steps = 10 - 1
# STEP 2
num_steps = 40 - 1 #first step already completed above
for i in range(num_steps):
    new_pair_counts = pair_counts.copy()
    for key, val in pair_counts.items():
        new_pair_counts[key] -= val #remove pairs that split and become two new unique pairs
        pairs = rules[key]
        for pair in pairs:
            new_pair_counts[pair] += val # 
        element_counts[pairs[0][1]] += val
    pair_counts = new_pair_counts
    
max_value = max(element_counts.values())
min_value = min(element_counts.values())
print(max_value-min_value)