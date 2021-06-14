import os, configparser, sys
import pandas as pd 
from glob import glob

arg1 = sys.argv[1]

config = configparser.ConfigParser()
config.read('Pipeline.config')

(forwd,reverse) = (config.get("MGI_Adapter",'forward'),config.get('MGI_Adapter','reverse'))

(inp,outp) = (config.get('PATH','INPUT')+arg1,config.get('PATH','OUTPUT')+arg1)

file_list = glob('%s/*.fastq'%inp)+glob('%s/*.fq'%inp)+glob('%s/*.fastq.gz'%inp)+glob('%s/*.fq.gz'%inp)
file_list.sort()

for fq in range(0,len(file_list),2):
    sample_name = fq.split('/')[-1].rstrip('.fq').rstrip('.fq.gz').rstrip('.fastq').rstrip('.fastq.gz')
    read_1 = file_list[fq]
    read_2 = file_list[fq+1]
    cmd = 'cutadapt -a %s -A %s -q 5 -m 30 -o %s %s %s %s'%()
print(file_list)


