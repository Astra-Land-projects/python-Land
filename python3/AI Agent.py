import ast
import operator
from datetime import datetime


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow
}


def calculator(expression):

    try:
        tree = ast.parse(
            expression,
            mode="eval"
        )

        return evaluate(tree.body)

    except Exception:
        return "Invalid expression."


def evaluate(node):

    if isinstance(
        node,
        ast.Constant
    ):
        if isinstance(
            node.value,
            (int, float)
        ):
            return node.value

    if isinstance(
        node,
        ast.BinOp
    ):
        left = evaluate(node.left)
        right = evaluate(node.right)

        operation = OPERATORS.get(
            type(node.op)
        )

        if operation is None:
            raise ValueError()

        return operation(
            left,
            right
        )

    raise ValueError()


def time_tool():
    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def agent(user_input):

    text = user_input.lower()

    if text.startswith("calculate "):

        expression = user_input[
            len("calculate "):
        ]

        result = calculator(
            expression
        )

        return f"Result: {result}"

    if "time" in text:

        return (
            f"Current time: "
            f"{time_tool()}"
        )

    return (
        "I don't have a tool for "
        "that request yet."
    )


print("===== AI AGENT =====")
print("Examples:")
print("calculate 10 + 20 * 3")
print("what is the time?")
print("Type exit to quit.")


while True:

    user = input("\nUser: ")

    if user.lower() == "exit":
        break

    print(
        "Agent:",
        agent(user)
    )