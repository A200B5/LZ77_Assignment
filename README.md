# LZ77 Data Compression

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-LZ77-orange)
![Type](https://img.shields.io/badge/Compression-Lossless-green)

A Python implementation of the **LZ77 lossless data compression algorithm**, developed as part of a Data Compression course assignment.

The project demonstrates the core concepts of LZ77, including the **Search Buffer**, **Look-Ahead Buffer**, **longest-match searching**, **LZ77 tag generation**, and **compression ratio calculation**.

---

## About the Project

LZ77 is a dictionary-based lossless compression algorithm that represents repeated sequences by referencing data that has already been processed.

Each encoded sequence is represented using the following tag:

```text
<Position, Length, Next Symbol>
```

Where:

- **Position** – The distance back in the Search Buffer where the matching sequence starts.
- **Length** – The number of characters in the matching sequence.
- **Next Symbol** – The character immediately following the matched sequence.

When no matching sequence is found, the algorithm generates:

```text
<0, 0, Next Symbol>
```

---

## How It Works

LZ77 uses a sliding window divided into two parts:

```text
+----------------------+----------------------+
|    Search Buffer     |   Look-Ahead Buffer  |
+----------------------+----------------------+
        Already                 Next
       processed              to process
```

For each step, the algorithm:

1. Searches the **Search Buffer** for the longest match.
2. Determines the **Position** of the match.
3. Determines the **Length** of the match.
4. Takes the **Next Symbol** following the match.
5. Generates an LZ77 tag.
6. Moves the window forward and continues until the input is completely processed.

---

## Features

- LZ77 lossless compression
- Search Buffer and Look-Ahead Buffer
- Longest-match searching
- LZ77 tag generation
- Compression size calculation
- Compression ratio calculation
- User input support
- Simple Python implementation

---

## Example

### Input

```text
aaaabbababbaaabbaaaaaaaaa
```

### LZ77 Tags

The input is represented using tags in the following format:

```text
<Position, Length, Next Symbol>
```

Example:

```text
<0, 0, "a">
<1, 1, "a">
<1, 1, "b">
...
```

The generated tags can then be used to calculate the compressed size and compression ratio.

---

## Compression Ratio

The compression ratio is calculated as:

```text
Compression Ratio = Compressed Size / Original Size × 100
```

For example:

```text
Original Size   = 200 bits
Compressed Size = 126 bits
```

Therefore:

```text
Compression Ratio = 126 / 200 × 100
                  = 63%
```

---

## Technologies

- **Python 3**
- **Visual Studio Code**

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/A200B5/LZ77_Assignment
```

### Navigate to the Project

```bash
cd LZ77
```

### Run the Program

```bash
python lz77.py
```

The program will ask the user to enter the string that should be compressed.

---

## Project Structure

```text
LZ77/
│
├── lz77.py
└── README.md
```

---

## Concepts Covered

- Lossless Data Compression
- Dictionary-Based Compression
- LZ77 Algorithm
- Sliding Window
- Search Buffer
- Look-Ahead Buffer
- Longest Match
- Position and Length Encoding
- Compression Ratio

---

## Team Members

- **Ahmed Bakr**
- **Ahmed Emad**
- **Mohamed Mahmoud**

---

## Course

**Data Compression**

This project was developed as part of a Data Compression course assignment.
