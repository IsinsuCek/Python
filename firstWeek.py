"""rows = 5
for i in range(rows,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()"""

"""rows = 5 
for i in range (0,rows):
    for j in range (0,i+1):
        if j == 0:
           print (" "*(rows - i) + "*",end = "")
        else: print("*", end = "")
    print()"""

"""rows = 5
for i in range (rows,0,-1):
    for j in range(0,i):
       if j == 0:
        print (" "* (rows-i)+ "*",end="")
       else: print("*", end = "")
    print() """

"""rows  = 5
for i in range (rows, 0,-1):
    print (" "* (rows-i)+ "*"*i)"""

"""rows = 5
for i in range (1,rows+1):
         print (" "* (rows-i)+ "*"*i*2)"""

"""rows = 5
for i in range (rows,0,-1):
     print (" "* (rows-i)+ "*"*i*2)"""

"""rows = 5
for i in range (0,rows+1):
    print("*"*i)
    for j in range (0,rows+1):
     print (" "*(rows-j)+ "*"*j)"""

"""print("Hello World")
num = int(input("Lutfen bir sayi giriniz: "))
count = 0
for i in range (0,num):
    count = count + i 
print(count)"""