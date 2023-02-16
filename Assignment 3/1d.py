for i in range(18, 64, 9):
    if i % 2 != 0:
        print(f"-{i}", end="")
    else:
        print(f"{i}", end="")
    if i <= 54:
        print(", ", end="")

