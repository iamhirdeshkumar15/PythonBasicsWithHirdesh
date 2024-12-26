# Find the minimum element and maximum element from an array
def find(arr):
    minn, maxx = arr[0], arr[0]
    for num in arr[1:]:
        if num < minn:
            minn = num
        elif num > maxx:
            maxx = num
    return minn, maxx

# Find and print the minimum and maximum elements
array = [4,10,40,1,5,9,2,6,3,5]
minn,maxx = find(array)
print(f"Minimum: {minn}, Maximum: {maxx}")

######################################################################################
# Take user input for the array
input_str = input("Enter elements of the array separated by spaces: ")
array = list(map(int, input_str.split()))
# Find and print the minimum and maximum elements
minn, maxx = find(array)
print(f"Minimum: {minn}, Maximum: {maxx}")
######################################################################################