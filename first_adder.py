def adder(x, y):
    """Add two numbers together."""
    print("INSIDE ADDER!")
    return x + y


assert adder(2, 5) == 7
assert adder(2, 7) == 10, "expected 2+7 to be 10"
assert adder(2, 3) == 5
# dont want to add parenthesis when passing 2 statements.. its a staement not function
print("HELLO WORLD!")

#stops execution once it hits error... 2 prints even though we called assertion 3x
# not a great way to get comprehensive tests... it stops exectution
# 2nd reason: dont get a log or test report.. ex #of fails and passes and expected values
# not that commmonly used. built in python function

#on regular python if you use following cmd to run "optimized" code it removes asserts and will print hello statement
# "python -O first_adder.py" 