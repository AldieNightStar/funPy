# FunPy - functional extensions for python

## Limit calls: `limited(count)`
```py
import funpy

@funpy.limited(5)
def sayHello():
    print("hello!")

for i in range(32):
    sayHello() # Will be called 5 times. Other calls will be ignored

sayHello.count # How many call's remains
sayHello.reset() # Reset call's count
```

## Repeat: `repeat(count)`
```py
import funpy

@funpy.repeat(5)
def sayHi():
    print("Hi!")

sayHi()
```

## Twice Tuple Result: `tupleTwice`
```py
import funpy

@funpy.tupleTwice
def getAbc():
    return "abc"

print(getAbc()) # ('abc', 'abc')
```

## Each argument processor: `forEachArg`
* Each argument will be executed separately
```py
import funpy

@funpy.forEachArg
def p(text, n):
    # text - is an each argument
    # n    - is a current argument number
    print(f"{n}: {text}")

p("Hello!", "Hi!", "What's up")
# Output will be:
#    0: Hello!
#    1: Hi!
#    2: What's up
```

## Executor: `executeWith(executor)`
```py
import funpy

# This function is an executor(f).
# It will deside to call f() or will send it to somewhere else. For ex: new Thread
def executor(f):
    print("Before!")
    print("Result: ", f())
    print("After!")
    return 1000

# Will execute this function via executor(f) func
@funpy.executeWith(executor)
def add(a, b):
    return a + b

add(10, 20)
# Will print Before, Result, After and return 1000
```