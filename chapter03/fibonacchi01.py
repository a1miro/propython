def fibonacci():
    yield 1
    yield 2
    yield 2
    yield 3
    yield 5
    yield 8




if __name__ == "__main__":
    for i in fibonacci():
        print(i)

