from bracket_checker import check_brackets

if __name__ == '__main__':
    print('Введите строку со скобками: ')
    user_input = input()

    result = check_brackets(user_input)
    print(result)
