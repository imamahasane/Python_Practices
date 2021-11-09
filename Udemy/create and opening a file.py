def average(array):
    myList = []
    myList.append(arr)

    set(myList)
    m = sum(myList)
    mm = m/len(myList)
    return mm

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)