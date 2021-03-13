print("MathHomewor.py")

# Ask the user to enter a math problem
problem = input ("Enter a math problem,or 'c' to quit: ")
# Keep going until the user enters 'c' to quit
while (problem !="c"):
    # Show the problem, and the answer using eval()
    print("The answer to ", problem, "is:",eval(problem) )
    # Ask for another math problem
    problem = input("Enter another math problem,or 'c' to quit: ")
    # This while loop will kepp going until you enter 'c' to quit