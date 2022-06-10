# 모듈 불러오기
import discord,time,random,os,platform,json
import numpy as np
import os
import sys
import  
#필요한 변수 지정 장소 
botname = ("더블 초코")
OScheck = platform.system()

#구동부
class chatbot(discord.Client):
    async def on_ready(self):
        # 상태 메시지 설정 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("봇")
        #계정 상태를 변경한다 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        #OS 구별 하는거 
        if OScheck == ("Windows") :
            os.system('cls')
            print("[discord bot start]")
            print()
        elif OScheck == ("Linux") :
            os.system('clear')
            print("[discord bot start]")
            print()
    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):

        이름 = (message.author.display_name)
        사용자이름 = (message.author.name)
        idname = (message.guild.name)
        command_make  = (message.content.startswith)

        if message.author.bot:
            return None

        #봇 설명하기
        if command_make("=봇"):
            print('----- 봇 실행-----' ) 
            print("이용한 서버>("+ idname +")" " 사용자>("+ 사용자이름 +")"+ (" 실행시간>" + time.strftime('%y년_%m월_%d일_%M분_%S초', time.localtime(time.time()))))
            embed=discord.Embed(title="NAME:"+ botname, description="한강 물 온도 ", color=0x9ADFB0)
            embed.set_author(name="")
            embed.add_field(name="개발자", value="더블 초코", inline=True)
            embed.add_field(name="도움주신분", value="오리들의 모임", inline=True)
            embed.add_field(name="버전", value='```[2.1.1]```', inline=True)
            embed.add_field(name="명령어 설명은", value='```"+설명"```', inline=False)
            await message.channel.send(embed=embed)


        if message.content.startswith("=핑"):
            embed = discord.Embed(title = ':stopwatch: 현재 핑', description = str(client.latency)[0:5] + 'ms', color = 0x00ff00)
            await message.channel.send(embed=embed)
    

# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("token")
