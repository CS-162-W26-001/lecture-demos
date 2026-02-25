"""
1. Function needs to call itself
2. Stop recursion at some point (base case)
3. Get closer to the base case every recursive call

"""

def recursive(n: int) -> None:
    if n == 0:
        return
    if n == 1:
        print("n = 1")
        return
    print("Before", n)
    recursive(n - 1)
    print("After", n)

def main() -> None:
    recursive(5)

if __name__ == "__main__":
    main()
