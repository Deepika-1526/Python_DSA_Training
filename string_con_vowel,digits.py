"""input_string = "f46feLK9y56u#@&56hIjbn6KJhA"
lower_vowels = {'a', 'e', 'i', 'o', 'u'}
upper_vowels = {'A', 'E', 'I', 'O', 'U'}
lower_consonants = set('abcdefghijklmnopqrstuvwxyz') - lower_vowels
upper_consonants = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - upper_vowels
digits = set('0123456789')
special_chars = set(input_string) - (lower_vowels | upper_vowels | lower_consonants | upper_consonants | digits)

lower_vowels_count = 0
upper_vowels_count = 0
lower_consonants_count = 0
upper_consonants_count = 0
digits_count = 0
special_chars_count = 0

for char in input_string:
    if char in lower_vowels:
        lower_vowels_count += 1
    elif char in upper_vowels:
        upper_vowels_count += 1
    elif char in lower_consonants:
        lower_consonants_count += 1
    elif char in upper_consonants:
        upper_consonants_count += 1
    elif char in digits:
        digits_count += 1
    else:
        special_chars_count += 1
print("Lower Vowels:", lower_vowels_count)
print("Upper Vowels:", upper_vowels_count)
print("Lower Consonants:", lower_consonants_count)
print("Upper Consonants:", upper_consonants_count)
print("Digits:", digits_count)
print("Special Characters:", special_chars_count)""" 
input_string = "f46feLK9y56u#@&56hIjbn6KJhA"
uv,uc,lv,lc,d,s=0,0,0,0,0
for i in a:
    if(i.isupper()):
        if(i in 'AEIOU'):
            uv=uv+1
        else:
            uc=uc+1
    elif(i.islower()):
        if(i in 'aeiou'):
            lv=lv+1
        else:
            lc=lc+1
    elif(i.isdigit()):
        d=d+1


