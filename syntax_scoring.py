import numpy as np

with open('../data/syntax_scoring') as f:
    lines = f.read().splitlines()

open_chars = ['(','[','{','<']
close_chars = [')',']','}','>']

pair_dict = dict(zip(close_chars+open_chars,open_chars+close_chars)) # Create two way map, searching '(' yields ')' and vice versa
error_score_dict = dict(zip(close_chars,[3,57,1197,25137]))
incomplete_score_dict = dict(zip(close_chars,[1,2,3,4]))
error_score = 0
incomplete_scores = []
for line in lines:
    exceptions = []
    buffer = []
    for char in line:
        if char in open_chars:
            buffer += char
        if char in close_chars:
            if pair_dict[char]!=buffer[-1]:
                exceptions+=[char]
            buffer = buffer[:-1]
    if exceptions:
        error_score += error_score_dict[exceptions[0]]
        continue
    score = 0
    # Close last opening character first, then second, and so on
    for char in buffer[::-1]:
        score *= 5
        score += incomplete_score_dict[pair_dict[char]]
    incomplete_scores += [score]
        
print(error_score)

incomplete_scores = sorted(incomplete_scores)
print(incomplete_scores[len(incomplete_scores)//2])
