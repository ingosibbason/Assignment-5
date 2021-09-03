#Generate a sequence that lokks like 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
#Ask user how many ot those numbers he wants (n)
#The Sequence starts is can be described like this:
#1. 1       = 1     Starts with 1
#2. 1+1     = 2     Adds 1, since 1 is the last number in the sequence
#3. 1+2     = 3     Adds 1 and 2 to get 3
#4. 1+2+3   = 6     Adds 1, 2 and 3 to get 6
#5. 2+3+6   = 9     Only adds the last three digits in the sequence from now on until n
# And print the output

n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_current = 1
num_keep = 0
num1 = 1
num2 = 0
num3 = 0
num1old = 0
num2old = 0
num_over9 = 0


# print(num_current)
# num_current += num1
# num1 = num_current

for i in range(0, n):                   #1
    if i == 0:
        print(num_current)
        num_keep = num_current
        num_current += num1
        num_keep = num_keep
    elif i == 1:                        #1+1 = 2
        print(num_current)   
        
        num_keep = num_current           
        num_current += num1
        num1old = num1
        num1 = num_keep
        num2 = num1old
        num3 = num_current
    elif i == 2:
        print(num_current)              #1+2+3=6
        num_current = num1 + num2 + num3 
        num_keep = num_current  
        num1old = num1          #Geyma num1
        num1 = num_keep         #Num1 er núna nýja talan
        num2old = num2          #Geyma num1
        num2 = num1old          #Num2 er núna gamla num1
        num3 = num2old          #Num3 er núna gamla num2 (Þarf ekki að geyma gamla þristinn)
    elif i == 3:
        print(num_current)              #1+2+3=6
        num_current = num1 + num2 + num3 
        num_keep = num_current  
        num1old = num1          #Geyma num1
        num1 = num_keep         #Num1 er núna nýja talan
        num2old = num2          #Geyma num1
        num2 = num1old          #Num2 er núna gamla num1
        num3 += num2old          #Num3 er núna gamla num2 (Þarf ekki að geyma gamla þristinn)
        num_over9 = num_keep + num2old
    