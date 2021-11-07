# Transcribing DNA into RNA

http://rosalind.info/problems/rna/

Write a program called `rna.py` that will accepts one or more files, each containing a sequence of DNA on each line and the name of an output directory.
The sequences in each file will be transcribed to RNA in output file located in the output directory.

The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./rna.py -h
usage: rna.py [-h] [-o DIR] FILE [FILE ...]

Transcribe DNA into RNA

positional arguments:
  FILE                  Input DNA file

optional arguments:
  -h, --help            show this help message and exit
  -o DIR, --outdir DIR  Output directory (default: out)
```

The input files should look like this:

```
$ cat tests/inputs/input1.txt
GATGGAACTTGACTACGTAAATT
```

The default output directory is "out."
Note how all the input files are processed into the output directory and the STDOUT from the program summarizes the actions:

```
$ ./rna.py tests/inputs/*
Done, wrote 5 sequences in 3 files to directory "out".
```

And the output should look like this:

```
$ head -c 20 out/*
==> out/input1.txt <==
GAUGGAACUUGACUACGUAA
==> out/input2.txt <==
UUAGCCCAGACUAGGACUUU
==> out/input3.txt <==
CUUAGGUCAGUGGUCUCUAA
```

To test:

```
pytest -xv
```

