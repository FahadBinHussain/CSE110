def show_palindromic_triangle(n):
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(1, i+1):
            print(k, end=" ")
        for l in range(i-1, 0, -1):
            print(l, end=" ")
        print()
    return

show_palindromic_triangle(5)
