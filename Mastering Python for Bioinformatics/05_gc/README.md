# Finding GC Content in Sequences

http://rosalind.info/problems/gc/

Write a Python program called `cgc.py` that takes a single positional argument which should be a readable text file.

The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./cgc.py -h
usage: cgc.py [-h] FILE

Compute GC content

positional arguments:
  FILE        Input sequence file

optional arguments:
  -h, --help  show this help message and exit
```

The input file will be in FASTA format:

```
$ cat tests/inputs/1.fa
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
```

The output should be the sequence ID with the highest GC content along with that GC content as a floating-point value to 6 significant digits:

```
$ ./cgc.py tests/inputs/1.fa
Rosalind_0808 60.919540
```

To test:

```
pytest -xv
```


