def main(n):
    digit1 = n % 10
    n //= 10
    answer = digit1
    
    digit2 = n % 10
    n //= 10
    if digit2 > answer:
        answer = digit2
    
    digit3 = n % 10
    n //= 10
    if digit3 > answer:
        answer = digit3
    
    digit4 = n % 10
    n //= 10
    if digit4 > answer:
        answer = digit4
    
    digit5 = n % 10
    if digit5 > answer:
        answer = digit5
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    return answer