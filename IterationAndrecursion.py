print("iterative version")
num=int(input("enter a number:"))
factorial = 1

if num<0:
    print("no factorial")
if num >= 0:
    for t in range(1, 1+num):
        factorial = t*factorial
print(factorial)

print("recursive version")

def fact(i):
    return 1 if (i==1 or i==0) else i*fact(i-1);

print(fact(num))
    