import warnings
import numpy as np
from itertools import cycle
import os
 
warnings.simplefilter(action='ignore', category=FutureWarning)
bored = np.zeros((3, 3), dtype=int)
 
x_win = np.array([1, 1, 1])
o_win = np.array([2, 2, 2])

playing = True
 
def show_bored():
   bored_text = ""
   print("  A B C")
   for x in range(3):
     bored_text += str(x + 1) + " "
     for y in range(3):
       if bored[x, y] == 1:
         bored_text += "X "
       elif bored[x, y] == 2:
         bored_text += "O "
       elif bored[x, y] == 0:
         bored_text += "_ "
     bored_text += "\n"
 
   print(bored_text + "\n")
 
show_bored()
 
def check_bored():
   global playing
   diagonal_right = []
   diagonal_left = []
 
   top_rl = np.array(bored[0, :], dtype=int)
   mid_rl = bored[1, :]
   bot_rl = bored[2, :]
 
   left_ud = bored[:, 0]
   mid_ud = bored[:, 1]
   right_ud = bored[:, 2]
 
   for x in range(3):
       diagonal_right.append(bored[x, x])
   diagonal_right = np.array(diagonal_right)
   for x in range(3):
       y = abs(x - 2)
       diagonal_left.append(bored[x, y])
   diagonal_left = np.array(diagonal_left)
 
   # Right left wins
   if np.allclose(top_rl, x_win):
       print("X wins")
       replay()
       return
   elif np.allclose(top_rl, o_win):
       print("O wins")
       replay()
       return
   if np.allclose(mid_rl, x_win):
       print("X wins")
       replay()
       return
   elif np.allclose(mid_rl, o_win):
       print("O wins")
       replay()
       return
   if np.allclose(bot_rl, x_win):
       print("X wins")
       replay()
       return
   elif np.allclose(bot_rl, o_win):
       print("O wins")
       replay()
       return
 
   # Up down wins
   if np.allclose(left_ud, x_win):
       print("X wins")
       replay()
       return
   elif np.allclose(left_ud, o_win):
       print("O wins")
       replay()
       return
   if np.allclose(mid_ud, x_win):
       print("X wins")
       replay()
       return
   elif np.allclose(mid_ud, o_win):
       print("O wins")
       replay()
       return
   if np.allclose(right_ud, x_win):
       print("X wins")
       replay()
       return
   elif np.allclose(right_ud, o_win):
       print("O wins")
       replay()
       return

   # Diagonal wins
   if np.allclose(diagonal_right, x_win):
       print("X wins")
       replay()
       return
   elif np.allclose(diagonal_right, o_win):
       print("O wins")
       replay()
       return 
        
   if np.allclose(diagonal_left, x_win):
       print("X wins")
       replay()
       return
   elif np.allclose(diagonal_left, o_win):
       print("O wins")
       replay()
       return
   
   # Tie
   if not 0 in bored:
     print("Draw")
     replay()
     return
 
def player_input(mark):
  if mark == 1:
    choice = input("X turn: ")
    mark_number = 1
  elif mark == 2:
    choice = input("O turn: ")
    mark_number = 2
   
  try:
    number = int(choice[0]) - 1
    letter = choice[1]
 
    if letter.lower() == "a":
      letter = 0
    elif letter.lower() == "b":
      letter = 1
    elif letter.lower() == "c":
      letter = 2
    
    if bored[number, letter] == 0:
      bored[number, letter] = np.array(mark_number)
    else:
      print("Spot already taken")
      return player_input(mark=mark)
 
  except:
    print("Error with input")
    return player_input(mark=mark)

def clear_bored():
  global bored
  bored = np.zeros((3, 3), dtype=int)

def replay():
  global playing
  answer = input("Do yo wish to play again?: ")

  if answer.lower() == "y" or answer.lower() == "yes":
    clear_bored()
    os.system("clear")
    show_bored()
  else:
    playing = False


marks = cycle([1, 2])
while playing:
   mark = next(marks)
   player_input(mark=mark)
   os.system("clear")
   show_bored()
   check_bored()
