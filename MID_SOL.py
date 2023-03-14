game_number = int(input())
our_win = 0
our_score = 0
their_score = 0


for i in range(0, game_number):
  
  x = input()
  our_goal = int(x[0])
  their_goal = int(x[2])
                   
  if our_goal > their_goal:
    our_win += 1
    our_score += 3
    their_score += 0
    
  elif our_goal == their_goal: 
    our_score += 1
    their_score += 1
    
  elif our_score < their_goal:
    our_score += 0
    their_score += 3

print(f"Your score is {our_score}")
print(f"Winning percentage: {our_win/(game_number * 100)}%")