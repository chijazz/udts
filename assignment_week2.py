# Write 
# 1. A program to revers strings; 
# 2. A program to check if a word is palindrome
# 2. A program to add to fractions and give answers as fractions and (do not use fractions models)

# print('Hi!!!, WELCOME TO REVERSAL WORLD')
# word =input('Enter your word')[::-1]
# print(word)
# print('Thank you for playing reversal world') 

# print('ADDITIONS IN FRACTION')
# A1_nume = float(input('Enter the numerator for 1st fraction :'))
# A1_deno = float(input('Enter the denominator for the 1st fraction :'))
# B2_nume = float(input('Enter the numerator for 2nd fraction :'))
# B2_deno = float(input('Enter the denominator for the 2nd fraction :'))

# if(A1_deno == B2_deno):
#     fraction = A1_nume + B2_nume
#     print(fraction, '/', A1_deno)


# if(A1_deno != B2_deno):
#     fraction = (A1_nume * B2_deno) + (B2_nume * A1_deno)
#     print ('Addition of fractions are :', fraction, '/', A1_deno * B2_deno )


print('WELCOME TO FIND THAT PALINDROME')

word =input('Enter your word')
rword=''.join(reversed(word))
#print(response)
#print(word)
print('PALINDROME is',word in rword)


if word in rword:
    print('Congratulations!!!! YOU WON')

if word not in rword:
    print('OOPS!!!! TRY AGAIN NEXT TIME')