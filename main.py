import argparse

from parse import parse_dir
from printer import print_html


def main():
    parser = argparse.ArgumentParser(description='verilog hierarchy printer')
    parser.add_argument('path', help='rtl directory')
    parser.add_argument('--top', help='top module name')
    parser.add_argument('--output', help='output file. stdout if not defined')

    args = parser.parse_args()
    modules = parse_dir(args.path)
    html = print_html(modules, args.top)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(html)
            f.close()
    else:
        print(html)
    pass


if __name__ == '__main__':
    main()
