# Prime Factorization and Divisors Finder

This Python script provides functions to find the prime factors and divisors of a given number. The script uses a simple algorithm to factorize the number into its prime components and then generates all possible divisors using these prime factors.

## Usage

1. Clone the `index.py` file from this repository
2. Run the `index.py` script
3. Enter a number you want to find the Divisors of

## Functions

_This function takes an integer **num** as input and returns a list of its prime factors._
### `findPrimaryFactors(num: int) -> List[int]`

<br>

_This function takes an integer **num** as input and returns a list of all its divisors._
### `findDividers(num: int) -> List[int]`

## Example:
```python
print("Please enter a number!")
num = int(input(">> "))

print("Prime Factors:", findPrimaryFactors(num))
print("Divisors:")
for x in findDivisors(num):
    print(x, ": ", num % x == 0)
```

## License

This project is licensed under the [MIT License](LICENSE).

---

## Developer
This Project was Developed by [c4vxl](https://c4vxl.de)