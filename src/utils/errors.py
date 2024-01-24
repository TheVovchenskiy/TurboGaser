from termcolor import colored


def print_error(error_msg: str):
    print(colored(f'Error: {error_msg}', 'red'))
