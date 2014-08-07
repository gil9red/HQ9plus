"""\
EN:
Interpreter language HQ9+.
HQ9+ is a joke programming language. It has four "operations":
    H: print "Hello, world!"
    Q: print the program's source code (sometimes called a quine)
    9: print the lyrics to 99 Bottles of Beer
    +: add one to the accumulator (the value of the accumulator cannot be accessed)

RU:
Интерпрететаор языка HQ9+.
Команды:
    Команда «H» выводит сообщение «Hello, world!»;
    Команда «Q» выводит исходный код программы, которая выполняется (то есть, куайн);
    Команда «9» выводит слова стихотворения 99 Bottles of Beer on the Wall;
    Команда «+» увеличивает на единицу (инкрементирует) счетчик, который больше никак нельзя использовать.
"""

import argparse
import sys

__author__ = 'ipetrash'


def execute(source):
    """
    EN:
    The function parses source code HQ9+ and execute it.

    RU:
    Функция выполняет разбор исходного кода HQ9+ и выполняет его.

    :param source: Исходный код
    :return:
    """

    counter = 0
    template = ("%d bottles of beer on the wall\n"
                "%d bottles of beer!\n"
                "Take one down, pass it around\n"
                "%d bottles of beer on the wall!\n")

    for s in source.upper():  # EN: To ignore case; RU: Для игнорирования регистра;
        if s is "H":
            print("Hello, world!")
        elif s is "Q":
            print(source)
        elif s is "9":
            for i in range(99, 1, -1):
                print(template % (i, i, i-1))
        elif s is "+":
            counter += 1


def create_parser():
    parser = argparse.ArgumentParser(description='Interpreter language HQ9+.')
    parser.add_argument("path", help="Path to file")
    return parser


if __name__ == '__main__':
    parser = create_parser()

    if len(sys.argv) is 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        file_name = args.path
        source = open(file_name).read()
        execute(source)