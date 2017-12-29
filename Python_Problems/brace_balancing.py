

def braces(strings):
    stack=[]
    print(strings)
    balance_flag=False
    pushChars,popChars='{[(','}])'
    for item in strings:
        for s in item:
            if s in pushChars:
                stack.append(s)
            elif s in popChars:
                if pushChars.index(stack.pop())==popChars.index(s):
                    balance_flag=True
                else:
                    balance_flag=False
                    break
        if balance_flag:
            print("Yes")
        else:
            print("No")
if __name__=='__main__':
    strings=['{}[]()','{[}]}']
    braces(strings)