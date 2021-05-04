from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    string = Counter(s)
    string = Counter(string.values())
    
    if len(string.keys()) == 1:
        return 'YES'
    elif len(string.keys()) == 2:
        key1, key2 = string.keys()
        if string[key1] == 1 and (key1 - 1 == key2 or key1 == 1): return 'YES'
        elif string[key2] == 1 and (key2 - 1 == key1 or key2 == 1): return 'YES'
        else: return 'NO'
    else: 
        return 'NO'
    
    
if __name__ == '__main__':

    s = input()

    result = isValid(s)