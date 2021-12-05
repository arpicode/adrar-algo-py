import math
from typing import Union

COLOR_LIGHT_GREEN = '\033[92m'
COLOR_LIGHT_MAGENTA = '\033[95m'
COLOR_LIGHT_CYAN = '\033[96m'
COLOR_END = '\033[0m'
BOLD = '\033[1m'
MSG_ERROR = '\033[30m\033[41m ERROR \033[0m'
MSG_WARNING = '\033[30m\033[43m WARNING \033[0m'

OPERATIONS = {
    '+': 'Addition',
    '-': 'Soustraction',
    '*': 'Multiplication',
    '/': 'Division'
}


def display_menu() -> None:
    print(f'{COLOR_LIGHT_CYAN}Choisir une opération :{COLOR_END}\n')

    for key in OPERATIONS:
        print(f'\t{BOLD}{key}{COLOR_END} → {OPERATIONS[key]}.')

    print(f'\n\t{COLOR_LIGHT_MAGENTA}Entrez 0 pour quitter.\n{COLOR_END}')


def ask_for_operation() -> Union[str, bool]:
    operation = input(f'\t{COLOR_LIGHT_CYAN}Opération ?{COLOR_END} ')

    if OPERATIONS.get(operation, False) or operation == '0':
        return operation

    return False


def ask_for_values(num_values: int = 2) -> list[float]:
    values = []
    i = 0

    while i < num_values:
        try:
            values.append(float(input(f'Entrez la valeur n°{i + 1} : ')))
            i += 1
        except:
            print(f'{MSG_WARNING} Vous devez saisir un nombre valide !{COLOR_END}\n')

    return values


def get_result(op: str, val: list) -> float:
    if op == '+':
        return add(val[0], val[1])
    elif op == '-':
        return substract(val[0], val[1])
    elif op == '*':
        return multiply(val[0], val[1])
    elif op == '/':
        return divide(val[0], val[1])


def add(a: float, b: float) -> float:
    return a + b


def substract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        print(f'{MSG_ERROR} Division par 0 !{COLOR_END}')
        if a == 0:
            result = 0
        else:
            result = a * math.inf
    else:
        result = a / b

    return result


if __name__ == '__main__':
    while True:
        display_menu()
        operation = ask_for_operation()
        if operation == '0':
            break

        if (operation != False):
            print()
            values = ask_for_values()
            print()
            print(f'{COLOR_LIGHT_GREEN}{get_result(operation, values)}')
        else:
            print(f'\n{MSG_ERROR} Opération inconnue !')
        print(COLOR_END)
