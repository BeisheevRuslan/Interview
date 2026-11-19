from stack import Stack

brackets = {')': '(', ']': '[', '}': '{'}


def check_brackets(string):
    a = Stack()
    for i in string:
        if i in '([{':
            a.push(i)
        elif i in brackets:
            if a.is_empty():
                return 'Несбалансировано'
            else:
                if a.pop() != brackets[i]:
                    return 'Несбалансировано'
    if a.is_empty():
        return 'Сбалансировано'
    else:
        return 'Несбалансировано'
