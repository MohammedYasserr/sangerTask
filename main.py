print("Hello, Sanger!")

import gzip

#function to calculate how many sequences(reads) in one fastq.gz file 
def get_seq_count():
    sequences = 0
    with gzip .open('./data/test.fastq.gz' ,'rb' ) as sequence:
        for id in sequence:
            seq = next(sequence)
            sequences +=1
            next(sequence)
            next(sequence)
    print(sequences)

get_seq_count()


# function to calculate how many nucleotides in one fastq.gz file
def get_nucleotides_count():
    bases = 0
    with gzip .open('./data/test.fastq.gz', 'rb') as read:
        for id in read:
            seq = next(read)
            bases += len(seq.strip())
            next(read)
            next(read)
    print(bases)


get_nucleotides_count()


print("See you, Sanger!")