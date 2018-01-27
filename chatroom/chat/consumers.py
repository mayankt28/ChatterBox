from channels import Group
from .models import session



def ws_connect(message):
    # Add to reader group
    Group("chat_room").add(message.reply_channel)
    # Accept the connection request
    message.reply_channel.send({"accept": True})
    print('websocket --->CONNECTED')

def ws_disconnect(message):
    # Remove from reader group on clean disconnect
    Group("chat_room").discard(message.reply_channel)
    print('websocket --->DISCONNECTED')


def ws_receive(message): 
    Session_info = session()
    user = session.objects.filter(user_id = message.reply_channel)
    if user:
        text = message.content.get('text')
        text = user[0].name +": "+ text
        Group("chat_room").send({
            "text":text
            })
    else:
        Session_info.user_id = message.reply_channel
        Session_info.name = message.content.get('text')
        Session_info.save()
    
        
    
