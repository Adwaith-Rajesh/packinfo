import argparse
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:

    parser = argparse.ArgumentParser(prog='packinfo')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--file', '-f', help='Run %(prog)s on a file.')
    group.add_argument(
        '--dir', '-d', help='Run %(prog)s on all files in a dir / package.')
    parser.add_argument('--output-file', '-o',
                        help='Set the output file (JSON).')
    args = parser.parse_args(argv)

    print(args)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
