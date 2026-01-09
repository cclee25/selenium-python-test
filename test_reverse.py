text = input("Input text: ").strip().lower()

reversed_list = []
converted_list = []

i = len(text) - 1

while i >= 0:
    reversed_list.append(text[i])
    i -= 1

j = 0

while j <= (len(text) - 1):
    converted_list.append(text[j])
    j += 1

if converted_list == reversed_list:
    print("PALINDROME")
else:
    print("NOPE")