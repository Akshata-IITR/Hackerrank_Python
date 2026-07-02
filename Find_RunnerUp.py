if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unqarr= set(arr)
    sortedscores=sorted(unqarr)
    runner_up=sortedscores[-2]
    print(runner_up)
