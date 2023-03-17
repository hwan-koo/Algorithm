while True:
    n = int(input())
    if n == -1:
        break
    temp_array = []
    for i in range(1, n):
        if n % i == 0:
            temp_array.append(i)
    if sum(temp_array) == n:
        print(f"{n} = ", end="")
        for j in range(len(temp_array)):
            if j == len(temp_array) - 1:
                print(temp_array[j])
            else:
                print(f"{temp_array[j]} + ", end="")
    else:
        print(f"{n} is NOT perfect.")