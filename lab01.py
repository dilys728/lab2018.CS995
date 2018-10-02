import sys
max = sys.maxsize
min = -sys.maxsize -1
def divide(x, y):
if y==0:
print("division by 0")
elif ((x>max) or (x<min) or (y>max) or (y<min)):
print ("overflow")
elif ((x.isalpha) or(y.isalpha)):
print("not number")
else:
z=x/y
print("Result:", z)