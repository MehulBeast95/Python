#emoji converter
#message=input(enter)
def emoji_converter(message):
    words = message.split(' ') #converts input message into list of words
#create an emoji dictionery use windows logo key + dot(.) to add emojis
    emojis = {
        ":)" : "😄" ,
        ":(" : " 😥"
        }
    output =''
    for word in words:
        output+=emojis.get(word,word)+" "
    print(output)

message=input('enter the message')
emoji_converter(message)