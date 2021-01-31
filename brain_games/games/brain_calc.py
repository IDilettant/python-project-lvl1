#!/usr/bin/env python3
"""Calculate game."""
import operator
import random

DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    """Generate a mathematical expression with two random terms.

    Returns:
        Return mathematical expression (str)
    """
    # limit the random number to two-digits for the convenience of the player
    number_size_limiter = 99
    first_number = random.randint(1, number_size_limiter)
    second_number = random.randint(1, number_size_limiter)
    math_operation_sign = random.choice(('+', '-', '*'))
    return '{0} {1} {2}'.format(
        first_number,
        math_operation_sign,
        second_number,
    )


def calculate_correct_answer(question):
    """Calculate a question and return answer.

    Args:
        question (str): mathematical expression

    Returns:
        Return the result of evaluating a mathematical expression (str)
    """
    question = question.split()
    if question[1] == '+':
        expr_result = operator.add(
            int(question[0]),
            int(question[2]),
        )
    elif question[1] == '-':
        expr_result = operator.sub(
            int(question[0]),
            int(question[2]),
        )
    elif question[1] == '*':
        expr_result = operator.mul(
            int(question[0]),
            int(question[2]),
        )
    return str(expr_result)