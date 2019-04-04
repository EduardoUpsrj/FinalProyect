import prime_numbers

def test_example1():
    answer = prime_numbers.primeNumbers(7)
    assert answer == True
    

def test_example2():
    answer = prime_numbers.primeNumbers(-7)
    assert answer == True
