def main(a,b):
    answer = 0
    if a == b:
        answer = 0
    elif a > b:
        answer = a
    else:
        answer = b
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    return answer
        