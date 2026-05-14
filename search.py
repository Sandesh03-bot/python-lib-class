import pandas as pd

# Replace with your dataset file name
df = pd.read_csv("netflix_titles.csv")

# Extract titles and remove empty values
titles = df["title"].dropna().tolist()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = 0
    j = 0

    # Compare elements
    while i < len(left) and j < len(right):
        if left[i].lower() < right[j].lower():
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Case-insensitive comparison
        if arr[mid].lower() == target.lower():
            return mid

        elif arr[mid].lower() < target.lower():
            low = mid + 1

        else:
            high = mid - 1

    return -1


sorted_titles = merge_sort(titles)

movie_name = input("Enter movie title to search: ")

result = binary_search(sorted_titles, movie_name)

if result != -1:
    print(f'"{movie_name}" found in Netflix dataset.')
else:
    print(f'"{movie_name}" not found in Netflix dataset.')
    