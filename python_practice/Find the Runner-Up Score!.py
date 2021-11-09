if __name__ == "__main__":
    n = int(input())    
    a = map(int, input().split())
    
    result = sorted(set(a))
    print(result[-2])

#print("_________________OR__________")
# 
#if __name__ == "__main__":
#    n = int(input())  
#    for i in range(n):
#        a = map(int, input().split())
#
#        result = sorted(set(a))
#        print(result[-2])
#        break