def get_valid_int(prompt, condition=lambda x: x > 0, error_msg="Invalid input. Please try again."):
    while True:
        try:
            value = int(input(prompt))
            if condition(value):
                return value
            else:
                print(error_msg)
        except ValueError:
            print("Please enter a valid number.")
            