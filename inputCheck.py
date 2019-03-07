# Conversion Check Functions for Assignment 3

def canBeFloat(s):
   try:
      float(s)
   except:
      return False
   return True

def canBeInt(s):
   try:
      int(s)
   except:
      return False
   return True
