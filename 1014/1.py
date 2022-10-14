
TC=int(input())

for tc in range(TC):
    n=int(input())
    trees=list(map(int,input().split(" ")))
    target=max(trees)
    trees.remove(target)

    dateValue=2
    cnt=0
    while True:
        cnt+=1
        dateValue%=2
        dateValue+=1
        if min(trees)<target-2:
            trees[trees.index(min(trees))]+=dateValue
        elif min(trees)==target:
            break
        else:
            for i in range(len(trees)):
                if trees[i]+dateValue==target:
                    trees[i]+=dateValue
                    break
                else:
                    trees[trees.index(min(trees))]+=dateValue
                    break

    print(f"#{tc+1} {cnt-1}")

'''
4       
2 3 10 5
'''

