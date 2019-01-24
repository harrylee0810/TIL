# N명의 사람이 1리터의 쥬스를 나누어 각자 잔에 따라서 마시고자 한다.
# 그런데 한사람이 따르고 분배하는 것은 공평하지 않기 때문에 다음 방법을 통해 쥬스를 나눠 마시기로 하였다.
# 첫번째 사람이 원하는 만큼 한잔 따르고, 두번째 사람이 원하는 만큼  한잔 따르고, ..., N번째 사람이 남은만큼 한잔 따른다.
# 그 후 N번째 사람이 N개의 잔 중에 하나를 가져가고, N-1번째 사람이 남은 잔 중에 하나를 가져가고, 최종적으로 첫번째 사람이 마지막으로 남은 잔을 가져간다.

# 모든 사람은 목이 마른 상태이기 때문에, 최대한의 쥬스를 마시고자 최선의 전략을 쓴다고 가정하자.
# 또한 이들은 서로 모르기 때문에, 담합 혹은 협력 등은 없다고 가정하자.
# 이때 첫번째 사람부터 N번째 사람까지 각각 쥬스를 얼마씩 마시게 되는지 구하도록 하자.


a = int(input())
for i in range(1,a+1):
    b = int(input())
    result = ['1/'+ str(b) for j in range(b)]
    print(f"#{i} {' '.join(result)}")


# 입력
# 2	// 전체 테스트케이스 개수
# 1   // 첫 번째 TC의 사람의 수 N
# 2   // 두 번째 TC의 사람의 수 N

# 출력
# #1 1/1	// 1번 TC 결과
# #2 1/2 1/2  // 2번 TC 결과
