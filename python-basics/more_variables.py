PI = 3.14159

def area_of_rectangle() -> int:
    height = 2
    width = 8
    area = height * width
    return area

def area_of_circle(radius:int) -> int:
    pi = 3.14
    area =  pi * (radius ** 2)
    if area > 50:
        print("This is a large circle")
    return int(area)
    
    print("goodbye")

def main() -> None:

    string_value_of_5 = "5"
    my_integer = 0

    my_integer = int(string_value_of_5)

    #print(area)
    #print("area_of_rectangle()", area_of_rectangle())

    #greeting = "hello again"
    #print(greeting)
    
   # greeting = "goodbye"
    #print(greeting)

    #greeting = 12345
    #print(greeting)

    area = area_of_circle(5)
    print(area)

if __name__ == "__main__":
    main()
