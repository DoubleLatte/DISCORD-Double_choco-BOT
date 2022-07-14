# 모듈 불러오기
import discord,time,random,os,platform,json
import numpy as np
from hanriver import *
#필요한 변수 지정 장소 
botname = ("더블 초코")
OScheck = platform.system()

#구동부
class chatbot(discord.Client):
    async def on_ready(self):
        # Game | Streaming | CustomActivity
        stm = discord.Streaming("r")
        game = discord.Game("봇")
        await client.change_presence(status=discord.Status.online, activity=game)

        #OS 구별 하는거 
        if OScheck == ("Windows") :
            os.system('cls')
            print("[discord bot start]")
            print()
        else:
            os.system('clear')
            print("[discord bot start]")
            print()
    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):

        Name = (message.author.display_name)
        UserName = (message.author.name)
        IdName = (message.guild.name)
        Command  = (message.content.startswith)
        SendM = (message.channel.send)
        AddEmbed = (embed.add_field)

        if message.author.bot:
            return None

        #봇 설명하기
        if command("=봇"):
            print('----- 봇 실행-----' ) 
            print("이용한 서버>("+ idname +")" " 사용자>("+ 사용자이름 +")"+ (" 실행시간>" + time.strftime('%y년_%m월_%d일_%M분_%S초', time.localtime(time.time()))))
            embed=discord.Embed(title="NAME:"+ botname, description="한강 물 온도 ", color=0x9ADFB0)
            embed.set_author(name="")
            AddEmbed(name="개발자", value="더블 초코", inline=True)
            AddEmbed(name="도움주신분", value="오리들의 모임", inline=True)
            AddEmbed(name="버전", value='```[2.1.1]```', inline=True)
            AddEmbed(name="명령어 설명은", value='```"+설명"```', inline=False)
            await SendM(embed=embed)


        if command("=핑"):
            embed = discord.Embed(title = ':stopwatch: 현재 핑', description = str(client.latency)[0:5] + 'ms', color = 0x00ff00)
            await SendM (embed=embed)
        
        if commmand("=한강"):
            embed = dicord.Embed(title = '한강온도',)   
            await SendM (embed=embed)


if __name__ == "__main__":
    client = chatbot()
    client.run("DiscordBot_token")
