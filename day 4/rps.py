import random
def O_input():
  opponent_chocie = random.randint(1,3)
  if opponent_chocie == 1:
    print('Rock!')
  if opponent_chocie == 2:
    print('Paper!')
  if opponent_chocie == 3:
    print('Scissors!')
  return opponent_choice
def P_input():
  return int(input('(1)Rock (2)Paper (3)Scissors')
def main():
  pc = p_input()
  oc = O_input()
  if pc == 1 and oc == 1:
    print('tie!')
  if pc == 2 and oc == 2:
    print('tie!')
  if pc == 3 and oc == 3:
    print('tie!')
  if pc == 1 and oc == 2:
    print('Opponent Won!')
  if pc == 1 and oc == 3:
    print('Player Won!')
  if pc == 2 and oc == 1:
    print('Player Won!')
  if pc == 2 and oc == 3:
    print('Opponent Won!')
  if pc == 3 and oc == 1:
    print('Opponent Won!')
  if pc == 3 and oc == 2:
    print('Player Won!')
main()
