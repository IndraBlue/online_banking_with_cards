choice=0
while(choice<4):
  print("Press 1 to deposit cash")
  print("Press 2 to withdraw cash")
  print("Press 3 to get mini statement")

  choice=int(input("Enter choice: "))
  if choice==1:
    Card_No=int(input("Enter card no.: "))
    PassWord=int(input("Enter the password: "))
    Amount=int(input("Enter the amt to deposit: "))
    for j in a:
      j.credit(Amount,PassWord,Card_No)
  elif choice==2:
    Card_No=int(input("Enter card no.: "))
    PassWord=int(input("Enter the password: "))
    Amount=int(input("Enter the amt to withdraw: "))
    for j in a:
      j.debit(Amount,PassWord,Card_No)
  elif choice==3:
    Card_No=int(input("Enter card no.: "))
    PassWord=int(input("Enter the password: "))
    for j in a:
      j.check_balance(PassWord,Card_No)
  else:
    print("Thanks for using the ATM!!")
    break
