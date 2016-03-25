
import random

class Account(object):
  """docstring for Account"""


class EvilAccount(Account):
  def iquiry(self):
    if random.randint(0,4) == 1:
      return self.balance * 1.10

class DepositCharge(object):
  """docstring for DepositCharge"""
  fee = 5.00
  def deposit_fee(self):
    self.withdraw(self.fee)

class withdrawCharge(object):
  fee = 3.50
  def withdrawFee(self):
    self.withdraw(self.fee)

# Class using multiple inheritance
class MostEvilAccount(EvilAccount, DepositCharge, withdrawCharge):
  def deposit(self, amt):
    self.deposit_fee()
    super(MostEvilAccount, self).deposit(amt)
  def withdraw(self, amt):
    self.withdraw_fee()
    super(MostEvilAccount, self).withdraw(amt)

