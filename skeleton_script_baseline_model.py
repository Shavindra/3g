#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Description:
    Baseline impact predictor of SNPs in VEP format.
    Uses raw BLOSUM62 matrix from a text file for scoring.
"""

import argparse
import sys
import os


def parse_args():
    """
        Parses inputs from the commandline.
        :return: inputs as a Namespace object
    """

    parser = argparse.ArgumentParser(description='Generates baseline model predictions.')
    # Arguments
    parser.add_argument('vep', help='a path to the VEP input file')
    parser.add_argument('blosum', help='a path to the BLOSUM62 input file')
    parser.add_argument('-o', dest='out_path', help='a path to write the output .tsv file with baseline model scores. '
                                                    'This arguments is required!', required=True)

    return parser.parse_args()

def parse_blosum(path):
    """
        Reads BLOSUM62 matrix file and stores in a 2-dimensional dictionary.
        :param path: a str with the BLOSUM62 substitution matrix file path
        :return: a 2-dimensional dict with amino acid (AA) substitution scores
    """

    aas = []
    aa_scores = []
    with open(path, "rb") as f:
        for line in f:
            # Convert bytes to str
            line = line.decode('UTF-8')
            # Skip headers
            if line.startswith('#') or line.startswith('x'):
                continue
            # Store AAs and scores (matrix is symmetric)
            else:
                aas.append(line.strip('\n').split()[0])
                aa_scores.append(line.strip('\n').split()[1:len(line)])

    # Create a 2-dimensional dictionary with AAs as keys and empty dictionaries as values
    blosum_dict = {}
    for aa in aas:
        blosum_dict[aa] = {}

    #########################
    ### START CODING HERE ###
    #########################
    # You need to fill in the dictionaries in blosum_dict for each key AA (amino acid) with the corresponding
    # substitution scores between that AA and any other AA.
    # Use aas list to loop over all amino acids:
    # for i in range(len(aas)):
        # Now loop over each score position for the AA with position i which are stored in the i-th list of aa_scores.
        # These are the BLOSUM62 scores between the AA with position i and the AA with position j:
        # for j in range(...):
            # Get the score between the AA with position i and the AA with position j from aa_scores:
            # score = ...

            # For the dictionary of the i-th AA key of blosum_dict, store the j-th AA as a key and the score as a value:
            # blosum_dict... = ...

    #########################
    ###  END CODING HERE  ###
    #########################

    return blosum_dict
