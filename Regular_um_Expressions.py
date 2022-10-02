def main():
    print(count(input("Text: ").lower()))


def count(s):
    count = 0
    s_list = list(s)

    if s.startswith("u") and s_list[1] == "m":
        count += 1

    for index, val in enumerate(s_list):
        if val == "u" and len(s) > 3:
            if s[index - 1].isspace():
                count += 1

    return count


if __name__ == "__main__":
    main()
