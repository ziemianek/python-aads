"""

Recursion is a way of solving a problem by having a function calling itself
    -- performing the same operation multiple times with different inputs
    -- in every step we try smaller inputs to make the problem smaller
    -- base condition is needed to stop the recursion, otherwise infinite loop will occur

"""

# basic example using russian doll:
def open_russian_doll(doll):
    if doll == 1:
        return "All dolls are opened"
    else:
        open_russian_doll(doll - 1)
