# komleksitas waktu O(N)
# komleksitas ruang O(N)

def pair_sum(arr, target):
    num_indices = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]

        num_indices[num] = i

    return None

if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]