def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return s[-n:len(s)]
print(main('codeschooluz',3))
print(main('positive',1))
