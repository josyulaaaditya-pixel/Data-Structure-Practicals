
# 1. SELECTION SORT
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# 2. BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# 3. TAKE CUSTOM SALARIES
n = int(input("Enter number of employees: "))
salaries = []

for i in range(n):
    salary = float(input("Enter salary: "))
    salaries.append(salary)


# 4. CHOOSE SORTING METHOD
choice = input("Enter selection or bubble: ").lower()

if choice == "selection":
    sorted_salaries = selection_sort(salaries.copy())

elif choice == "bubble":
    sorted_salaries = bubble_sort(salaries.copy())

else:
    print("Invalid choice")
    exit()


# 5. DISPLAY RESULTS
print("Sorted Salaries:", sorted_salaries)
print("Top 5 Highest:", sorted_salaries[-5:][::-1])
