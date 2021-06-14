import os 
import sys

input_path = '/BiO/Research/WES/0.RawData/'
output_path = '/BiO/Research/WES/1.Cleandata/'

file_list = os.listdir(input_path)
file_list.sort()

for i in range(0,len(file_list),2):
    name = file_list[i].split('_')
    n1 = name[1]+'-trimmed_1.fq.gz'
    n2 = name[1]+'-trimmed_2.fq.gz'
    n3 = name[1]+'-trimmed_3.fq.gz'

    #print('sickle pe -t sanger -g -f {0} {1} -o {2} {3} -s {4}'.format(input_path+file_list[i],input_path+file_list[i+1],output_path+n1,output_path+n2,output_path+n3))
    os.system('sickle pe -t sanger -g -f {0} -r {1} -o {2} -p {3} -s {4}'.format(input_path+file_list[i],input_path+file_list[i+1],output_path+n1,output_path+n2,output_path+n3))

