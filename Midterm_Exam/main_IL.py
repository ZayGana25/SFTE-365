# main.py

# Importing the greet function from the my_module module
from module_IL import question

def main():
    color = input("What is your favorite color? Type your answer here... ")
    question(color)

if __name__ == "__main__":
    main()