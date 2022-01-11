import sys

string = sys.argv[1]

def reverse(s):
  string = ""
  for i in s:
    string = i + string
  return string

print ("Input String: ",end="")
print (string)
  
print ("Reversed String: ",end="")
print (reverse(string))