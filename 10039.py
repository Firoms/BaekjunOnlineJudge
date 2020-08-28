score_list = []
for i in range(5):
    score_list.append(int(input()))


def avg(scores):
    total = 0
    for single_score in scores:
        if single_score < 40:
            total += 40
        else:
            total += single_score
    average = int(total/5)
    return average


print(avg(score_list))
