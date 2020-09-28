#Find the sum of all the multiples of 3 or 5 below 1000. Linear time approach since
#it is the simplest answer and this does not need to be scaleable
def MultiplesThreeAndFive(max):
    sum = 0
    
    for counter in range(0, max):
        
        if(counter % 3 == 0 or counter % 5 == 0):
           sum += counter
           
    return sum
    
def main():
    print(MultiplesThreeAndFive(1000))


main()    
