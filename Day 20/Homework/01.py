new_arr = [1,3,34,5,22,7,10,16,31,4,9,24,18]
for i in range(len(new_arr)):
    if (new_arr[i]% 5 == 0) and (new_arr[i]% 3 == 0):
        print(new_arr[i])