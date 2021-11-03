import funpy

def executor(f):
    print("Before!")
    print("Result: ", f())
    print("After!")

@funpy.executeWith(executor)
def add(a, b):
    return a + b

add(10, 20)