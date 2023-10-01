def join_array_remove_duplicate(arrayA, arrayB):
    # your code here
    hasil = arrayA + arrayB

    hasil_tanpa_duplikat = []

    for item in hasil:
        if item not in hasil_tanpa_duplikat:
            hasil_tanpa_duplikat.append(item)

    return hasil_tanpa_duplikat

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]


    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]


    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
