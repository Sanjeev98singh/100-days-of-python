# val = int(input('Enter a digit from 0 to 9: '))
# d = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
# if(val in d):
#     print(d[val])
# else:
#     print('Invalid input. Please enter a digit from 0 to 9.')

val = int(input('Enter a digit from 0 to 9: '))
units = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
tens  = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

ones_digit = val%10
tens_digit = val//10

output = tens[tens_digit] + " " + units[ones_digit]
print(output)