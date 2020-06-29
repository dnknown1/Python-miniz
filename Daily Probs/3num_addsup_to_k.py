"""
This problem was asked by Microsoft.

Given an array of numbers and a number k, determine if there are three entries in the array which add up to the specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.
"""
def adds_upto_k(arr, k):
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)):
            key = k-(arr[i]+arr[i+j])
            if key in arr[j+1:]:
                return True
    return False

if __name__ == '__main__':
    arr = [20, 303, 3, 4, 25]
    k   = 49
    print(adds_upto_k(arr, k))
