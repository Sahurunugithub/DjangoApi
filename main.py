
# class Amount:
#     def __init__(self,balance, accno):
#         self.bal= balance
#         self.acc= accno
#
#     def debit(self,amount):
#         self.bal -= amount
#         print("The debited amount is ",amount)
#         print("the total balance is ", self.total_balance())
#
#     def credit(self,amount):
#         self.bal += amount
#         print("The credited amount is ",amount)
#         print("the total balance is ",self.total_balance())
#
#     def total_balance(self):
#         return self.bal
#
# acc1 = Amount(35000, 123)
# print(acc1.bal)
# print(acc1.acc)
#
# debit_=int(input("Enter the amount you want to debit: "))
# acc1.debit(debit_)
#
# credit_=int(input("Enter the amount you want to credit: "))
# acc1.credit(credit_)
#
# # A simple Python script to add two numbers
# def add_numbers(num1, num2):
#     return num1 + num2
#
# # Call the function and print the result
# result = add_numbers(3, 5)
# print(f"The sum is {result}")
#
#
# # A Python script using list comprehensions and functions
# def get_even_numbers(data_list):
#     return [num for num in data_list if num % 2 == 0]
#
# # Using the function with a list
# numbers = range(1, 11)
# even_numbers = get_even_numbers(numbers)
# print(f"Even numbers: {even_numbers}")
#

# An advanced Python script with error handling, file operations, and OOP
class DataProcessor:
    def __init__(self, file_path):
        self.file_path = "C:\\Users\\Preeti.sahu\\Downloads"

    def read_data(self):
        try:
            with open(self.file_path) as file:
                data = file.read()
                return data
        except FileNotFoundError:
            print("File not found.")
            return None

    def process_data(self, data):
        # Implement data processing logic here
        pass

# Using the class to process data
processor = DataProcessor('image.png')
data = processor.read_data()
if data:
    processor.process_data(data)


