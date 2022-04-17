import argparse
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:

    parser = argparse.ArgumentParser()
    parser.add_argument('dir')
    args = parser.parse_args(argv)

    print(args)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
