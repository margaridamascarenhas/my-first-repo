def greet(name):
    return f"Hello, {name}! Welcome to the lab."

def farewell(name):
    return f"Goodbye, {name}, see you next time!"

def shout(name):
    return f"HELLO {name.upper()}!!!"

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
    print(shout("World"))
