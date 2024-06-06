import os
import argparse
import pyfastx
#############################################################################
#Author：chirrupe 
#Describtion: Pseudo_shortgun.py is a mulit processes tool for make wanted length fragments from a fasta file.
#Version: V1.0
#Data: 2021/10/19
#Example: python Pseudo_shortgun.py -input input.fasta -l 150 -output output.fasta
#############################################################################

parser=argparse.ArgumentParser(description='Pseudo_shortgun.py is a mulit processes tool for make wanted length fragments from a fasta file')
parser.add_argument('-input',type=str,help='Input your fasta file',required=True)
parser.add_argument('-output',type=str,help='Input your output fasta file',required=True)
parser.add_argument('-l',type=int,help='Input the fragment's length',required=True)
args=parser.parse_args()



input_file = args.input
length = args.l
output_file = args.output

fa = pyfastx.Fasta(input_file)
with open(output_file, 'w') as output:
	for seq in fa:
		seq_length=len(seq.seq)
		if seq_length > length:
			for seq_end in range(length,seq_length,length):
				if seq_length-seq_end>=length:
					seq_start = seq_end-length
				elif seq_length-seq_end<length:
					seq_start = seq_length-length
					seq_end = seq_length
				fraction_seq = seq.seq[seq_start:seq_end]
				fraction_name = f'>{seq.name} {seq_start}-{seq_end}'
				output.write(f'{fraction_name}\n')
				output.write(f'{fraction_seq}\n')
		else:
			print(f"the sequence {seq.name} is shorter than the fragment's setting\n")
			print(f"passed\n")
print('Done !')
			
