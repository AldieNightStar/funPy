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

## Maybe: `Maybe(value)`
```py
import funpy

# Will get value or will raise the ValueError
d = funpy.Maybe(32).get_val()

# Will get value or will execute another getter
d = funpy.Maybe(32).orGet(lambda: 32).get_val()

# Will get value or another one if first one is None
d = funpy.Maybe(32).orElse(16)

# Process the value when it's present and get
d = funpy.Maybe(32).process(lambda val: print(val)).get_val()

# Map the value when it's present and get the value
d = funpy.Maybe(32).map(lambda n: n * 2).get_val()
```

## Random element: `get_random(elemms)`
```py
import funpy

# Will return random element from the list
elem = get_random([1, 2, 3])
```

## OneOf functions: `one_of(args, *funcs)`
```py
import funpy

# Call each function in a list with args and get the first non-None result
# arg1 - arguments
# argN - functions
elem = one_of([10, 20, 30], func1, func2, func3)
```