from copy import deepcopy
import numpy as np
import random

class Agent:
  def __init__(self, playerChar, competitorChar, weights, update):
    self.weights = weights
    self.player = playerChar
    self.competitor = competitorChar
    self.alpha = 0.0001
    self.updateMechanism = update

  def look_for_winner(self, stateBoard, player):

    is_winner = False
    for i in range(3):
      if (stateBoard[i][0] == stateBoard[i][1] == stateBoard[i][2] == player) or (stateBoard[0][i] == stateBoard[1][i] == stateBoard[2][i] == player):
        is_winner = True
        break
    if (stateBoard[0][0] == stateBoard[1][1] == stateBoard[2][2] == player) or (stateBoard[0][2] == stateBoard[1][1] == stateBoard[2][0] == player):
      is_winner = True
    return is_winner

  def is_board_full(self, stateBoard):
    for i in range(3):
      for j in range(3):
        if stateBoard[i][j] == ' ':
          return False     
    return True
          
  def is_game_finished(self, stateBoard):
    finished = False
    winner = 'none'
    if (self.look_for_winner(stateBoard, 'X')):
      finished = True
      winner = 'X'

    elif (self.look_for_winner(stateBoard, 'O')):
      finished = True
      winner = 'O'
    
    elif (self.is_board_full(stateBoard)):
      finished = True
      winner = 'tie'
    return (finished, winner)

  def possible_successors(self, stateBoard, player):
    successors = []
    for i in range(3):
      for j in range(3):
        if stateBoard[i][j] == ' ':
          succ = deepcopy(stateBoard)
          succ[i][j] = player
          successors.append(succ)
    return successors

  def count_2succesive(self, stateBoard, player):
    f = 0
    #check rows
    for i in range(3): 
      if (stateBoard[i][0] == stateBoard[i][1] == player) and (stateBoard[i][2] == ' '):
        f += 1
      if (stateBoard[i][0] == stateBoard[i][2] == player) and (stateBoard[i][1] == ' '):
        f += 1
      if (stateBoard[i][2] == stateBoard[i][1] == player) and (stateBoard[i][0] == ' '):
        f += 1

    #check columns
    for i in range(3): 
      if (stateBoard[0][i] == stateBoard[1][i] == player) and (stateBoard[2][i] == ' '):
        f += 1
      if (stateBoard[0][i] == stateBoard[2][i] == player) and (stateBoard[1][i] == ' '):
        f += 1
      if (stateBoard[2][i] == stateBoard[1][i] == player) and (stateBoard[0][i] == ' '):
        f += 1
    
    #check diagonal
    if (stateBoard[0][0] == stateBoard[1][1] == player) and (stateBoard[2][2] == ' '):
      f += 1
    if (stateBoard[0][0] == stateBoard[2][2] == player) and (stateBoard[1][1] == ' '):
      f += 1
    if (stateBoard[2][2] == stateBoard[1][1] == player) and (stateBoard[0][0] == ' '):
      f += 1
    if (stateBoard[2][0] == stateBoard[1][1] == player) and (stateBoard[0][2] == ' '):
      f += 1
    if (stateBoard[2][0] == stateBoard[0][2] == player) and (stateBoard[1][1] == ' '):
      f += 1
    if (stateBoard[0][2] == stateBoard[1][1] == player) and (stateBoard[2][0] == ' '):
      f += 1
    return f
  
  def count_3corner(self, stateBoard, player):
    f = 0
    if (stateBoard[0][0] == stateBoard[2][0] == stateBoard[0][2] == player) and (stateBoard[1][0] == stateBoard[0][1] == ' '):
      f += 1  
    if (stateBoard[0][0] == stateBoard[2][0] == stateBoard[2][2] == player) and (stateBoard[1][0] == stateBoard[2][1] == ' '):
      f += 1 
    if (stateBoard[2][2] == stateBoard[2][0] == stateBoard[0][2] == player) and (stateBoard[2][1] == stateBoard[1][2] == ' '):
      f += 1 
    if (stateBoard[0][0] == stateBoard[0][2] == stateBoard[2][2] == player) and (stateBoard[1][2] == stateBoard[0][1] == ' '):
      f += 1 
    return f

  def count_1in_empty(self, stateBoard, player):
    f = 0
    #check rows
    for i in range(3): 
      if (stateBoard[i][0] == stateBoard[i][1] == ' ') and (stateBoard[i][2] ==player):
        f += 1
      if (stateBoard[i][0] == stateBoard[i][2] == ' ') and (stateBoard[i][1] ==player):
        f += 1
      if (stateBoard[i][2] == stateBoard[i][1] == ' ') and (stateBoard[i][0] ==player):
        f += 1

    #check columns
    for i in range(3): 
      if (stateBoard[0][i] == stateBoard[1][i] == ' ') and (stateBoard[2][i] ==player):
        f += 1
      if (stateBoard[0][i] == stateBoard[2][i] == ' ') and (stateBoard[1][i] ==player):
        f += 1
      if (stateBoard[2][i] == stateBoard[1][i] == ' ') and (stateBoard[0][i] ==player):
        f += 1
    
    #check diagonal
    if (stateBoard[0][0] == stateBoard[1][1] == ' ') and (stateBoard[2][2] ==player):
      f += 1
    if (stateBoard[0][0] == stateBoard[2][2] == ' ') and (stateBoard[1][1] ==player):
      f += 1
    if (stateBoard[2][2] == stateBoard[1][1] == ' ') and (stateBoard[0][0] ==player):
      f += 1
    if (stateBoard[2][0] == stateBoard[1][1] == ' ') and (stateBoard[0][2] ==player):
      f += 1
    if (stateBoard[2][0] == stateBoard[0][2] == ' ') and (stateBoard[1][1] ==player):
      f += 1
    if (stateBoard[0][2] == stateBoard[1][1] == ' ') and (stateBoard[2][0] ==player):
      f += 1
    return f

  def count_corner(self, stateBoard, player):
    f = 0
    #check rows
    for i in range(3): 
      if (stateBoard[i][2] ==player):
        f += 1
      if (stateBoard[i][0] ==player):
        f += 1

    #check columns
    for i in range(3): 
      if (stateBoard[2][i] ==player):
        f += 1
      if (stateBoard[0][i] ==player):
        f += 1

    return f

  def count_center(self, stateBoard, player):
    if stateBoard[1][1] == player:
      return 1
    else:
      return 0

  def count_3succesive(self,stateBoard, player):
    f = 0
    #check rows
    for i in range(3): 
      if (stateBoard[i][0] == stateBoard[i][1] == stateBoard[i][2] == player):
        f += 1

    #check columns
    for i in range(3): 
      if (stateBoard[0][i] == stateBoard[1][i] == stateBoard[2][i] == player):
        f += 1
    
    #check diagonal
    if (stateBoard[0][0] == stateBoard[1][1] == stateBoard[2][2] == player):
      f += 1
    if (stateBoard[0][2] == stateBoard[1][1] == stateBoard[2][0] == player):
      f += 1
    return f

  def cal_features(self, stateBoard, player, competitor):
    #f1: number of 2 symbol in a row/column/diagonal which third place is empty
    f1 = self.count_2succesive(stateBoard, player)
    #f2: number of 2 symbol in a row/column/diagonal which third place is empty of player's competitor
    f2 = self.count_2succesive(stateBoard, competitor)
    #f3: being in a row/column/diagonal with 2 empty space
    f3 = self.count_1in_empty(stateBoard, player)
    #f4: being in a row/column/diagonal with 2 empty space of player's competitor
    f4 = self.count_1in_empty(stateBoard, competitor)
    #f5: being in a corner with 2 empty space
    f5 = self.count_corner(stateBoard, player)
    #f6: being in a corner with 2 empty space of player's competitor
    f6 = self.count_corner(stateBoard, competitor)
    #f7: being in the center
    f7 = self.count_center(stateBoard, player)
    #f8: being in the center of player's competitor
    f8 = self.count_center(stateBoard, competitor)
    return [1, f1, f2, f3, f4, f5, f6, f7, f8]

  def cal_score_non_final_state(self, weights, features):
    weights = np.array(weights)
    features = np.array(features)
    return (weights.T @ features)

  def cal_score(self, stateBoard, player, competitor):
    gameOver, winner = self.is_game_finished(stateBoard)
    if gameOver:
      if winner == player:
        score = 100
      elif winner == 'tie':
        score = 0
      else:
        score = -100
    else:
      features = self.cal_features(stateBoard, player, competitor)
      score = self.cal_score_non_final_state(self.weights, features)
    return score

  def update_weights(self, st0, st1):
    scoreSt0 = self.cal_score(st0, self.player, self.competitor)
    scoreSt1 = self.cal_score(st1, self.player, self.competitor)
    delta = scoreSt1 - scoreSt0
    self.weights[0] = self.weights[0] + (self.alpha * delta)
    self.weights[1] = self.weights[1] + (self.alpha * delta * self.count_2succesive(st0, self.player))
    self.weights[2] = self.weights[2] + (self.alpha * delta * self.count_2succesive(st0, self.competitor))
    self.weights[3] = self.weights[3] + (self.alpha * delta * self.count_1in_empty(st0, self.player))
    self.weights[4] = self.weights[4] + (self.alpha * delta * self.count_1in_empty(st0, self.competitor))
    self.weights[5] = self.weights[5] + (self.alpha * delta * self.count_corner(st0, self.player))
    self.weights[6] = self.weights[6] + (self.alpha * delta * self.count_corner(st0, self.competitor))
    self.weights[7] = self.weights[7] + (self.alpha * delta * self.count_center(st0, self.player))
    self.weights[8] = self.weights[8] + (self.alpha * delta * self.count_center(st0, self.competitor))

  def find_best_move(self, stateBoard):
    successors = self.possible_successors(stateBoard, self.player)
    scoreSuccesors = []
    for nextState in successors:
      score = self.cal_score(nextState, self.player, self.competitor)
      scoreSuccesors.append(score)
      # print_board(nextState)
      # print(score, "\n\n")
    nextState = successors[scoreSuccesors.index(max(scoreSuccesors))]
    if self.updateMechanism:
      self.update_weights(stateBoard, nextState)
    return nextState

  def first_move(self, stateBoard):
    successors = self.possible_successors(stateBoard, self.player)
    nextState = random.choice(successors)
    if self.updateMechanism:
      self.update_weights(stateBoard, nextState)
    return nextState

def play_agents(weights1, weights2):
  stateBoard = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
  gameStates = []
  agent1 = Agent('X', 'O', weights1, True)
  agent2 = Agent('O', 'X', weights2, True)
  first = True
  while(True):
    if first:
      stateBoard = agent1.first_move(stateBoard)
      first = False
    else:
      stateBoard = agent1.find_best_move(stateBoard)
    gameStates.append(stateBoard)
    finished, winner = agent1.is_game_finished(stateBoard)
    if finished:
      if winner == 'X':
        msg = 'agent1 won the game'
      elif winner == 'tie':
        msg = 'no one won the game'
      else:
        msg = 'agent2 won the game'
      return(gameStates, msg, agent1.weights, agent2.weights, winner)
      
    stateBoard = agent2.find_best_move(stateBoard)
    gameStates.append(stateBoard)
    finished, winner = agent2.is_game_finished(stateBoard)
    if finished:
      if winner == 'X':
        msg = 'agent1 won the game'
      elif winner == 'tie':
        msg = 'no one won the game'
      else:
        msg = 'agent2 won the game'
      return(gameStates, msg, agent1.weights, agent2.weights, winner)

def print_board(stateBoard):
  print('\n')
  print(stateBoard[0][0] + '|' + stateBoard[1][0] + '|' + stateBoard[2][0])
  print("-----")
  print(stateBoard[0][1] + '|' + stateBoard[1][1] + '|' + stateBoard[2][1])
  print("-----")
  print(stateBoard[0][2] + '|' + stateBoard[1][2] + '|' + stateBoard[2][2])
  print('\n')	

def trian_agents():
  weights1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  weights2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
  winAgent1 = 0
  winAgent2 = 0
  tie = 0
  for _ in range(300):
    gameStates, msg, weights1, weights2, winner = play_agents(weights1, weights2)
    if winner == 'X':
      winAgent1 += 1
    elif winner == 'tie':
      tie += 1
    else: 
      winAgent2 += 1

    for state in gameStates:
      print_board(state)
    print (msg)

  print ("weights1", weights1)
  print ("weights2", weights2)
  print ("agent1: ", winAgent1, " Agent2: ", winAgent2, " tie: ", tie)
  if winAgent1 > winAgent2:
    return weights1
  else:
    return weights2

trian_agents()
