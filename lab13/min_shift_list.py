def shift_search(arr):
    left_index = 0
    right_index = len(arr) - 1
    mid = (left_index + right_index) // 2
    if len(arr) == 1:
        return arr[left_index]
    elif len(arr) == 2:
        if arr[left_index] > arr[right_index]:
            return arr[right_index]
        else:
            return arr[left_index]
    elif len(arr) == 0:
        return None
    else:
        if len(arr) % 3 == 0:
            if arr[mid] > arr[mid-1]:
                return arr[mid+1]
            else:
                return arr[left_index]
        else:
            if arr[mid] > arr[mid+1]:
                return arr[mid+1]
            else:
                return arr[left_index]
