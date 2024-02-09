from main import fizzbuzz
# write test code

def test_fizzbuzz():
    assert fizzbuzz(15) == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]
    assert fizzbuzz(5) == [1, 2, "fizz", 4, "buzz"]
    assert fizzbuzz(1) == [1]
    assert fizzbuzz(3) == [1, 2, "fizz"]
    




# docker build -t fizzbuzz .
# docker run fizzbuzz

# pip freeze > requirements.txt
# pip list
