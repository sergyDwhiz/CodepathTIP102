from Stack import MyStack


def apply_operator(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2  # Assuming integer division for simplicity

def evaluate_post_fix(exp):
    stack = MyStack()

    for char in exp:
        if char.isdigit():
            # Push numbers in stack
            stack.push(int(char))
        else:
            # Operator encountered
            # Pop top two numbers from stack
            right = stack.pop()
            left = stack.pop()
            # Apply operator to operands and push result back to stack
            result = apply_operator(char, left, right)
            stack.push(result)
    # Final result is at the top of the stack
    return stack.pop()

