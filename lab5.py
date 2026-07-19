import random
comparison_count = 0 # Global counter
def min_max_dc(arr, low, high):
    global comparison_count
    # Base case: single element
    if low == high:
        return arr[low], arr[low]
    # Base case: two elements
    if high == low + 1:
        comparison_count += 1
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    # Divide
    mid = (low + high) // 2
    min1, max1 = min_max_dc(arr, low, mid)
    min2, max2 = min_max_dc(arr, mid + 1, high)
    # Combine results
    comparison_count += 2
    overall_min = min(min1, min2)
    overall_max = max(max1, max2)
    return overall_min, overall_max
def min_max_naive(arr):
    global comparison_count
    overall_min = arr[0]
    overall_max = arr[0]
    for i in range(1, len(arr)):
        comparison_count += 1
        if arr[i] < overall_min:
            overall_min = arr[i]
        comparison_count += 1
        if arr[i] > overall_max:
            overall_max = arr[i]
    return overall_min, overall_max
# --- Demonstration on small array ---
arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]
comparison_count = 0
mn, mx = min_max_dc(arr, 0, len(arr) - 1)
print(f"Divide and Conquer: Min = {mn}, Max = {mx}, Comparisons = {comparison_count}")
comparison_count = 0
mn, mx = min_max_naive(arr)
print(f"Naive: Min = {mn}, Max = {mx}, Comparisons = {comparison_count}")
# --- Demonstration on large random array ---   
# --- Performance Analysis ---
print(f'\n{"Size":>8} {"DC Comps":>12} {"Naive Comps":>14} {"Formula 3n/2-2":>16}')
print('-' * 56)
for size in [10, 100, 1000, 10000]:
    arr = [random.randint(0, 10000) for _ in range(size)]
    comparison_count = 0
    min_max_dc(arr, 0, len(arr) - 1)
    dc_comparisons = comparison_count
    comparison_count = 0
    min_max_naive(arr)
    naive_comparisons = comparison_count
    formula_comparisons = (3 * size // 2) - 2
    print(f'{size:>8} {dc_comparisons:>12} {naive_comparisons:>14} {formula_comparisons:>16}')