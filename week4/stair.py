#다이나믹 프로그래밍
def count_ways(n):
    if n == 1:
        #1일때 1가지의 방법으로 오를 수 있으므로 1로 반환
        return 1
    elif n == 2:
        #2일때 2가지의 방법 2, 1-2 으로 오를 수 있으므로 2로 반환
        return 2

    dp = [0] * (n + 1)
    #각 층에 도달하는 방법의 수를 저장하는 리스트로서 0으로 초기화한다.
    dp[1] = 1
    #1층에 도달하는 방법의 수 1
    dp[2] = 2
    #2층에 도달하는 방법의 수 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        #1층과 2층은 이미 1과 2로 초기화 되었으므로 3층부터 시작하여 3층을 기점으로 한칸 전과 두칸 정의 경우의 수를 모두 합하는 반복문이다.

    return dp[n]


n = int(input())
print(count_ways(n))