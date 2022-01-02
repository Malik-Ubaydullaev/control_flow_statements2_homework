def main(n):
    digit1 = n % 10
    n //= 10
    answer = 1
    maxi = digit1
    
    digit2 = n % 10
    n //= 10
    if digit2 > maxi:
        answer = 2
        maxi = digit2
    
    digit3 = n % 10
    n //= 10
    if digit3 > maxi:
        answer = 3
        maxi = digit3
    
    digit4 = n % 10
    n //= 10
    if digit4 > maxi:
        answer = 4
        maxi = digit4
    
    digit5 = n % 10
    if digit5 > maxi:
        answer = 5
        
        
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    return answer