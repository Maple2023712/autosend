#Import Modules
from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
import json
import random
import os 
import pathlib
import sys

config_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
config_path = os.path.join(config_path, 'config.json')

#Load Config
with open(config_path) as f:
  data = json.load(f)
  for c in data['Config']:
        print('Loading...')
channelids = c['channelids'] #modify this in config.json
token = c['token'] #modify this in config.json
message = c['message'] #modify this in config.json
web = c['web'] #modify this in config.json
header_data = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": token
} 
 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 

def gen_context():
    context_list = [
        "快乐快乐熬夜🎉", "说得好，兄弟!", "活跃起来", "冲冲", "加油卷", "你们不上班吗",
        "有难度", "肝不肝", "好的全部错过", "我要加油了", "兄弟们给我冲，已经干完1个号了", "冲就对了冲就对了",
        "干~！干就一个字~！", "我肝不动了", "肝肝更健康", "别到时候偷偷的掉眼泪", "只有花的时间长才可以的",
        "你们是机器人吗", "燥起来来啊", "是的，马上就快到了，大家一起加油", "感觉外国人没那么卷", "有没有活人啊，说点人话 怎么感觉全是机器人",
        "能坚持下来的人就能拿到结果的"
    ]
    text = random.choice(context_list)
    return text
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v7/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Message Sent") 
            pass 
 
        else: 
            stderr.write(f"HTTP {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
 
def main(): 
	message_data = { 
		"content": gen_context(), 
		"tts": "false"
	} 
	for channelid in channelids:
            send_message(get_connection(), channelid, dumps(message_data)) 
#Keep Alive
if web == "true":
    from keepalive import keep_alive
    keep_alive()
else:
    print("Web Server Disabled")
#Start The Sender
if __name__ == '__main__': 
	while True:    
		main()      
		sleep(random.randrange(150, 200)) #How often the message should be sent (in seconds), every 1 hour = 3600
