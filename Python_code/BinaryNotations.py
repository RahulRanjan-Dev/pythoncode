def solution(A):
    length = 0

    for i in range(len(A)):
        if A[i] == -1:
            length += 1
            print(i)
            break
        else:
            length += 1
            i = A[i]

    return length

A = [1, -1, 1, 3, 2]
res=solution(A)
print(res)