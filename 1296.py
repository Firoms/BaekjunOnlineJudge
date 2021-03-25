# 데이트
import sys
boy_name = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline().rstrip())
score = 0
name = []
bl = boy_name.count('L')
bo = boy_name.count('O')
bv = boy_name.count('V')
be = boy_name.count('E')
for _ in range(N):
    girl_name = sys.stdin.readline().rstrip()
    l = girl_name.count('L') + bl
    o = girl_name.count('O') + bo
    v = girl_name.count('V') + bv
    e = girl_name.count('E') + be
    new_score = ((l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e))%100
    if score < new_score:
        score = new_score
        name = [girl_name]
    elif score == new_score:
        name.append(girl_name)
print(sorted(name)[0])
