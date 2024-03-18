print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

combined_names=name1+name2
lower_names = combined_names.lower()
t =lower_names.count('t')
r =lower_names.count('r')
u =lower_names.count('u')
e =lower_names.count('e')
first_number=t+r+u+e

l =lower_names.count('l')
o =lower_names.count('o')
v =lower_names.count('v')
e =lower_names.count('e')
second_number=l+v+o+e

result=int(str(first_number)+str(second_number))

if result <10 or result >90:
 print(f"Your score is {result}, you go together like coke and mentos.")
elif result >=40 and result <=50 :
 print(f"Your score is {result}, you are alright together.")
else:
 print(f"Your score is {result}.")
