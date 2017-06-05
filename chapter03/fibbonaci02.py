
def fibonacci():
    numbers = []
    while True:
        if len(numbers) < 2:
            numbers.append(1)
        else:
            numbers.append(sum(numbers))
            numbers.pop(0)
        yield numbers[-1]

if __name__ == "__main__":
    '''
    for i in fibonacci():
        print(i)
    '''

    gen = fibonacci()
    for i in range(0,10):
        print(next(gen))

