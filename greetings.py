def greet(name):
    return f"Hi there, {name}! Great to have you in the lab."

def farewell(name):
    return f"Goodbye, {name}, see you next time!"

def shout(name):
    return f"HELLO {name.upper()}!!!"

def thank_you(name):
    return f"Thank you, {name}, for coming to the lab!"

if __name__ == "__main__":
    print(greet("World"))
    print(farewell("World"))
    print(shout("World"))
    print(thank_you("World"))
