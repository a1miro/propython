registry = []

def register(decorated):
    registry.append(decorated)
    return decorated


@register
def foo():
    return 3

@register
def bar():
    return 5

def main():
    answers=[]
    for func in registry:
        answers.append(func())

    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()


