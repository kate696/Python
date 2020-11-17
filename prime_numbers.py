N = 50

print("The first prime numbers between 1 and 50 are:")

for p in range(1, N + 1):
   if p > 1:
       for i in range(2, p):
           if (p % i) == 0:
               break
       else:
           print(p)