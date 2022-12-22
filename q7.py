n = int(input("Enter the number of fibonacci numbers you wish to average out:"))
if n<1:
    print("Not supported")
    exit()
###Fibonacci terms
ft=1
prevTerm = 0
###A variable to strore the sum of all the numbers
sumOfNum = 0
print("Fibpnacci series")
for k in range(0,n):
    ###store the sum of fibonacci terms in sumofNum
    sumOfNum += prevTerm
    print(prevTerm,end = " " )
    ###keep adding previous term to get next term
    c = ft
    ft += prevTerm
    prevTerm = c
print("\nAverage of first ",n,"terms is ",sumOfNum/n)

