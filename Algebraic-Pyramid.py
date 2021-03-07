# Algebraic-Pyramid.py
def MutateList(ListObj):
  'Function to Mutate a list object whenever called rather than recursively running this code'
  ListObjReturn = []
  for _ in range(0,len(ListObj)-1):
    ListObjReturn.append(ListObj[_]+ListObj[_+1])
  return(ListObjReturn)

def DrawPyramid(ListObj):
  'Function to draw upside down pyramids ig?'
  NumOfLayers = len(ListObj)
  X = " "
  for layer in range(0,NumOfLayers):
    line = f"{X} "
    for item in ListObj:
      line += f"{item} "
    line += X
    print(line)
    NumOfLayers -= 1
    ListObj = MutateList(ListObj)
    X += " "
  print("\n")
    
#! testing here 

DrawPyramid([4,6,8,2])
DrawPyramid([30,12,10,5])
DrawPyramid([3,6,9,12])
DrawPyramid([3,6,9])
DrawPyramid([30,12,10,5])
DrawPyramid([1,2,3,4,5,6])

