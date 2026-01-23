from typing import TextIO

def read_file() -> None:
    with open('data.csv', 'r') as csv_file:
        contents = parse_file(csv_file)
        print(contents)


def parse_file(csv_file:TextIO) -> list[list[str]]:
    line_number = 1
    lines = []
    for line in csv_file:
        if line_number > 1:
            lines.append(parse_line(line))
        line_number += 1
    return lines


def parse_line(line: str) -> list[str]:
    tokens: list[str] = []
    line = line.strip()
    tokens = line.split(",")
    return tokens


def file_write() -> None:
    filename = 'new-data.txt'
    with open(filename, 'a') as file:
        file.write("Hello world!\n")
        file.write("Goodbye\n")

def main() -> None:
    #read_file()
    file_write()

if __name__ == "__main__":
    main()
