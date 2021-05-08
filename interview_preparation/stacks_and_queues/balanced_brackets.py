def isBalanced(s):
    # Write your code here
    stack = []
    open_brackets = '{[('
    close_brackets = '}])'
    
    for b in s:
        if b in open_brackets:
            stack.append(b)
        else:
            if stack and open_brackets.index(stack.pop()) == close_brackets.index(b):
                continue
            else:
                return 'NO'
    return 'NO' if stack else 'YES'
    
    
    
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        
        print(result)