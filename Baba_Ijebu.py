#!/usr/bin/env python
# coding: utf-8

# # Baba-Ijebu Lotto
# 
# The main principle of the game is to choose the specific number from 1 to 90. There are different ways to play, and the amount of your win directly depends on how much you stake and how much winning numbers you have. There are five options: Permutations, 2 Sure, 3,4,5 Direct.
# 
# 
# **Baba Ijebu Permutation**
# 
# Choosing this way of winning you have a higher chance to win. It means that you can combine up to ten numbers and if at least two of them come out as a draw it means that you have won. As it is the easiest way to play, you should be ready that your win won’t be so high. It is more a way to return the money you have bet.
# 
# 
# **Baba Ijebu 2 Sure**
# 
# This way is the most popular, it also has less risk as the first option but promises the higher win. You are supposed to play two numbers out of 5 in a draw that will win. 
# 
# 
# **Baba Ijebu 3 Direct**
# 
# The principle is almost the same as with 2 Sure, but you win if out of 5 draw number you have 3. If you have two or one, sorry but you have lost. 
# 
# 
# **Baba Ijebu 4 Direct**
# 
# You will win if you have four numbers out of 5 draw. 
# 
# 
# **Baba Ijebu 5 Direct**
# 
# To win, you must predict five numbers out of 5 possible.
# 
# 
# RFERENCE: http://www.netnewsledger.com/2018/04/25/play-baba-ijebu-lotto-detailed-guide/
# 
# 
# 
# 

# In[1]:


import numpy as np


# In[2]:


def selection_error_handling():
  """The function is used to restrict the input to Y or N"""
  while True:
    try:
      answer = input("specify with a Y or N \n")
      if answer.upper() in  ['Y','N']:
        return answer.upper()

    except Exception:
      print("You inputed the wrong entry, retry by specifying Y or N ")
    else:
      print("You inputed the wrong entry, retry by specifying Y or N ")
      


# In[3]:


def guess_error_handling():
  """The function is used to restrict the input to range of numbers between 1 and 90"""
  while True:
    try:
      guess = int(input("kindly input your guess "))
      if guess in  [guess for guess in range(1,91)]:
        return guess
  
    except Exception:
      print("You are to input and integer ")
    else:
      print("Your guess should be between 1 and 90")


# In[4]:


def bet_error_handling():
  """The function is used to restrict the input to values greater than or equals 100"""
  while True:
    try:
      amount = int(input("How much bet do you wish to place  "))
      if amount >= 100 :
        return amount
  
    except Exception:
      print("You must input an integer")
    else:
      print("The minimum bet allowed is 100")


# In[5]:


def game_mode():
  """ game_mode function return either SYSTEM SIMULATION or PLAYER INTERFERENCE

  Returns:
       mode(str): The game mode which get selected
   """
  print(f"Select your game mode")
  mode_list = ['SYSTEM SIMULATION','PLAYER INTERFERENCE'] 
  for mode in  mode_list:
    print(f'would you want {mode.lower()} ')
    mode_selector=selection_error_handling()
    if mode_selector=='Y':
      print(f'YOU JUST SELECTED {mode}')
      break
  return mode


# In[6]:


def Category_selector():
  """ The function is used to select the game category which can either be 
  'permutaion', '2-sure','3-direct','4-direct','5-direct'

  Returns:
    category(str): The category which gets selected

  """
  category_name=['permutaion', '2-sure','3-direct','4-direct','5-direct']
  for category in category_name:
    print(f'Would you like to play {category} ')
    
    answer=selection_error_handling()
    if answer =='Y':
      print(f'THANK YOU, YOU JUST SELECTED {category.upper()}')
      break
  return category


# In[7]:


def Correct_guess_required(category_output):
  """ The function is used to determine the minimum required correct guess to win a game
   Args:
      category_output(str): The category selected
  
   Returns:
      min_req(int): The minimum required correct guess

  """ 
  guess_dictionary={'permutaion': 2, '2-sure': 2,'3-direct': 3,'4-direct': 4,'5-direct': 5}
  min_req=guess_dictionary.get(category_output)
  return min_req


# In[8]:


def entry_required(category_output):
  """ This function is used to determine the number of required entries/guess
  Args:
    category_output(str): The game category selected

  Returns:
    int: Returns either 10 or 5

  """
  if category_output == 'permutaion':
    return 10
  else:
    return 5


# In[9]:


def data_collection(mode_output,entry_required_output):
  """ This function generates the guesses either by system simulation or player interference
      which is dependent on the game mode

    Args:
      mode_output(str): The game mode selected
      entry_required_output(int): The required number of entries

    Returns:
      data_list(list): A list of guesses
  
  """
  data_list=[]
  if mode_output =='PLAYER INTERFERENCE':
    print('You are to input numbers between 1-90')
    for attempt in range(entry_required_output,0,-1):
      print(f'You have {attempt} more attempts to go')
      guess=guess_error_handling()
      data_list.append(guess) 
  else:
    for i in range(entry_required_output):
      data_list.append(np.random.randint(1,91))
  print(f'YOUR GUESSES ARE {data_list}')
  return data_list


# In[10]:


def winning_number(entry_required_output):
  """ This function is used to simulate the winning numbers

  Args:
    entry_required_output(int): The required number of entries

  Returns:
    winning_list(list): A list of the winning numbers
  
  """
  winning_list=[]
  for i in range(entry_required_output):
    winning_list.append(np.random.randint(1,91))
  print(f'THE LUCKY NUMBERS ARE {winning_list}')
  return winning_list


# In[11]:


def win_or_lose(winning_list_output,data_list_output,category_output):
  """ This function is used to determin if the requirement to win the game is met

  Args:
    winning_list_output(list): This is a list of the winning numbers
    data_list_output(list): This is a list of the guesses
    category_output(str): The selected game category
  
  Returns:
    str: either win or lose

  """
  if len(np.intersect1d(winning_list_output,data_list_output))>=Correct_guess_required(category_output):
    print('CONGRATULATION, YOU WON')
    return 'win'
  else:
    print('SORRY, YOU LOST THE GAME')
    return 'lose'


# In[12]:


def payout():
  "This function is used to determine the amount to be paid, if the game is won"
  odd_dictionary={'permutaion': 16, '2-sure': 36,'3-direct': 64,'4-direct': 100,'5-direct': 144}
    
  bet=bet_error_handling()

  mode_output=game_mode()
    
  category_output=Category_selector()

  Correct_guess_required(category_output)
    
  entry_required_output=entry_required(category_output)

  data_list_output=data_collection(mode_output,entry_required_output)
    
  winning_list_output=winning_number(entry_required_output)

  win_or_lose_output=win_or_lose(winning_list_output,data_list_output,category_output)
    
  if win_or_lose_output == 'win':
     payout = bet * odd_dictionary.get(category_output) 
     print(f'You just won {payout}')


# In[15]:


payout()


# In[ ]:




