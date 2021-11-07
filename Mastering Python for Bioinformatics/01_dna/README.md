# Counting tetranucleotide frequency

http://rosalind.info/problems/dna/

Create a program called `dna.py` that will accept a sequence of DNA as a single positional argument.
The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./dna.py -h
usage: dna.py [-h] DNA

Tetranucleotide frequency

positional arguments:
  DNA         Input DNA sequence

optional arguments:
  -h, --help  show this help message and exit
```

The program should print the frequencies of the bases A, C, G, and T:

```
$ ./dna.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
20 12 17 21
```

To test:

```
pytest -xv
```

