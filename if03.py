def main(a,b,c):
    answer = 0
    if a >= b:
        if a <= c:
            answer = a
        elif b >= c:
            answer = b
        else:
            answer = c
    elif b >= a:
        if b <= c:
            answer = b
        elif a >= c:
            answer = a
        else:
            answer = c
     
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    return answer