n=int(input("Enter the range:"))
for row in range (1,n+1):
   space=n-row
   star=row
   print (" "*space + "* " *star)
for row in range (n-1,0,-1):
   space=n-row
   star=row
   print (" "*space + "* "*star)
