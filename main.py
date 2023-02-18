print("Hello Sanger")

import gzip
import pyfastx

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


