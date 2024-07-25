import winsound

def play_sound():
    duration = 100  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2] # Sorting the first half
        right_arr = arr[len(arr)//2:]  # Sorting the second half

        merge_sort(left_arr)
        merge_sort(right_arr)
        

        i = j = k = 0

        # merge
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] =left_arr[i]
                i += 1

            else:
                arr[k] =right_arr[j]
                j += 1
            play_sound()
            print(arr)
            k += 1

        # Checking if any element was left
        while i < len(left_arr):
            arr[k] =left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# Accept an array of n numbers from user input
arr = list(map(int, input("Enter the numbers to be sorted, separated by spaces: ").split()))
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)
