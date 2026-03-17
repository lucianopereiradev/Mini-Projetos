import argparse
import os
import random
import string
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create random text files with short random names"
    )
    parser.add_argument(
        "count",
        type=int,
        help="Number of files to create"
    )
    parser.add_argument(
        "--dir",
        dest="directory",
        default=".",
        help="Directory in which to create files (default: current)"
    )
    parser.add_argument(
        "--length",
        type=int,
        default=8,
        help="Maximum length of the random name (excluding extension)"
    )
    parser.add_argument(
        "--prefix",
        default="",
        help="Optional prefix for generated filenames"
    )
    return parser.parse_args()


def random_name(length: int) -> str:
    choices = string.ascii_lowercase + string.digits
    return "".join(random.choice(choices) for _ in range(length))


def main():
    args = parse_args()
    dst_dir = os.path.abspath(args.directory)

    if not os.path.isdir(dst_dir):
        print(f"Error: '{dst_dir}' is not a directory.")
        sys.exit(1)

    created = []
    for i in range(args.count):
       
        maxrandom = max(1, args.length - len(args.prefix))
        name = args.prefix + random_name(maxrandom)
        path = os.path.join(dst_dir, name + ".txt")
       
        while os.path.exists(path):
            name = args.prefix + random_name(maxrandom)
            path = os.path.join(dst_dir, name + ".txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write("This is a randomly generated file.\n")
        created.append(path)
        print(f"Created {path}")

    print(f"\nSuccessfully created {len(created)} files in {dst_dir}.")


if __name__ == "__main__":
    main()
