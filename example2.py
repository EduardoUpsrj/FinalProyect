def primeNumbers(number):
    comprobar = True

    while comprobar:


        if number > 0:

            comprobar = False
            
            i = 2

            while i <= number:

                creciente = 2

                esPrimo = True

                while esPrimo and creciente < i:
                    
                    if i % creciente == 0:

                        esPrimo = False

                    else:

                        creciente += 1
                        
                if esPrimo:

                    print(i,"es primo.")

                i += 1
        else:

            print("El numero ingresado no es correcto, intenta de nuevo")
            print("falso")
            return False
        
    print("true")
    return True


primeNumbers(7)
