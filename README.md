# File Analyzer Pro
A versatile command-line utility for analyzing text files.

## Features
- Count lines, words, and characters in text files
- Generate statistical analysis (average line length, word length, empty lines)
- Process multiple files with wildcard patterns
- Recursively analyze directories
- Filter files by extension
- Multiple output formats (text, JSON, CSV)
- Save results to output file

## Installation
Clone the repository or download the script file:
``` 
git clone https://github.com/yourusername/file-analyzer-pro.git
cd file-analyzer-pro
```

## Usage
Basic usage:
```
python3 file_analyzer_pro.py [file(s)] [options]
```

## Options

- `--mode {lines,words,chars,all,stats}`: Specify analysis mode(s) (default: lines)
- `-v, --verbose`: Enable verbose output
- `-r, --recursive`: Recursively analyze directories
- `-f, --format {text,json,csv}`: Output format (default: text)
- `-o, --output FILE`: Save results to a file
- `--encoding ENCODING`: Specify file encoding
- `--ext EXTENSION`: Filter by file extension (e.g., .txt)

## Examples
Count words in a file:

```
python3 file_analyzer_pro.py document.txt --mode words
```

Analyze multiple files with different modes:

```
python3 file_analyzer_pro.py file1.txt file2.txt --mode words chars
```

Recursively analyze all Python files in a directory:

```
python3 file_analyzer_pro.py src/ -r --ext .py
```

Generate statistics in JSON format:

```
python3 file_analyzer_pro.py *.txt --mode stats -f json
```

Save results to a file:

```
python3 file_analyzer_pro.py logs/ -r --ext .log -o analysis.csv -f csv
```

## More Command Examples 
Here's a list of ways you can call your enhanced file analyzer program:

1. Basic usage with default settings (lines count):
   ```
   python3 file_analyzer_pro.py file.txt
   ```

2. Analyze a specific mode:
   ```
   python3 file_analyzer_pro.py file.txt --mode words
   python3 file_analyzer_pro.py file.txt --mode chars
   python3 file_analyzer_pro.py file.txt --mode lines
   python3 file_analyzer_pro.py file.txt --mode stats
   ```

3. Analyze with multiple modes:
   ```
   python3 file_analyzer_pro.py file.txt --mode words chars
   python3 file_analyzer_pro.py file.txt --mode lines words chars
   ```

4. Use the "all" mode to get all basic counts:
   ```
   python3 file_analyzer_pro.py file.txt --mode all
   ```

5. Enable verbose output:
   ```
   python3 file_analyzer_pro.py file.txt -v
   python3 file_analyzer_pro.py file.txt --verbose
   ```

6. Change output format:
   ```
   python3 file_analyzer_pro.py file.txt -f json
   python3 file_analyzer_pro.py file.txt -f csv
   python3 file_analyzer_pro.py file.txt --format json
   ```

7. Save output to a file:
   ```
   python3 file_analyzer_pro.py file.txt -o results.txt
   python3 file_analyzer_pro.py file.txt --output results.json -f json
   ```

8. Analyze multiple files:
   ```
   python3 file_analyzer_pro.py file1.txt file2.txt file3.txt
   ```

9. Use wildcards for multiple files:
   ```
   python3 file_analyzer_pro.py *.txt
   ```

10. Analyze files in a directory:
    ```
    python3 file_analyzer_pro.py directory/
    ```

11. Recursively analyze files in directories:
    ```
    python3 file_analyzer_pro.py directory/ -r
    python3 file_analyzer_pro.py directory/ --recursive
    ```

12. Filter by file extension:
    ```
    python3 file_analyzer_pro.py directory/ --ext .txt
    ```

13. Specify file encoding:
    ```
    python3 file_analyzer_pro.py file.txt --encoding utf-8
    python3 file_analyzer_pro.py file.txt --encoding latin-1
    ```

14. Combine multiple options:
    ```
    python3 file_analyzer_pro.py *.txt -v -f json -o results.json --mode all
    python3 file_analyzer_pro.py directory/ -r --ext .py --mode lines words -v
    ```

These examples showcase the flexibility of your enhanced file analyzer, allowing you to analyze text files in many different ways and formats.

## Requirements

Python 3.6+

License
