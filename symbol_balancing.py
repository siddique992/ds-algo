
def isValid(string):
    if len(string) % 2 == 1:
        return False
    if string[0] in ')}]':
        return False
    brackets = []
    d = {')': '(', '}': '{', ']': '['}
    for bracket in string:
        if bracket in '({[':
            brackets.append(bracket)
        elif bracket in ')}]':
            if d[bracket] == brackets[-1]:
                brackets.pop()
            else:
                 return False
    return True


if __name__ == '__main__':
    line = input('Enter brackets: ')
    if isValid(line):
        print('Balanced Brackets.')
    else:
        print('Brackets not balanced.')
