'''
This Capstone project is based on our discussion in class, The project is to create a Google Pay replica

Prerequisites:

1) understanding of class, objects and OOPS concepts (https://www.programiz.com/python-programming/object-oriented-programming)

2) understanding of design patterns: (https://henriquesd.medium.com/design-patterns-introduction-220f811db857)

3) understanding mediator pattern (https://refactoring.guru/design-patterns/mediator/python/example#:~:text=Mediator is a behavioral design,the dozens of other classes.), pls read the given link and click on "Learn about Mediator"

Instructions: 

1) Spend the first 30 to 40 mins reading through the resources I have provided ( this is mandatory to solve the problem)

2) After having read through it, our task is the following: 

  a) Every user must be able to sign up using google pay

  b) once registered, he must be able to sync his accounts (keep this random)

  c) must be able to send/recieve money

  d) A ledger to keep track of the money he recieve or spend

3) Pls understand that you dont need to do this as an application, do this just as class and objects and using some or all of the oops concepts depending on your idea

4) you are free to use any idea, this is a creative assignment, so dont worry about marks, and grading wont be linear, so try to be creative and add comments for what you have done

5) Once complete paste your entire code here

'''



# def menu():
#   a=input()
# #Taking input from user to login or signup
# x="You want to login or sign up for this website"
# print(x)
# y=input("Enter your answer: ")
# f=open("text.txt","w+")
# if (y=="login"):
#   username=input("Enter your username: ")
#   password=input("Enter your password: ")
#   with open(r'text.txt','r') as file:
#     context=file.read()
#     if username in context:
#       if password in context:
#         # calling the functn
#         menu()
#     else:
#       print("Your username or password is incorrect.")
      
# elif (y=="signup"):
#   username=input("Enter your username: ")
#   password=input("Create your password: ")
#   f.write(username+"\t"+password+"\n")
#   with open(r'text.txt','r') as file:
#     context=file.read()
#     if username in context:
#       if password in context:
#         print("Your account had already existed.")
#         print("Try to login")



def choices():
    choice = int(input("For Sigining Up Type 1 and For login Type 2: "))
    if choice == 1:
       return getdetails()
    elif choice == 2:
       return checkdetails()
    else:
       raise TypeError

def getdetails():
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("User_Data.txt",'w')
    info = info + " " +name + " " + password
    f.write(info)

def checkdetails():
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            return "Welcome Back, " + name
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Please Sign Up."

print(choices())

# def menu():
#   print("1.Balance\t 2.Transaction")
#   choose=int(input("Enter your choice: "))
#   if choose==1:
#     return balance()
#   elif choose==2:
#     return transaction()
#   else:
#     TypeError("Please select correct number.")
# print(menu())

# def transaction():
#   print("1.Send \t 2.Recieve")
#   x=int(input("Enter your choice: "))
#   if x==1:
#     return send()
#   elif x==2:
#     return receive()
#   else:
#     return Type Error("Please select correct number.")


class Bank_Account:
	def __init__(self):
		self.balance=500
		print("Welcome to the Deposit & Withdrawal: ")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance >= amount:
			self.balance -= amount
			print("\n You Withdraw:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)
  
  def send(self):
    amount = float(input("Enter amount to be send: "))
    if self.balance >= amount:
      self.balance -= amount
      print("\n You had send:", amount)
    else:
      print("\n Insufficient balance ")

# Calling functions with that class object
def func():
  print("1.Deposit \t 2.Withdraw \t 3.Net balance \t 4.send")
  x=int(input("Enter your choice: "))
  if x==1:
    s = Bank_Account()
    s.deposit()
  elif x==2:
    s = Bank_Account()
    s.withdraw()
  elif x==3:
    s = Bank_Account()
    s.display()
  elif x==4:
    s = Bank_Account()
    s.send()
  else:
    print("Wrong Choice")
func()
   