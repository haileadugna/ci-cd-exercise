# fizzbuss

def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        
# write test 

def test_fizzbuzz():
    assert fizzbuzz(15) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]
    assert fizzbuzz(5) == [1, 2, "fizz", 4, "buzz"]
    assert fizzbuzz(1) == [1]
    



# docker build -t fizzbuzz .
# docker run fizzbuzz

# pip freeze > requirements.txt
# pip list
