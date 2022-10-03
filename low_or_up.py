"""This code returns the percentage of capital letters in a string."""


def loworup(text: str) -> str:
    """This code returns the percentage of capital letters in a string.

    Args:
        text(str): str - some text
    """
    upper = 0
    procent = text.split()
    for subtext in procent:
        if sum(map(str.isupper, list(subtext))) > sum(map(str.islower, list(subtext))):
            upper += 1
    return "{0}%".format(int(upper / len(text.split()) * 100))
