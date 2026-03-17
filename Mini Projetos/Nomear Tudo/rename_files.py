import argparse
import os
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Batch rename files in a directory")
    parser.add_argument("folder", help="Path to the folder containing files to rename")
    parser.add_argument(
        "pattern",
        nargs="?",
        help="Filename pattern. Use {n} for a sequence number."
    )
    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Starting index for numbering (default: 1)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be renamed without actually performing changes"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    folder = os.path.abspath(args.folder)

    if not os.path.isdir(folder):
        print(f"Error: '{folder}' is not a directory.")
        sys.exit(1)

    pattern = args.pattern
    if not pattern:
        pattern = input("Enter the base pattern for new filenames (use {n} for numbers): ").strip()
        if not pattern:
            print("No pattern supplied, aborting.")
            sys.exit(1)

    if "{n}" not in pattern:
      
        import re

        match = re.match(r"^(.*?)(\d+)$", pattern)
        if match:
            base, digits = match.group(1), match.group(2)
            
            if args.start == 1:
                index = int(digits)
            pattern = base + "{n}"
        else:
            pattern = pattern + "_{n}"

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    files.sort()

    index = args.start
    for original in files:
        base, ext = os.path.splitext(original)
        new_name = pattern.format(n=index) + ext
        src = os.path.join(folder, original)
        dst = os.path.join(folder, new_name)
        if os.path.exists(dst):
            print(f"Skipping '{original}': target '{new_name}' already exists.")
        else:
            if args.dry_run:
                print(f"{original} -> {new_name}")
            else:
                os.rename(src, dst)
                print(f"Renamed '{original}' to '{new_name}'")
        index += 1


if __name__ == "__main__":
    main()
