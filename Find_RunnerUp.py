if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array=sorted(arr, reverse=True)
    i=0
    while array[i]==array[i+1]:
        i+=1
    print(array[i+1])
