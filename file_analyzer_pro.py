#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File Analyzer Pro - A versatile command-line utility for analyzing text files

This program provides functionality to analyze text files by counting lines,
words, characters, and generating statistical information. It supports multiple
files, directory recursion, different output formats, and more.

Author: Andre McKenzie
Version: 1.0
"""

import argparse, os, sys
import json
import csv
import glob
from datetime import datetime


def analyze_file(filename, modes, verbose, encoding=None):
    """
        Analyze a text file based on specified modes.

        Args:
            filename (str): Path to the file to analyze
            modes (list): List of analysis modes (lines, words, chars, stats, all)
            verbose (bool): Whether to display verbose output
            encoding (str, optional): File encoding. Defaults to UTF-8.

        Returns:
            dict: Dictionary with filename as key and analysis results as value,
                  or None if file cannot be read
    """

    # Check if file exists
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        return None
    try:
        # Try to detect encoding if not specified
        # Set default encoding if not specified
        if not encoding:
            encoding = 'utf-8'

        # Open and read the file
        with open(filename, 'r', encoding=encoding) as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None

    # Print verbose information if enabled
    if verbose:
        print(f"Analyzing '{filename}' in {', '.join(modes)} modes(s)...")

    # Initialize results dictionary
    results = {}

    # Line count analysis
    if 'lines' in modes or 'all' in modes:
        results['lines'] = content.count('\n') + 1 # +1 for the last line without newline

    # Word count analysis
    if 'words' in modes or 'all' in modes:
        results['words'] = len(content.split())

    # Character count analysis
    if 'chars' in modes or 'all' in modes:
        results['chars'] = len(content)

    # Statistical analysis
    if 'stats' in modes:
        lines = content.splitlines()
        words = content.split()

        # Store statistics in results
        results['stats'] = {
            # Calculate average line length with protection against division by zero
            'avg_line_length': sum(len(line) for line in lines) / max(len(lines), 1),
            # Calculate average word length with protection against division by zero
            'avg_words_length': sum(len(word) for word in words) / max(len(words), 1),
            # Count empty lines
            'empty_lines': sum(1 for line in lines if not line.strip())
        }

    # Return results with filename as the key
    return {filename: results}

def formatted_output(results, format_type):
    """
        Format analysis results based on specified format type.

        Args:
            results (dict): Analysis results dictionary
            format_type (str): Output format type (text, json, csv)

        Returns:
            str: Formatted output string
    """

    # JSON format
    if format_type == 'json':
        return json.dumps(results, indent=2)
    elif format_type == 'csv': # CSV format
        output = []
        header = ['filename', 'lines', 'words', 'chars']
        output.append(','.join(header))
        for filename, data in results.items(): # Add a row for each analyzed file
            row = [filename]
            for item in header[1:]:
                row.append(str(data.get(item, '')))
            output.append(','.join(row))
        return '\n'.join(output)
    else: # Text format (default)
        output = []
        # Format each file's results
        for filename, data in results.items():
            output.append(f"Results for '{filename}':")
            for key, value in data.items():
                if isinstance(value, dict): # Handle nested dictionaries (stats)
                    output.append(f" {key.capitalize()}:")
                    for stat_key, stat_value in value.items():
                        output.append(f"    {stat_key}: {stat_value:.2f}")
                else:
                    output.append(f"  {key.capitalize()}: {value}")
        return '\n'.join(output)


def main():
    """
    Main function to parse command-line arguments and execute file analysis.
    """
    # Initialize argument parser
    parser = argparse.ArgumentParser(
        description="Analyze text files and count lines, words, or characters."
    )

    # Define command-line arguments
    parser.add_argument("files", nargs='+', help="Path(s) to text file(s)")
    parser.add_argument(
        "--mode", choices=["lines", "words", "chars", "all", "stats"],
        default=["lines"], nargs='+',
        help="Types of analysis to perform (default: lines)"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output."
    )
    parser.add_argument(
        "-r", "--recursive", action="store_true",
        help="Recursively analyze directories."
    )
    parser.add_argument(
        "-f", "--format", choices=['text', "json", "csv"], default='text',
        help="Output format (default: text)"
    )
    parser.add_argument(
        "-o", "--output", help="Save results to a file"
    )
    parser.add_argument(
        "--encoding", help="Specify file encoding"
    )
    parser.add_argument(
        "--ext", help="Filter by file extension (e.g., .txt"
    )

    # Parse command-line arguments
    args = parser.parse_args()

    # Handle file patterns and directory recursion
    all_files = []

    # Process each file or directory pattern
    for file_pattern in args.files:
        if os.path.isdir(file_pattern) and args.recursive:
            # Recursively walk the directory
            for root, _, files in os.walk(file_pattern):
                for file in files:
                    # Filter by extension if specified
                    if args.ext and not file.endswith(args.ext):
                        continue
                    all_files.append(os.path.join(root, file))
        else:
            # Handle glob pattern (wildcards)
            matched_files = glob.glob(file_pattern, recursive=args.recursive)
            # Filter by extension if specified
            if args.ext:
                matched_files = [f for f in matched_files if f.endswith(args.ext)]
            all_files.extend(matched_files)

    # Remove duplicates
    all_files = list(set(all_files))
    # Check if any files were found
    if not all_files:
        print("Error: No matching files found.")
        return
    # Analyze each file and collect results
    all_results = {}
    for file in all_files:
        result = analyze_file(file, args.mode, args.verbose, args.encoding)
        if result:
            all_results.update(result)

    # Format the output according to specified format
    formated_output = formatted_output(all_results, args.format)

    # Save to output file or print to console
    if args.output:
        try:
            # Write results to specified output file
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(formated_output)
            print(f"Results saved to '{args.output}'")
        except Exception as e:
            # Handle errors when writing to output file
            print(f"Error saving results: {e}")
            print(formated_output)
    else:
        # Print output to console
        print(formated_output)


if __name__ == "__main__":
    main()


