import numpy as np
import os
import math

AVG = np.array([0,0,0,0,0,0,0])
doc = open('out.txt','w')

K = 1 # number of objects
D = 9000 # number of disk thrown to the object surface
def read_dir(filedir, lable):
    # lable = 0 indicates calculating AVG
    # lable = 1 indicates calculating NUC
    if lable == 0:
        print("calculating AVG ....")
        avg = np.array([0,0,0,0,0,0,0])
        pathDir = os.listdir(filedir)
        for allDir in pathDir:
            child = os.path.join('%s\\%s' % (filedir, allDir))
            print(child)
            avg = avg + read_each_file(child,lable)
        return avg
    else:
        print("calculating NUC ....")
        cnt = np.array([0,0,0,0,0,0,0])
        pathDir = os.listdir(filedir)
        for allDir in pathDir:
            child = os.path.join('%s\\%s' % (filedir, allDir))
            print(child)
            tmp = read_each_file(child,lable)
            cnt = cnt + tmp
        std_dev = np.sqrt(cnt)
        ret = np.sqrt(cnt / (K * D * 1.0))
        print("AVG=",AVG)
        print("std_dev=",std_dev)
        return ret,std_dev

def read_each_file(filepath,lable):
    # sum of the value
    if lable == 0:
        ret = np.array([0, 0, 0, 0, 0, 0, 0])
        with open(filepath,'r') as f:
            all_data = f.readlines()
            for line in all_data:
                tmp = line.strip().split(' ')
                val = np.array(list(map(float,tmp)))
                ret = ret + val
                if (val[0] > 10 or val[1] > 10 or val[2] > 10 or val[3] > 10 or val[4] > 10 or val[5] > 10):  # or val[6]>250):
                    print("BUG1: ", filepath, " ", val)
        return ret
    # sum of the square
    else:
        ret = np.array([0, 0, 0, 0, 0, 0, 0])
        with open(filepath,'r') as f:
            all_data = f.readlines()
            for line in all_data:
                tmp = line.strip().split(' ')
                val = np.array(list(map(float,tmp)))
                if(val[0]>10 or val[1]>10 or val[2]>10 or val[3]>10 or val[4]>10 or val[5]>10):# or val[6]>250):
                    print("BUG2: ",filepath," ",val)
                ret = ret + (val-AVG)*(val-AVG)
        return ret


if __name__ == "__main__":
    # where you put XXX_density.xyz 
    filedir = "eval_result\\tmp1"
    avg = read_dir(filedir, 0)
    AVG = avg / (K * D * 1.0)
    std_dev = read_dir(filedir, 1)




