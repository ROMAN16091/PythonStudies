# Перевірка умов за допомогою оператора if-elif-else
if 5 < 4:
    print("Ok")
elif 3 < 2:
    print("OK 2")
elif 4 < 3:
    print("OK 3")
else:
    print("no")
# У цьому прикладі всі умови хибні, тому буде виконано else і виведено "no"

# Перевірка, чи є число непарним або парним
num1 = int(input("Enter num: "))
if num1 % 2 != 0:  # Якщо число непарне
    print("Odd")
else:  # Якщо число парне
    print("Even")

# Перевірка чи закінчується введений email на '@gmail.com'
ends_email = "@gmail.com"
email_input = input("Enter your email: ")
if email_input.endswith(ends_email):  # Якщо email закінчується на '@gmail.com'
    print(f"Hello {email_input}")
else:  # Якщо email не закінчується на '@gmail.com'
    print(f"Error email {email_input}")
