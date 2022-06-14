import warnings
from telethon import TelegramClient
from pytgcalls import GroupCallFactory
from telethon.tl.functions.channels import JoinChannelRequest
import pafy
from pytgcalls.exceptions import GroupCallNotFoundError

print("Youtube to Telegram Voice Chat BOT -- Make sure you have the libraries installed\n")
warnings.filterwarnings('ignore')
client = TelegramClient('Newuser',api_hash='c573ce027d06821ba4d79c288b8b5dc4',api_id="8230543").start()
groupcall = GroupCallFactory(client,GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON).get_group_call()
while True:
    channel = input("Enter Group Username(Public) : ")
    url = input("Enter Youtube link : ")

    video = pafy.new(url)
    stream = video.streams[0].url

    async def main():
        try: 
            chat = await client.get_entity(channel)
            await client(JoinChannelRequest(channel))
            await groupcall.join(channel)
            await groupcall.start_video(stream)
            print("Video Streaming has started , press ctrl + c to exit")
            await client.run_until_disconnected()
        except GroupCallNotFoundError:
            print("Group Call not started , please try again") 
    client.loop.run_until_complete(main())        
    continue  
    


