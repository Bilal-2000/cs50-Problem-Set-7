import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    dates = {"1": "13", "2": "14", "3": "15",
             "4": "16", "5": "17", "6": "18",
             "7": "19", "8": "20", "9": "21",
             "10": "22", "11": "23", "12": "24"}
    i = 1
    time_list = list()
    size = len(s)
    small = False
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM
    if size > 15:
        matches = re.search(
            r"^(1[0-2]||[1-9]):?([0-5][0-9])?[ ](AM|PM)[ ]to[ ](1[0-2]||[1-9]):?([0-5][0-9])?[ ](AM|PM)$", s)
        if matches:
            pass
        else:
            raise ValueError
    else:
        matches = re.search(
            r"^(1[0-2]||[1-9])[ ](AM|PM)[ ]to[ ](1[0-2]||[1-9])[ ](AM|PM)$", s)
        small = True
        if matches:
            pass
        else:
            raise ValueError

    if small:
        while i < 5:
            time_list.append(matches[i])
            i += 1
    else:
        while i < 7:
            time_list.append(matches[i])
            i += 1

    for index, val in enumerate(time_list):
        if val == "PM":
            if small:
                time_list[index - 1] = dates.get(time_list[index - 1])
            else:
                time_list[index - 2] = dates.get(time_list[index - 2])

    for index, val in enumerate(time_list):
        if len(val) < 2:
            time_list[index] = f"0{val}"

    if small:
        return(f"{time_list[0]}:00 to {time_list[2]}:00")
    else:
        return(
            f"{time_list[0]}:{time_list[1]} to {time_list[3]}:{time_list[4]}")


if __name__ == "__main__":
    main()
