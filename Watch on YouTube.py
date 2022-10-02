import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(
        r"https?://(?:www.)?youtube.com/embed/(\w+)", s, re.IGNORECASE)
    if match:
        print("https://youtu.be/", match[1], sep="")
        sys.exit()
    return None


if __name__ == "__main__":
    main()
