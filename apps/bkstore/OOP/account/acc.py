class Account:

    def __init__(self,filepath): # to use a variable anywhere else in a class, ref it to the self attribute eg. self.filepath
        self.filepath=filepath
        with open(self.filepath, 'r') as file:
            self.balance=int(file.read()) # balance is the instance variable and self is the object

    def withdraw(self,amount):
        self.balance=self.balance - amount # subtract amount to withdraw from balance

    def deposit(self,amount):
        self.balance=self.balance + amount # add amount to deposit to current balance

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

# Inheritance helps you derive a sub class out of a base class. The sub class contains all the methods of the base class and some more.
class Checking(Account):
    """This class generates checking account objects""" # __doc__ for documentation via print

    type="checking" # is a class variable since it is declared outside the methods in the class but is valid for all methods. Instance variables (self.fee for eg.) is valid only for the instance

    def __init__(self,filepath,fee): # you can add extra parameters
        self.fee=fee
        Account.__init__(self,filepath) # this basically creates the Account class inside Checking

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee # remove amount to be transferred


jack_aza=Checking("account//jack.txt",1) # jack_aza is an instance variable valiid only for this instance.
jack_aza.transfer(5)
print(jack_aza.balance)
jack_aza.commit()
print(jack_aza.type) # this 'type' is a class variable valid in all instances.

john_aza=Checking("account//john.txt",1) # john_aza is an instance variable valid only for this instance.
john_aza.transfer(4)
print(john_aza.balance)
john_aza.commit()
print(john_aza.type) # type is a class variable valid for all methods in the class

print(john_aza.__doc__) # print the documentation of the class being used - Checking in this case.
