import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['GET','POST'])
def sms_reply():
    body = request.values.get('Body', None).lower()

    resp = MessagingResponse()

    if 'hi' in body:
        msg = resp.message('Welcome to Winter Riddles. We are going to play a game. You have 100 riddles to answer to receive your gift. For every riddle you get wrong, you will lose 1% of that gift which will be donated to charity through crypto currency. Just kidding...haha. Good luck. Send the name of your favorite brother to start your first riddle.')
        msg.media('https://media.giphy.com/media/l3vR4Gx1wLssrskRa/giphy.gif')
    elif 'sheldon' in body:
        msg = resp.message('100 riddles to go. What lives in winter, dies in summer, and grows with its roots upward?')
    elif 'icicle' in body:
        msg = resp.message("Correct, 99 riddles to go! I am a drink that is made when you're cold. Some add marshmallows no matter if young or old. What am I?")
        msg.media('https://media.giphy.com/media/VBEd4PzBjdG3S/giphy-downsized.gif')
    elif 'hot chocolate' in body:
        msg = resp.message("Correct, 98 riddles to go! You can catch me easily, especially around Christmas time, but you can never throw me. What am I?")
        msg.media('https://media.giphy.com/media/l3vR6JC7NZZgTpmWQ/giphy-downsized.gif')
    elif 'cold' in body:
        msg = resp.message("Correct 97 riddles to go! In the winter when you're cold you come be me to warm your toes. What am I?")
        msg.media('https://media.giphy.com/media/3o7ZeCHGCq8vJgj4GY/giphy-downsized.gif')
    elif 'fire' in body:
        msg = resp.message("Correct! Isn't this so much fun!! I can drift, lift, swirl, and fall; but only in the winter or not at all. I can get big, but I’m usually small. I can appear when the weather is either wild or tame. I have a million brothers and sisters, but we never look the same. What am I?")
        msg.media('https://media.giphy.com/media/Jo75g5HXkwpESvld1E/giphy-downsized.gif')
    elif 'snowflake' in body:
        msg = resp.message("Correct! Please rank the fun of this activity from a 1-5?")
        msg.media('https://media.giphy.com/media/3o7TKWrn9zfNhUnbLa/giphy-downsized.gif')
    elif '1' in body:
        msg = resp.message("Really......")
        msg.media('https://media.giphy.com/media/eh7W3dJGvRa4FymAPf/giphy-downsized.gif')
    elif '5'in body:
        msg = resp.message("Correct!, what is your favorite activity to do on a snowy mountain?")
        msg.media('https://media.giphy.com/media/3og0IxZOnkznTxmwjC/giphy-downsized.gif')
    elif 'ski' in body:
        msg = resp.message("Correct go to your favorite brother to receive your gift and merry christmas!")
        msg.media('https://media.giphy.com/media/8p61R8vQrihPJKYo1L/giphy-downsized.gif')
    else:
        msg = resp.message("hmmm are you sure about that?")
        msg.media('https://media.giphy.com/media/3jN3GziOKUEmI/giphy-downsized.gif')

    return str(resp)

if __name__ == '__main__':
    app.run()
