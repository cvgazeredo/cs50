import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Incorrect usage of command-line")

    # TODO: Read database file into a variable
    database = open(sys.argv[1])
    data = csv.DictReader(database)
    with open(sys.argv[2]) as f:
        sequence = f.read()
    #print(sequence)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as dna_file:
        reader_dna = csv.reader(dna_file)
        for row in reader_dna:
            subsequence = row
    #print(subsequence)

    # TODO: Find longest match of each STR in DNA sequence
    counts = {}
    for subsequence in data.fieldnames[1:]:
        counts[subsequence] = longest_match(sequence, subsequence)
    #print(counts)

    # TODO: Check database for matching profiles
    for row in data:
            if all(counts[subsequence] == int(row[subsequence]) for subsequence in counts):
                print(row['name'])
                database.close()
                return

    print("No match")
    database.close()

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
