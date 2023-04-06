from stack.stack import Stack


def multi_bracket_validation(list_of_char):
    stack = Stack()
    brackets_dict = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    for char in list_of_char:
        print(char)
        if char in brackets_dict.keys():
            stack.push(char)
        if char in brackets_dict.values():
            if stack.top:
                if brackets_dict[stack.top.value] == char:
                    stack.pop()
                else:
                    return False
            else:
                return False
    return True


if __name__ == '__main__':
    pass



