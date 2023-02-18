print("Hello Sanger")

import gzip
import pyfastx

#function to calculate how many sequences(reads) in one fastq.gz file 

def get_seq_count():
    reads=0
    with gzip .open('./data/test.fastq.gz' ,'rb' ) as read:
        for id in read:
            seq = next(read)
            reads +=1
            next(read)
            next(read)
    print(reads)

get_seq_count()


