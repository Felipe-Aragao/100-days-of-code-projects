from operations import add, subtract, multiply, divide

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def main():
    num1 = float(input('First number: '))
    should_continue = True
    while should_continue:
        for i in operations:
            print(f'{i}  ', end=' ')
        operation_symbol = input('\nOperation: ')
        num2 = float(input('Next number: '))

        operation_choice = operations[operation_symbol]
        answer = operation_choice(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answer:.2f}')
        num1 = answer
        continue_option = input('Do you want to continue?(Y/N)').lower()
        if continue_option == 'y':
            continue
        elif continue_option == 'n':
            restart_option = input('Do you want to restart?(Y/N)').lower()
            if restart_option == 'y':
                main()
            else:
                break
        else:
            should_continue = False


main()
