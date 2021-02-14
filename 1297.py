# TV 크기
import sys
a,b,c = map(int,sys.stdin.readline().split(" "))
print(int(((a**2)*(b**2)/(b**2+c**2))**0.5), int(((a**2)*(c**2)/(b**2+c**2))**0.5))