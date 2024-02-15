print('hello world')
# hello.py

import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide the value of x as a command-line argument.")
        sys.exit(1)
        
    x = int(sys.argv[1])
    print(f"x is {x}")

if __name__ == "__main__":
    main()

