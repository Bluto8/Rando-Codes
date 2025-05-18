# Magic 8 Ball 
import random
question = str(input('Question:'))


Randomnum = random.randint (1,9)
if Randomnum == 1:
    answer = 'Yes - Definitely'
elif Randomnum == 2:
    answer = 'It is decidedly so'
elif Randomnum == 3: 
    answer = 'Without a doubt'
elif Randomnum == 4:
    answer = 'Reply hazy, try again'
elif Randomnum == 5:
    answer = 'Ask again later'
elif Randomnum == 6:
    answer = 'Better not tell you now'
elif Randomnum == 7:
    answer = 'My sources say no'
elif Randomnum == 8:
    answer = 'Outlook not so good'
elif Randomnum == 9:
    answer = 'very doubtful'
else:
    answer = 'Error'

print('Magic 8 ball:'+ answer)
