import example2

def test_example1():
    answer = example2.primeNumbers(7)
    assert answer == True
    

def test_example2():
    answer = example2.primeNumbers(-5)
    assert answer == False
