# BookBot

BookBot is a command-line application that analyzes text files and generates statistical reports about their content. This is my first [Boot.dev](https://www.boot.dev) project!

## Overview

BookBot reads a book or text file and provides detailed analysis including:
- Total word count
- Character frequency distribution (alphabetic characters only)
- Characters sorted by frequency in descending order

## Project Structure

```
BuildABookbotInPython/
├── main.py              # Main entry point for the application
├── stats.py             # Statistical analysis functions
├── README.md            # Project documentation
├── books/               # Directory containing sample text files
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
└── __pycache__/         # Python cache directory
```

## Features

- **Word Count Analysis**: Counts the total number of words in the provided text
- **Character Frequency Analysis**: Counts occurrences of each alphabetic character (case-insensitive)
- **Sorted Results**: Displays characters sorted by frequency from highest to lowest
- **Command-line Interface**: Easy-to-use CLI for analyzing any text file

## Installation

No external dependencies are required. This project uses only Python's standard library.

### Requirements
- Python 3.x

## Usage

Run the program with a path to a text file:

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

### Output

The program displays a formatted report:

```
============ BOOKBOT ============
Analyzing book found at <path>...
----------- Word Count ----------
Found <count> total words
--------- Character Count -------
<character>: <count>
<character>: <count>
...
============= END ===============
```

## How It Works

### main.py
- Accepts a file path as a command-line argument
- Reads the entire text from the file using `get_book_text()`
- Calls statistical functions from `stats.py`
- Formats and displays the results

### stats.py
- **get_num_words(text)**: Splits the text by whitespace and counts words
- **get_num_characters(text)**: Counts the frequency of each character (case-insensitive)
- **get_sorted_list_of_dicts(dicts_char_count)**: Converts the character count dictionary to a list of dictionaries and sorts by frequency in descending order
- **sort_on(items)**: Helper function used as the sorting key

## Sample Books

The project includes three classic books for testing:
- **frankenstein.txt** - Frankenstein by Mary Shelley
- **mobydick.txt** - Moby-Dick by Herman Melville
- **prideandprejudice.txt** - Pride and Prejudice by Jane Austen
