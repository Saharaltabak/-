# السؤال الاول A
L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]
d = {}
for key, value in zip(L1, L2):
    d[key] = value
print(d)



# السؤال الاول B
number = int(input("أدخل عددًا لحساب عامليه: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"عاملي العدد {number} هو: {factorial}")



# السؤال الاول C
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
B_items = [item for item in L if item.startswith('B')]
print("العناصر التي تبدأ بحرف 'B':", B_items)



# السؤال الاول D

d = {i: i+1 for i in range(11)}
print(d)


# السؤال الثاني
def binary_to_decimal(binary_str):
    # This function converts a binary string to a decimal number.
    decimal_number = 0
    length = len(binary_str)
    
    for i in range(length):
        # Convert each character to an integer (0 or 1)
        bit = int(binary_str[i])
        # Calculate its value in decimal and add it to the total
        decimal_number += bit * (2 ** (length - 1 - i))
    
    return decimal_number

def is_binary_string(s):
    # This function checks if a given string is a valid binary number
    for char in s:
        if char not in '01':
            return False
    return True

def main():
    while True:
        binary_str = input("Enter a binary number: ")
        
        if is_binary_string(binary_str):
            decimal_number = binary_to_decimal(binary_str)
            print(f"The decimal equivalent of binary {binary_str} is {decimal_number}.")
            break
        else:
            print("Invalid input. Please enter a valid binary number (containing only 0 and 1).")

if __name__ == "__main__":
    main()


#السؤال الثالث quiz التعامل مع ملف 
import json
import csv
import os

def load_quiz(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.endswith('.csv'):
        questions = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    questions.append({'question': row[0], 'answer': row[1]})
        return questions
    elif file_path.endswith('.txt'):
        questions = []
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 2):
                questions.append({'question': lines[i].strip(), 'answer': lines[i+1].strip()})
        return questions
    else:
        raise ValueError("Unsupported file format")

def take_quiz(questions):
    score = 0
    for question in questions:
        print(question['question'])
        answer = input("Enter answer: ")
        if answer.lower() == question['answer'].lower():
            score += 1
    return score

def save_results_json(username, score, results_file):
    result = {'username': username, 'score': score}
    try:
        with open(results_file, 'r') as file:
            results = json.load(file)
    except FileNotFoundError:
        results = []
    results.append(result)
    with open(results_file, 'w') as file:
        json.dump(results, file, indent=4)

# Load questions from a file
questions_file = input("Enter the path to the questions file (text, json, csv): ").strip()
questions = load_quiz(questions_file)

# Conduct the quiz
user_score = take_quiz(questions)

# Get user name and save results
user_name = input("Enter your name: ")
results_file = 'results.json'

save_results_json(user_name, user_score, results_file)

print("Result is:", user_score)



#السؤال الرابع  BankAccount
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate=0.05):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")


# Create a BankAccount instance
bank_account = BankAccount("12345678", "sahar")

# Deposit $1000
bank_account.deposit(1000)

# Withdraw $500
bank_account.withdraw(500)

# Print the current balance
print(f"Current balance: ${bank_account.get_balance():.2f}")

# Create a SavingsAccount instance
savings_account = SavingsAccount("87654321", "sahar")  # 5% interest rate

# Apply interest
savings_account.apply_interest()

# Print the account details
print(savings_account)



