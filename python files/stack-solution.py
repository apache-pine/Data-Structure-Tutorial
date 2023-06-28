def reverse_string(string):
    stack = []

    # Push each character onto the stack
    for char in string:
        stack.append(char)

    # Create an empty string called reversed_string
    reversed_string = ""

    # Pop each character from the stack to get the reversed string
    while len(stack) > 0:
        reversed_string += stack.pop()

    # Return the reversed string
    return reversed_string


# Sample Test Cases (may not be comprehensive)
print("\n=========== PROBLEM TESTS ===========")
string = "Hello, world!"
reversed_string = reverse_string(string)
print(reversed_string)  # !dlrow ,olleH

string = "This is a stack in action!"
reversed_string = reverse_string(string)
print(reversed_string)  # !noitca ni kcats a si sihT
