def runner_up(a):
    doplicat_remove = set(a)
    list_vlu = list(doplicat_remove)
    list_vlu.sort()
    return list_vlu

if __name__ == "__main__":
    n = int(input())
    a = input().split()
    result = runner_up(a)
    print(result)
    