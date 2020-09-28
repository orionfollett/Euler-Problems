#What is the largest prime factor of the number 600851475143 ?

import math

#finds all the prime factors and returns the biggest one
def LargestPrimeFactor(num):

    factors = []
    
    while(num % 2 == 0):
        num = num % 2
        factors.append[2]
    
    for counter in range(3, int(math.sqrt(num)) + 1, 2):  
        while num % counter== 0:
            factors.append(counter)
            num = num / counter
            
    return max(factors)

    
def main():
    print(LargestPrimeFactor(600851475143))

main()
