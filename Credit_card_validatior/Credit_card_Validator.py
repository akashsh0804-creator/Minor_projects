#program for credit card validating and also cassification of credit cards (American Express, Mastercard, VISA card)

sum_odd_digits = 0
sum_even_digits = 0
total = 0

oldcard_no = input("Enter a credit card no.:")
#Removing any "-" and " " from the user input
card_no = oldcard_no.replace("-", "")
card_no = card_no.replace(" ", "")

#__________Classification of Credit cards__________
if len(card_no) == 15 and card_no[0:2] == "34" or card_no[0:2] == "37":
    print(f"{oldcard_no} is from American Express")
elif len(card_no) == 16 and card_no[0:2] == "51" or card_no[0:2] == "52" or card_no[0:2] == "53" or card_no[0:2] == "54" or card_no[0:2] == "55":
    print(f"{oldcard_no} is a Mastercard")
elif len(card_no) == 13 or len(card_no) == 16 and card_no[0] == "4":
    print(f"{oldcard_no} is VISA card")

card_no = card_no[::-1]  #Reversing the card # for validation

#__________Getting values for validation__________
for num in card_no[::2]:
    sum_odd_digits += int(num)

for num in card_no[1::2]:
    num = int(num) * 2
    if num >= 10:
        sum_even_digits += (1 + (num % 10))
    else:
        sum_even_digits += num

total = sum_even_digits + sum_odd_digits

#__________Final Validation__________
if total % 10 == 0:
    print(f"Credit card # {oldcard_no} is Valid!")
else:
    print(f"Credit card # {oldcard_no} is Invalid!")
