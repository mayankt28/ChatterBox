from channels import Group
from .models import session
from channels.sessions import channel_session
from channels.auth import channel_session_user_from_http,http_session_user,channel_session_user


@channel_session_user_from_http
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

@channel_session_user
def ws_receive(message): 
    text = message.content.get("text")
    text = message.user.first_name +": "+ text
    Group("chat_room").send({'text':text})
  
        
    
