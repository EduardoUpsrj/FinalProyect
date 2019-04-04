def primeNumbers(number):
    if number > 0:     
        i = 2
        while i <= number:
            increment = 2
            isPrime = True
            while isPrime and increment < i:                    
                if i % increment == 0:
                    isPrime = False
                else:
                    increment += 1                        
            if isPrime:
                print(i,"is a prime number.")
            i += 1
        
        return True
    else:
        print("The number entered is incorrect.")
        
        return False

primeNumbers(10)   
#primeNumbers(-8)

