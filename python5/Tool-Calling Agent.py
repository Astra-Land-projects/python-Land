import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def calculator(expression):
    allowed = "0123456789+-*/(). "

    if not all(
        char in allowed
        for char in expression
    ):
        return "Invalid expression"

    return str(eval(expression))


while True:

    expression = input(
        "Calculate (exit): "
    )

    if expression == "exit":
        break

    print(
        calculator(expression)
    )