class ATM:
  def __init__(self,card_holder,card_number,card_company,card_bank,card_balance,card_password):
    self.card_holder=card_holder
    self.card_number=card_number
    self.card_company=card_company
    self.card_bank=card_bank
    self.card_balance=card_balance
    self.card_password=card_password

  def credit(self,Amount,passWord,Card_no):
    if self.card_number==Card_no and self.card_password==passWord:
      self.card_balance=self.card_balance+int(Amount)
      print("Cash deposited! thank you")
    else:
      return "Not a valid card or check your pin again!!"
  def debit(self,Amount,passWord,Card_no):
    if self.card_number==Card_no and self.card_password==passWord:
      self.card_balance=self.card_balance-int(Amount)
      print("Cash withdrawl successful! pls collect your cash")
    else:
      return "Not a valid card or check your pin again!!"
  def check_balance(self,passWord,Card_no):
    if self.card_number==Card_no and self.card_password==passWord:
      print("your balance is: ",self.card_balance)
    else:
      return "Not a valid card or check your pin again!!"

if __name__=="__main__":
  a=[]
  n=int(input("Enter the number of cards: "))
  for i in range(n):
    card_holder=input("Enter the card holder name: ")
    card_number=int(input("Enter the card number: "))
    card_company=input("Enter card company: ")
    card_bank=input("Enter the name of bank: ")
    card_balance=int(input("Enter the balance: "))
    card_password=int(input("Enter the password: "))
    obj=ATM(card_holder,card_number,card_company,card_bank,card_balance,card_password)
    a.append(obj)
