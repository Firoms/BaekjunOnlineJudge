# 16진수
import sys
num = sys.stdin.readline().rstrip()
num = num[::-1]
num_dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
mul = 1
ten = 0
for i in num:
    ten += num_dict[i]*mul
    mul*=16
print(ten)