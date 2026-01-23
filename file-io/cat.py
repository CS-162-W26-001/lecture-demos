def main() -> None:
    try: 
        with open('file-does-not-exist.txt', 'r') as file:
            for current_line in file:
                current_line = current_line.strip()
                print(current_line)
    except FileNotFoundError as e:
        print("Could not find file")


if __name__ == "__main__":
    main()

