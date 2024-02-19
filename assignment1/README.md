# Bioinformatics Programming Projetcs (tools)

This repository contains three Python projects for molecular biology and bioinformatics tasks. Each program serves a specific function, and this README offers an introduction to each one.

## Project 1: `calc_daltons.py`

### Description
In `calc_daltons.py` we calculate the molecular weight of a given protein sequence. It takes a protein sequence as input and calculates the total molecular weight based on the average molecular weight per amino acid  which is provided as input.
For this code, I took reference from w3schools website, google search engine and stackover flow.

### How to Use
1. Run the program by executing `python calc_daltons.py` in your terminal.
2. Input the protein sequence when prompted.
3. Input the average molecular weight per amino acid (in daltons).
4. The program will display the length of the protein sequence and its average weight in kilodaltons (KDa).

## Project 2: `calc_number_amino_acids.py`

### Description
In `calc_number_amino_acids.py` we calculate DNA sequences. It calculates the number of amino acids encoded by a given DNA sequence and estimates the molecular weight of the resulting protein sequence. I used google search and used import sys in this particular program.

### How to Use
1. Run the program by executing `python calc_number_amino_acids.py` in your terminal.
2. Provide a name for the DNA sequence when prompted.
3. Enter the length of the DNA sequence which should be divisible by 3
4. The program will calculate and display the length of the DNA sequence, the number of decoded amino acids, and the estimated average weight of the protein sequence in KDa.

## Project 3: `dynamic_protocol.py`

### Description
In `dynamic_protocol.py` calculates the volumes of NaCl and MgCl2 stock solutions required to make a desired solution. It also provides a protocol for preparation. The user is prompted to input the final volume and concentrations of NaCl and MgCl2 to calculate the required volumes. For this program I took reference from protocol.py file. 

### How to Use
1. Run the program by executing `python dynamic_protocol.py` in your terminal.
2. Enter the final volume of the solution (in ml) and the concentrations of NaCl and MgCl2 stock solutions (in mM) when prompted.
3. The program will calculate and display the protocol for preparing the solution, including the volumes of NaCl, MgCl2, and water to be added.

These projects provide various bioinformatics tools for analyzing protein and DNA sequences and preparing chemical solutions.
