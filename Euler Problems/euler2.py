
#considering the terms in the Fibonacci sequence whose values
#do not exceed four million, find the sum of the even-valued terms

def SumEvenFibTerms(max):
    sum = 0
    fib1 = 1
    fib2 = 2
    

    while(fib2 < max):
        if(fib2 % 2 ==0):
            sum += fib2
        temp = fib2
        fib2 = fib1 + fib2
        fib1 = temp
    return sum

    

def main():
    print(SumEvenFibTerms(4000000))


    
main()
