def maxValueDp(gaps,cur):
    gaps.sort()
    dp=[[0 for _ in range(cur+1)] for _ in range(len(gaps))]
    if len(gaps)<1:
        return 0
    for j in range(cur):
        dp[0][j+1]=((j+1)//gaps[0][0])*gaps[0][1]

    for i in range(1,len(gaps)):
        for j in range(cur):
            tt=((j+1)//gaps[i][0])*gaps[i][1]
            tt2=((j+1)//gaps[i][0])*gaps[i][0]
            left=(j+1)-tt2
            if left<0:
                left=0
            dp[i][j+1]=max(dp[i-1][j+1],tt+dp[i][left])
    return dp[-1][-1]

TC = int(input())

for tc in range(TC):
    initMoney,monthMoney=map(int,input().split(" "))
    N,L=map(int,input().strip().split(" "))
    monthItem=[[0 for _ in range(N)]for _ in range(L+1)]
    for i in range(N):
        income=list(map(int,input().strip().split(" ")))
        for j,item in enumerate(income):
            monthItem[j][i]=item
    curMoney=initMoney
    ans=0
    for i in range(L):
        # 주식 팔기
        
        # 주식 사기
        gaps=[]
        newItem=[]
        for j in range(N):
            gap=monthItem[i+1][j]-monthItem[i][j]
            if gap>0:
                gaps.append([monthItem[i][j],gap])
                newItem.append(monthItem[i][j])

        
        # 이번달 주식 가격 monthItem[i][j], 다음달 주식 가격 monthItem[i+1][j]
        # 어떻게 사야 가장 많이 벌지...?
        # 주식 사는 과정
        ans+=maxValueDp(gaps,curMoney)
        curMoney+=maxValueDp(gaps,curMoney)
        curMoney+=monthMoney
    print(f"#{tc+1} {ans}")

#     print()
#     curMoney+=monthMoney


'''
400 0
5 8
180 180 180 150 120 150 180 180 180
315 315 315 300 300 300 300 300 315
219 282 255 255 255 219 219 219 219
228 222 204 246 255 228 228 228 228
120 150 120 120 120 120 120 120 120

300 60
3 8
135 120 111 144 170 170 171 173 169
156 150 144 144 144 150 150 150 147
195 180 165 150 141 172 185 190 159

600 40
8 8
125 125 125 125 125 115 110 110 125
512 616 616 616 616 616 616 616 616
660 660 660 575 575 575 660 660 660
345 345 448 540 540 515 515 450 395
425 425 425 425 425 500 500 500 425
100 100 100 100 100 110 110 100 100
870 850 906 906 906 906 860 860 870
305 305 305 305 260 295 305 305 305 

'''





