# hello.py
def greet():
    print("Hello DevOps!")

def farewell():
    print("Goodbye, DevOps!")

def add_number(a, b):
    return a + b

if __name__ == '__main__':
    greet()
    farewell()
    result = add_number(5, 7)
    print(f"The sum of 5 and 7 is {result}")