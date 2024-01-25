from src.args_parser import ArgsParser


PROG_NAME = 'TurboGaser'


if __name__ == '__main__':
    args_parser = ArgsParser(PROG_NAME)
    args = args_parser.run()
