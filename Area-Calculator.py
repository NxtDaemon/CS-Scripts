import math

def AreaHandler(Shape,Parameter1,Parameter2):
  'Function To Handle Outputting Area of Standard Shapes'
  Shape = Shape.lower()
  if Shape == "square":
    Width = Parameter1
    return(Width ** 2)
  elif Shape == "rectangle":
    Width = Parameter1
    Length = Parameter2
    return (Width * Length)
  elif Shape == "circle":
    Radias = Parameter1
    return(math.pi * Radias ** 2)
  elif Shape == "triangle":
    Base = Parameter1
    Height = Parameter2
    return ((Base * Height) /2 )
  else:
    return("unrecognised")
  
  
# testing 
print(AreaHandler("Square",5,None))
print(AreaHandler("Rectangle",4,6))
print(AreaHandler("Circle",10,None))
print(AreaHandler("Triangle",7,4))