def fizzBuzz(n):
    # Write your code here
    i = 1
    while (i <= n):
        three_bool = False
        five_bool = False
        if (i % 3 == 0 and i >= 3):
            three_bool = True
        if (i % 5 == 0 and i >= 5):
            five_bool = True
        if (three_bool and five_bool):
            print("FizzBuzz")
        elif (three_bool):
            print("Fizz")
        elif (five_bool):
            print("Buzz")
        else:
            print(i)
        i+=1

print(fizzBuzz(15))