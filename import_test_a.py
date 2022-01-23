import os

def function():
    print("The test_a file function is called.")

def main():
    print(os.listdir('/'))

# This print function will execute when this file will be imported somewhere else.
print(os.listdir('/'))