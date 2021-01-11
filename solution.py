def solution(A, K):
    if K > len(A):
        return -1
    maxSum = 0
    even = []
    odd = []
    for el in A:
        if el % 2:
            odd.append(el)
        else:
            even.append(el)
    odd.sort()
    even.sort()
    i = len(even) - 1
    j = len(odd) - 1
    while K > 1:
        print(K, i, j, maxSum)
        if (K % 2 == 1):
            if i >= 0:
                maxSum += even[i]
                i -= 1
            else:
                return -1
            K -= 1
        elif(i >= 1 and j >= 1):
            if (even[i] + even[i-1] <= odd[j] + odd[j-1]):
                maxSum += odd[j] + odd[j-1]
                j -= 2
            else:
                maxSum += even[i] + even[i-1]
                i -= 2
            K -= 2
        elif i >= 1:
            maxSum += even[i] + even[i-1]
            i -= 2
            K -= 2
        elif j >= 1:
            maxSum += odd[j] + odd[j-1]
            j -= 2
            K -= 2
    return maxSum

A = [3, 5, 7, 9, 11]
print(solution(A, 4))
