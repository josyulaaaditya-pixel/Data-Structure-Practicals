
# 1. LINEAR SEARCH
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 2. BINARY SEARCH
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# 3. TAKE INPUT
n = int(input("Enter number of IDs: "))
customer_ids = []

for i in range(n):
    cid = int(input("Enter ID: "))
    customer_ids.append(cid)

target_id = int(input("Enter ID to search: "))


# 4. LINEAR SEARCH RESULT
pos_linear = linear_search(customer_ids, target_id)

if pos_linear != -1:
    print("Linear Search: Found at", pos_linear)
else:
    print("Linear Search: Not Found")


# 5. BINARY SEARCH RESULT
customer_ids.sort()
pos_binary = binary_search(customer_ids, target_id)

if pos_binary != -1:
    print("Binary Search: Found at", pos_binary)
else:
    print("Binary Search: Not Found")
