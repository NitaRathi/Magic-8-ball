import random
import time

response = ['It is certain' , 'It is decidedly so' , 'Without a doubt' , 'YES definitely' , 'As I see it, YES' , 'Most likely',  'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
def Game():

    print('Welcome to Magic 8 ball game')
    print('Ask me a YES or NO question!')
    question = input()
    print('Thinking')
    time.sleep(random.randrange(0,5))
    print(random.choice(response))

while True:
    Game()
    repeat = input('Would you like to continue asking?(Y,N)')
    if not(repeat.lower()=='y'):
        print('You can come back anytime you want')
        break
