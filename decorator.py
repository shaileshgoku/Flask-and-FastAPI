def hello(func):
    def greet(*args, **kwargs):
        print("start the execution")

        sum_value=func(*args, **kwargs)

        print("end the execution")

        return sum_value
    return greet


@hello    # decorator which will call hello function and pass the sum function as a parameter inside hello function
def sum(a, b):
    print("I am inside sum function")
    return str(a + b)

a, b = 3, 6

print(sum(a, b))