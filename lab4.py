def check_sum_size():
    """
    Function to read two numbers, calculate the sum, and check if it's > 100.
    """
    try:
       
        num1 = float(input("94"))
        num2 = float(input("44 "))

       
        total_sum = num1 + num2

        
        if total_sum > 100:
            print("100")
        else:
            print("50")
            
    except ValueError:
        print("خطأ في الإدخال. يرجى إدخال أرقام صالحة.")


check_sum_size()

