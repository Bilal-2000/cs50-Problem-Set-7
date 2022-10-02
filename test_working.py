from Working_9_to_5 import convert


def test_first():
    convert("10 PM to 8 AM")


def test_second():
    convert("10:30 PM to 8:50 AM")


def test_third():
    convert("9:60 AM to 5:60 PM")


def test_fourth():
    convert("9 AM - 5 PM")


def main():
    test_first()
    test_second()
    test_third()
    test_fourth()


if __name__ == "__main__":
    main()
