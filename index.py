import random
from decimal import Decimal

def coin_flip():
  heads = 0
  tails = 1
  ht = random.randint(heads, tails)

  if ht == 0:
    print('You flipped heads!')
  elif ht == 1:
    print('You flipped tails!')
  else:
    print('You should only be getting heads or tails.')
  return ht

def starting_amount():
  print('How much money would you like to start with?')
  money = input()
  return Decimal(money) 

def bet_amount(balance):
  print('How much would you like to bet?')
  print('If you would like to quit bet $0')
  bet = input()
  while Decimal(bet) > Decimal(balance):
    print('You can not bet more than you have.')
    print('How much would you like to bet?')
    bet = input()
  return Decimal(bet)

def coin_flip_choice():
  print('Would you like to be heads or tails?')
  print('Please select 0 for heads, 1 for tails, 2 to quit')
  print('0: Heads')
  print('1: Tails')
  choice = input()
  while int(choice) > 1:
    print('This is not a valid choice. Try again!')
    print('0: Heads')
    print('1: Tails')
    choice = input()
  return int(choice)

def main():
  choice = 0
  money = starting_amount()
  balance = money
  bet = -1

  while bet != 0:  
    bet = bet_amount(balance)
    if bet == 0:
      break

    choice = coin_flip_choice() 
    ht = coin_flip()
  
    if choice == ht:
      print('You won!')
      balance = balance + bet
      print(f'Your balance is now {balance}.')
    else:
      print('You lose!')
      balance = balance - bet
      print(f'Your balance is now {balance}.')

    if balance == 0:
      print('Would you like to quit or add money?')
      print('0: Quit')
      print('1: Add money')
      wallet = input()
      if int(wallet) == 0:
        break
      elif int(wallet) == 1:
        print('How much money do you want to add?')
        wallet = input()
        balance = balance + Decimal(wallet)
        print(f'Your balance is now {balance}.')
      else:
        while int(wallet) > 1:
          print('This is not a valid choice. Try again!')
          print('0: Quit')
          print('1: Add money')
          wallet = input()
          balance = balance + Decimal(wallet)

if __name__== "__main__":
    main()