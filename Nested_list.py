if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a=[name, score]
        students.append(a)
    scores=[student[1] for student in students]
    unique=set(scores)
    sorted_scores=sorted(unique)
    second=sorted_scores[1]
    output=[student[0] for student in students if student[1]==second]
    output.sort()
    for i in output:
        print(i)
