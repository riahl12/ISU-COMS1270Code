# Riley Ahlrichs    4-18-2025
# Lab Week 12: Created unit tests for all the functions in the myMath.py file and fixed code in myMath.py if the test were not
# running as intended.

from myMath import add, subtract, multiply, divide, power, factorial, is_prime, sum_of_digits, gcd, fib, lcm, square_root, abs_diff, log, mod, mean, median, mode, celsius_to_fahrenheit, fahrenheit_to_celsius, inverse, triangular_number

def test_add():
    assert add(1,2) == 3
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5,3) == 2
    assert subtract(-3, 5) == -8

def test_multiply():
    assert multiply(5,2) == 10
    assert multiply(-3, 7) == -21

def test_divide():
    assert divide(14,7) == 2
    assert divide(0, 5)== 0
    try:
        divide(3, 0)
        assert False, "Expected ValueError but none was raised"
    except ValueError:
        pass

def test_power():
    assert power(5,3) == 125
    assert power(3,0) == 1
    assert power(0,4) == 0

def test_factorial():
    assert factorial(0) == 1      
    assert factorial(1) == 1      
    assert factorial(5) == 120
    try:
        factorial(-1)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass

def test_is_prime():
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(29) == True
    assert is_prime(100) == False

def test_sum_of_digits():
    assert sum_of_digits(123) == 6         # 1 + 2 + 3
    assert sum_of_digits(0) == 0           # edge case
    assert sum_of_digits(999) == 27        # 9 + 9 + 9
    assert sum_of_digits(-456) == 15

def test_gcd():
    assert gcd(48, 18) == 6    # GCD of 48 and 18 is 6
    assert gcd(56, 98) == 14
    assert gcd(1, 10) == 1
    assert gcd(-48, 18) == 6

def test_fib():
    assert fib(3) == 2    # 0, 1, 1, 2
    assert fib(4) == 3    # 0, 1, 1, 2, 3
    assert fib(10) == 55

def test_lcm():
    assert lcm(4, 5) == 20 
    assert lcm(1, 5) == 5
    assert lcm(0, 5) == 0

def test_sqr_root():
    assert square_root(4) == 2
    assert square_root(100) == 10
    try:
        square_root(-1)
        assert False, "Expected ValueError for negative input"
    except ValueError:
        pass

def test_abs_diff():
    assert abs_diff(5, 3) == 2
    assert abs_diff(-3, 5) == 8
    assert abs_diff(0, 50) == 50

def test_log():
    assert log(100, 10) == 2
    assert log(16, 2) == 4
    assert log(1, 10) == 0
    try:
        log(0, 10)
        assert False, "Expected ValueError for log(0)"
    except ValueError:
        pass

def test_mod():
    assert mod(15, 4) == 3    # 15 % 4 = 3
    assert mod(20, 6) == 2
    assert mod(10, -3) == -2
    assert mod(0, 5) == 0

def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3        # Mean of [1, 2, 3, 4, 5] is 3
    assert mean([10, 20, 30, 40]) == 25
    assert mean([1.5, 2.5, 3.5, 4.5]) == 3
    assert mean([-1, -2, -3, -4, -5]) == -3

def test_median():
    assert median([1, 2, 3, 4, 5]) == 3       # Median of [1, 2, 3, 4, 5] is 3
    assert median([7, 9, 11]) == 9
    assert median([10, 20, 30, 40]) == 25
    assert median([-5, -4, -3, -2, -1]) == -3

def test_mode():
    assert mode([1, 2, 2, 3, 4, 5, 6, 7, 8]) == 2        # Mode of [1, 2, 2, 3, 4, 5, 6, 7, 8] is 2
    assert mode([10, 20, 30, 30, 40, 50, 50, 50]) == 50
    assert mode([1.5, 2.5, 2.5, 3.5]) == 2.5
    try:
        mode([])
        assert False, "Expected ValueError for empty list"
    except IndexError:
        pass

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32        # 0°C = 32°F
    assert celsius_to_fahrenheit(100) == 212     # 100°C = 212°F
    assert celsius_to_fahrenheit(1000) == 1832   # 1000°C = 1832°F
    assert celsius_to_fahrenheit(25) == 77       # 25°C = 77°F

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0         # 32°F = 0°C
    assert fahrenheit_to_celsius(212) == 100      # 212°F = 100°C
    assert fahrenheit_to_celsius(77) == 25        # 77°F = 25°C
    assert fahrenheit_to_celsius(1832) == 1000    # 1832°F = 1000°C

def test_inverse():
    assert inverse(2) == 0.5         # Inverse of 2 is 0.5
    assert inverse(0.5) == 2         # Inverse of 0.5 is 2
    try:
        inverse(0)
        assert False, "Expected ValueError for inverse of zero"
    except ValueError:
        pass

def test_triangular_number():
    assert triangular_number(1) == 1          # 1st triangular number is 1
    assert triangular_number(3) == 6          # 3rd triangular number is 6 (1 + 2 + 3)
    assert triangular_number(5) == 15
    assert triangular_number(0) == 0
   
   