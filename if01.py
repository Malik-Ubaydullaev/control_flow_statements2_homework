def main(a,b,c):
    m = 0
    if a > b:
        if a > c:
            m = a
        else:
            m = c
    else:
        if b > c:
            m = b
        else:
            m = c
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    return m