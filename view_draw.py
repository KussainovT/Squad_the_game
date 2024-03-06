import os
import textwrap

black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magenta = '\033[35m'
cyan = '\033[36m'
white = '\033[37m'
reset = '\033[0m'


class Draw:
    def __init__(self):
        self.width = 60
        self.text_width = self.width - 4 - 5

    # TITLE
    def title(self, title, color):
        self.line()
        print(f"|   {color}{title.upper()}{reset}{' ' * (self.width - 5 - len(title))}|")
        self.line()
        self.br()

    # TITLE SHELTER
    def title_shelter(self, title, money):
        self.line()
        print(
            f"|   {yellow}ЧВК {title.upper()}{reset}{' ' * (self.width - 8 - len(title) - len(str(money)) - 4)}{green}${money}{reset}  |")
        self.line()
        self.br()

    # POINT LIST
    def point_list(self, mylist: list = [], title: str = '', is_titled: bool = False, point_symbol: str = ' ', divider_symbol: str = ''):
        if is_titled:
            print(title)
        for item in mylist:
            if isinstance(item, tuple):
                print(f"  {point_symbol} ", end='')
                for i, el in enumerate(item, start=1):
                    if i == len(item):
                        print(f"{el}")
                    else:
                        print(f"{el}{divider_symbol}", end='')
            else:
                print(f"  {point_symbol} {item}")

    # WRAPPED TEXT
    def p_wrapped(self, text):
        wrapped_text = textwrap.wrap(text, self.text_width)
        for line in wrapped_text:
            print(f"    {line}")

    def line(self):
        print(f"+{'-' * (self.width - 2)}+")

    def br(self):
        print()

    @staticmethod
    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')
