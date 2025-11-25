def greet(name):
    return "Hello, " + name + "!"

def main():
    names = ["Alice", "Bob", "Eve"]
    for n in names:
        print(greet(n))

if __name__ == "__main__":
    main()