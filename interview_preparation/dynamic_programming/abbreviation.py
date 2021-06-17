# You can perform the following operations on the string, a:

# Capitalize zero or more of a's lowercase letters.
# Delete all of the remaining lowercase letters in a.
# Given two strings, a and n, determine if it's possible to make a equal to b as described. If so, print YES on a new line. Otherwise, print NO.

def abbreviation(a, b):
    # Write your code here


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)
