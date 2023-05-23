"""
This module contains a function to generate all permutations of a given string.
"""

WORD = "abcd"
START_INDEX = 0

def permute(string, start, result):
    """
    Recursively generates all permutations of a given string.

    Args:
        string (str): The string to permute.
        start (int): The starting index for permutation.
        result (List[str]): A list to store the permutations.

    Returns:
        None
    """
    if start >= len(string):
        result.append(''.join(string))
        return
    for j in range(start, len(string)):
        string[j], string[start] = string[start], string[j]
        permute(string, start + 1, result)
        string[j], string[start] = string[start], string[j]

RESULT = []
permute(list(WORD), START_INDEX, RESULT)
print(RESULT)
