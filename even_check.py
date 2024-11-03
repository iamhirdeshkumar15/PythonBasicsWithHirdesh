# even_check.py
def is_even(num):
    """Check if a number is even.
    
    Args:
        num (int): The number to check.
        
    Returns:
        bool: True if the number is even, False otherwise.
    """
    return num % 2 == 0

if __name__ == "__main__":
    try:
        numbers = input("Enter numbers separated by commas: ")
        number_list = [int(num.strip()) for num in numbers.split(",")]
        for number in number_list:
            if is_even(number):
                print(f"{number} is even.")
            else:
                print(f"{number} is odd.")
    except ValueError:
        print("Invalid input! Please ensure all entries are integers.")
