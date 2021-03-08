#Standard-Form-Calculator

def StandardFormController(InputNumber):
  'Funtion to put a number into standard form'
  CheckVal = InputNumber
  Counter = 0 
  
  while InputNumber >= 10: 
    InputNumber /= 10
    Counter += 1
    
  while InputNumber < 1:
    InputNumber *= 10 
    Counter -= 1 
    
  print(f"{InputNumber} x 10^{Counter}")
  
StandardFormController(41400000000000)
StandardFormController(0.00000000027) # Causes ugly numbers due to precise math can be cut down with number formatting into a X amount of chars 
StandardFormController(5972000000000000000000000)
StandardFormController(1898000000000000000000000000) 