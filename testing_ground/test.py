from typing import Literal


print("test")


def test() -> bool:
    print("test func")
    return True


def test3() -> bool:
    print("test3 func")
    return True


def whoa() -> Literal[True]:
    print("whoa")
    print("whoa2")
    return True
