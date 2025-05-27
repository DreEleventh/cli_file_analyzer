import argparse
import os
import sys


def analyze_file(filename, mode, verbose):
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        return
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    result = None

    if verbose:
        print(f"Analyzing '{filename} in '{mode}' mode...")

    if mode == 'lines':
        result = content.count('\n') + 1
    elif mode == 'words':
        result = len(content.split())
    elif mode == 'chars':
        result = len(content)
    else:
        print(f"Error: Invalid mode '{mode}'")
        return

    print(f"{mode.capitalize()}: {result}")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a text file and count lines, words, or characters."
    )

    parser.add_argument("filename", help="Path to text file")
    parser.add_argument(
        "--mode", choices=["lines", "words", "chars"],  default="lines",
        help="Type if analysis to perform (default: lines)"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    args = parser.parse_args()
    analyze_file(args.filename, args.mode, args.verbose)


if __name__ == "__main__":
    main()