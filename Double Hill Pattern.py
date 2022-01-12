n=int(input())
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=' ')
    for k in range(0,i+1):
        print('*',end=' ')
    for j in range(2,(n-i-1)*2):
        print(end=' ')
    for k in range(0,i+1):
        if(k==4):
            break
        else:
            print('*',end=' ')
    print()
