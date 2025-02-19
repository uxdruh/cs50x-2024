# https://cs50.harvard.edu/x/2024/psets/6/dna/

import csv
from sys import argv, exit


def main():

    # TODO: Check for command-line usage
    if len(argv) != 3:
        print("Usage: python dna.py database.csv sequences.txt")
        exit(1)

    # TODO: Read database file into a variable
    STRs = []
    profiles = []

    with open(argv[1]) as csv_file:
        reader = csv.DictReader(csv_file)
        STRs = reader.fieldnames[1:]
        for row in reader:
            profiles.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(argv[2]) as seq_file:
        seq = seq_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    target = {}
    for STR in STRs:
        target[STR] = str(longest_match(seq, STR))

    # TODO: Check database for matching profiles
    for profile in profiles:
        match_count = 0

        for STR in STRs:
            if profile[STR] != target[STR]:
                break
            match_count += 1

        if match_count == len(STRs):
            print(profile["name"])
            exit(0)

    print("No match")
    exit(2)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
