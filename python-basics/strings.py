def main() -> None:
    name = "McDonald-Dunn \"Forest\""
    long_string = """

line 2


line 5


line 8

    """
    sqrt_of_2 = 2 ** 0.5
    print(f"square root of 2 is {sqrt_of_2:.2f}")
    
    object = "douglas fir"
    height = 125

    output = f"I went to {name} and saw {object}. It had a height of {height * 1000.5}ft."
    print(output)



if __name__ == "__main__":
    main()
