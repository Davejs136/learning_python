# !/usr/bin/python3
# -*- encoding: utf-8 -*-
from os import system

class Ticket():
  """ Class to buy tickets """
  def __init__(self, economic, middle, executive):
    self.economic = economic
    self.middle = middle
    self.executice = executive

  def run(self):
    self.status()
    option = self.cin('Enter the option: ')
    self.clear()
    while True:
      # Option 1 is executive
      if option == 1:
        self.buy_tickets(self.executice, 'executive')

      # Option 2 is middle
      elif option == 2:
        self.buy_tickets(self.middle, 'middle')

      elif option == 3:
        self.buy_tickets(self.economic, 'economic')

      # Status message
      elif option == 4:
        self.status()

      # Exit script
      elif option == 5:
        self.clear()
        print('Exit script')
        return 0
      
  def buy_tickets(self, type_tickets, name):
    self.clear()
    tickets = self.cin('Enter the amount: ')
    if tickets > type_tickets:
      print('Limit exceeded')
    else:
      self.clear()
      self[type_tickets] -= tickets
      print(f'You are buy {tickets} {type_tickets}')

  def status(self):
    self.clear()
    print('***** Airplane tickets status *****')
    print('1 ----------> Buy executive Tickets')
    print('2 ----------> Buy middle Tickets')
    print('3 ----------> Buy economic Tickets')
    print('4 ----------> Status Tickets')
    print('5 ----------> Exit system\n')

  def cin(self, message):
    return int(input(message))

  def clear(self):
    system('clear')

tickets = Ticket(100, 150, 50)
tickets.run()