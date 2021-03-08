import random

def MakePassword(Length):
  CharList = []
  for _ in range(0,Length):
    char = chr(random.randint(33,126))
    CharList.append(char)
  random.shuffle(CharList)
  Password = ""
  for _ in CharList:
    Password += _
  return(Password)

print(MakePassword(15))