# reading all the XXX_out_point2mesh_distance.xyz files from PU-Net/evaluation
# and compute avg and std

import numpy as np
import os
import math

AVG = 0
STD = 0
doc = open('out.txt','w')

K = 20
P_NUM = 5000
D = 9000
index = 0
PointNumber = 0
def read_dir(filedir, lable):
    if lable == 0: # calc mean
        print("calculating mean ....")
        avg = 0
        pathDir = os.listdir(filedir)
        for allDir in pathDir:
            child = os.path.join('%s\\%s' % (filedir, allDir))
            print(child)
            avg = avg + read_each_file(child,lable)
        print("PointNumber=",PointNumber)
        AVG = avg / (1.0*PointNumber)
        print("AVG=",AVG)
        return AVG
    else:  # calc std
        print("calculating std ....")
        cnt = 0
        pathDir = os.listdir(filedir)
        for allDir in pathDir:
            child = os.path.join('%s\\%s' % (filedir, allDir))
            print(child)
            tmp = read_each_file(child,lable)
            cnt = cnt + tmp
        ret = np.sqrt(cnt / (1.0*PointNumber))
        STD = ret
        print("STD=", STD)
        return STD

def read_each_file(filepath,lable):
    if lable == 0: # add all the distance of points2mesh
        ret = 0
        global PointNumber
        with open(filepath,'r') as f:
            all_data = f.readlines()
            for line in all_data:
                tmp = line.strip().split(' ')
                val = np.array(list(map(float,tmp)))
                ret = ret + val[3]
                PointNumber = PointNumber +1
        return ret
    else:
        ret = 0
        with open(filepath,'r') as f:
            all_data = f.readlines()
            for line in all_data:
                tmp = line.strip().split(' ')
                val = np.array(list(map(float,tmp)))
                ret = ret + (val[3]-AVG)*(val[3]-AVG) # np.square(val-AVG)
        return ret



if __name__ == "__main__":
    filedir = "evaluation_file\\distance_3"
    PointNumber = 0
    # get the sum of all the values in XXX_out_point2mesh_distance.xyz files
    avg = read_dir(filedir, 0)

    # get std value
    std = read_dir(filedir,1)



