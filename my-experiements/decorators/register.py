
registry = []
def register(decorated):
    global register
    registry.append(decorated)
    return decorated


@register
def func01():
    print("func01")

@register
def func02():
    print("func02")


def main():
    for f in registry:
        f()


if __name__ == "__main__":
    main()


