import itertools
import functools

p1_pos, p2_pos = 3,7
die_val = 1
p1_score, p2_score = 0,0


# PART 1

die_rolls = [sum(range(i,i+3)) for i in range(1,2000,3)] #deterministic die, excess roll sums well beyond 1000
roll_idx = 0

while True:
    p1_pos = (p1_pos + die_rolls[roll_idx]-1)%10+1 # Cycle from 1-9 using (i-1)%10+1 
    p1_score += p1_pos
    roll_idx +=1   
    if p1_score >= 1000:
        break
    
    p2_pos = (p2_pos + die_rolls[roll_idx]-1)%10+1
    p2_score += p2_pos
    roll_idx +=1
    if p2_score >= 1000:
        break       
print(roll_idx*3*min([p1_score,p2_score]))
print(p1_score,p2_score)


# PART 2

p1_pos, p2_pos = 3,7
p1_score, p2_score = 0,0
  
  
@functools.lru_cache(maxsize=None) # Makes recursion run much faster
def play_dirac(p1_pos,p1_score,p2_pos,p2_score): 
    p1_wins, p2_wins = 0, 0
    # Iterate through all possible rolls
    for roll in itertools.product([1,2,3],repeat=3):
        p1_newpos = (p1_pos + sum(roll)-1)%10+1
        p1_newscore = p1_newpos+p1_score
        if p1_newscore >= 21:
            p1_wins += 1
        else:
            # Player 2's turn, swap the inputs
            p2_newwin, p1_newwin = play_dirac(p2_pos,p2_score,p1_newpos,p1_newscore)
            p1_wins += p1_newwin
            p2_wins += p2_newwin
            
    return p1_wins, p2_wins
    
print(max(play_dirac(p1_pos,p1_score,p2_pos,p2_score)))
