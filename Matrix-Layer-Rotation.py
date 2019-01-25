import math
import os
import random
import re
import sys
import copy

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    for k in range(0,r):
        a=copy.deepcopy(matrix)
        b=0
        while(b<int(min(m,n)/2)):
            for i in range(0,m):
                for j in range(0,n):
                    if(i==(0+b)):
                        if(j==(0+b)):
                            matrix[i][j]=a[i][j+1]                        
                        if(j>(0+b) and j<(n-1-b)):
                            matrix[i][j]=a[i][j+1]
                    if(j==(0+b)):
                        if(b==0):
                            if(i>(0+b)):
                                matrix[i][j]=a[i-1][j]
                        else:
                            if(i>(0+b) and i<m-1):
                                matrix[i][j]=a[i-1][j]
                    if(i==(m-1-b)):
                        if(b==0):
                            if(j>(0+b)):
                                matrix[i][j]=a[i][j-1]
                        else:
                            if(j>(0+b) and j<n-1):
                                matrix[i][j]=a[i][j-1]
                    if(j==(n-1-b)):
                        if(i<(m-1-b) and i>=b):
                            matrix[i][j]=a[i+1][j]
            b=b+1
    for i in range(0,m):
        for j in range(0,n):
            print(matrix[i][j],end='\t')
        print()
    

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
