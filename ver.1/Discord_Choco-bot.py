# 모듈 불러오기
import discord
import time
import random
import os
import platform
import json
import numpy as np
#필요한 변수 지정 장소 
botname = ("플로스/ FLOS")
OScheck = platform.system()
회사명_1 = ("더블초코")
회사명_2 = ("더블민트")
#구동부
class chatbot(discord.Client):
    async def on_ready(self):
        # 상태 메시지 설정 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("실행│플로스")
        #계정 상태를 변경한다 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        #OS 구별 하는거 
        if OScheck == ("Windows") :
            os.system('cls')
            print("[플로스 기동]")
            print()
        elif OScheck == ("Linux") :
            os.system('clear')
            print("[플로스 기동]")
            print()
    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        이름 = (message.author.display_name)
        사용자이름 = (message.author.name)
        idname = (message.guild.name)
        if message.author.bot:
            return None

        #봇 설명하기
        if message.content.startswith("플로스"):
            print('----- 봇 실행-----' ) 
            print("이용한 서버>("+ idname +")" " 사용자>("+ 사용자이름 +")"+ (" 실행시간>" + time.strftime('%y년_%m월_%d일_%M분_%S초', time.localtime(time.time()))))
            embed=discord.Embed(title="NAME:"+ botname, description="종류:미니게임 봇", color=0x9ADFB0)
            embed.set_author(name="")
            embed.add_field(name="개발자", value="더블초코", inline=True)
            embed.add_field(name="도움주신분", value="오리들의 모임 맴버들", inline=True)
            embed.add_field(name="명령어 설명은", value='```"+설명"```', inline=False)
            await message.channel.send(embed=embed)

        #설명
        if message.content.startswith("+설명"):
            print("사용자>("+ 사용자이름 +")"+(" 실행시간>" + time.strftime('%y년_%m월_%d일_%M분_%S초', time.localtime(time.time()))))
            embed=discord.Embed(title=":scroll: 명령어 목록:scroll: ", description="<목차>", color=0x00AA18)
            embed.set_author(name="")
            embed.add_field(name="```플로스```", value="봇에 대한 설명", inline=False)
            embed.add_field(name="```+핑```", value="봇 핑", inline=False)
            embed.add_field(name="```+등록```", value="게임에 정보 등록", inline=False)
            embed.add_field(name="```+칭호```", value="상점 불러오기", inline=False)
            embed.add_field(name="```+통장```", value="게임용 통장 불러오기", inline=False)
            embed.add_field(name="```+주식```", value="현재 주식 불러오기", inline=False)
            embed.add_field(name="```+주사위```", value="주사위 돌리기", inline=False)
            embed.add_field(name="```+구매```", value="주식 구매하기", inline=False)
            embed.add_field(name="```+판매```", value="주식 판매하기", inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith("+핑"):
            embed = discord.Embed(title = ':stopwatch: 현재 핑', description = str(client.latency)[0:5] + 'ms', color = 0x00ff00)
            await message.channel.send(embed=embed)
    
        # 게임 개발중
        if message.content.startswith("+게임"):
            print('----- 게임홈실행-----' ) 
            print("사용자>("+ 사용자이름 +")"+ (" 실행시간>" + time.strftime('%y년_%m월_%d일_%M분_%S초', time.localtime(time.time()))))
            embed=discord.Embed(title="**보유중인 TRPG 게임**", description="신작 예정일: 미정", color=0xB700FF)
            embed.set_author(name="목록")
            embed.add_field(name="작품 목록", value="-----------", inline=False)
            embed.add_field(name="작품명", value="```장르:미정```", inline=True)
            await message.channel.send(embed=embed)


        #스토리북 보내기 
        if message.content == "대본1":
            print("사용자>("+ 사용자이름 +")"+(" 실행시간>" + time.strftime('%y년_%m월_%d일_%M분_%S초', time.localtime(time.time()))))
            await message.channel.send("스토리북이 DM으로 보내졌어요!")
            if message.author.dm_channel:
                embed=discord.Embed(title="**작품명**", description="플레이 타임:", color=0x00BBFF)
                embed.set_author(name=" ")
                embed.add_field(name="글쓴이:", value="더블초코", inline=False)
                embed.add_field(name="줄거리", value="줄거리 들어갈곳", inline=True)
                embed.add_field(name="스토리 다운로드", value="----대본링크----", inline=False)
                await message.author.dm_channel.send(embed=embed)
            elif message.author.dm_channel is None:
                channel = await message.author.create_dm()
                embed=discord.Embed(title="**작품명**", description="플레이 타임:", color=0x00BBFF)
                embed.set_author(name=" ")
                embed.add_field(name="글쓴이:", value="더블초코", inline=False)
                embed.add_field(name="줄거리", value="줄거리 들어갈곳", inline=True)
                embed.add_field(name="스토리 다운로드", value="----대본링크----", inline=False)
                await channel.send(embed=embed)


        #프로필
        if message.content.startswith("+통장"):
            print("사용자>("+ 사용자이름 +")"+(" 실행시간>" + time.strftime('%y년_%m월_%d일_%M분_%S초', time.localtime(time.time()))))
            with open('JSON\ '+ 사용자이름 +'.json', 'r') as f:
                json_data = json.load(f)

            player_칭호 = json_data['player']['\uce6d\ud638']
            player_money = json_data['player']['MONEY']
            player_TU1 = json_data['player']['TU_1']
            player_TU2 = json_data['player']['TU_2']
            player_TU3 = json_data['player']['TU_3']

            총주식 = ((player_TU1 +"/"+ player_TU2 +"/"+ player_TU3))

            embed=discord.Embed(title="**이름>**"+ 이름, description="***칭호:***" + player_칭호, color=0x00FFFF)
            embed.set_author(name= 이름 + "의 통장")
            embed.add_field(name="***자금:***", value=player_money + "골드", inline=True)
            embed.add_field(name="***주식:***", value=총주식, inline=True)
            await message.channel.send(embed=embed)
        #주식부분
        if message.content.startswith("+주식"):
            print("사용자>("+ 사용자이름 +")"+ (" 실행시간>" + time.strftime('%y년_%m월_%d일_%M분_%S초', time.localtime(time.time()))))
            with open('JSON\주식.json', 'r+') as f:
                json_data = json.load(f)
            주식1 = json_data['tusik']['tusik1']
            주식2 = json_data['tusik']['tusik2']
            embed=discord.Embed(title=":coin:**주식 거래소**:coin:", description=time.strftime('%y년_%m월_%d일_%M분', time.localtime(time.time())), color=0Xffd700)
            embed.set_author(name=" 더블 초코 주식 거래창")
            embed.add_field(name="***" + 회사명_1 + "***", value= (주식1), inline=False)
            embed.add_field(name="***"+ 회사명_2 + "***", value=(주식2), inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith("+주사위"):
            print("사용자>("+ 사용자이름 +")"+(" 실행시간>" + time.strftime('%y년_%m월_%d일_%M분_%S초', time.localtime(time.time()))))
            time.sleep(1)
            dice = random.randrange(1,9)
            await message.channel.send(":game_die: 주사위>  "+str(dice) )
        
        if message.content.startswith("플로스"):
            ids = message.guild.id
            idname = message.guild.name
            print(ids)
            print(idname)

        if message.content.startswith("+등록"):
            유저아이디 = (message.author.id)
            jack = str(유저아이디)
            player_data = dict()
            player = dict()
            player["NAME"] = jack
            player["칭호"] ="-null-"
            player["MONEY"] ="10000000"
            player["TU_1"] = "0"
            player["TU_2"] = "0"
            player["TU_3"] = "0"
            player["building"] = "0"
            player["COIN_1"] = "0"
            player["COIN_2"] = "0"
            player["COUNT"] = "1"
            player_data["player"] = player
            with open('JSON\ '+ 사용자이름 +'.json', 'w', encoding='utf-8') as make_file:
                json.dump(player_data, make_file, indent="\t")
            await message.channel.send(사용자이름 +" 등록 되었습니다")

        if message.content.startswith("+구매"):
            msg_l = message.content.split()
            try:
                주식량 = msg_l[2]
            except:
                await message.channel.send("+구매 <회사명> <주식의 수>")
                return
            회사명 = msg_l[1]
            if 회사명 == 회사명_1:
                with open('JSON\주식.json', 'r+') as f:
                    json_data = json.load(f)
                주식1_가격 = json_data['tusik']['tusik1']
                전체가격1 = (int(주식량) * int(주식1_가격))
                
                with open('JSON\ '+ 사용자이름 +'.json', 'r') as f:
                    json_data = json.load(f)
                player_칭호 = json_data['player']['\uce6d\ud638']
                플래이어자본 = json_data['player']['MONEY']
                플래이어1주식1 = json_data['player']['TU_2']
                플래이어1주식2 = json_data['player']['TU_3']
                플래이어_건물1 = json_data['player']['building']
                플래이어_코인1 = json_data['player']['COIN_1']
                플래이어_코인2 = json_data['player']['COIN_2']
                결과_1= (int(플래이어자본) - int(전체가격1))
                if 결과_1 <= -1 :
                    await message.channel.send("자금보다 더 많이 구매하실수 없습니다.")
                    return 
                else :
                    await message.channel.send("구매 하셨습니다."+" │현재 자금>"+ str(결과_1) )
                    결과_1= (int(플래이어자본) - int(전체가격1))
                    유저아이디 = (message.author.id)
                    jack = str(유저아이디)
                    player_data = dict()
                    player = dict()
                    player["NAME"] = jack
                    player["칭호"] = player_칭호
                    player["MONEY"] = 결과_1
                    player["TU_1"] = 주식량
                    player["TU_2"] = 플래이어1주식1
                    player["TU_3"] = 플래이어1주식2
                    player["building"] = 플래이어_건물1
                    player["COIN_1"] = 플래이어_코인1
                    player["COIN_2"] = 플래이어_코인2
                    player_data["player"] = player
                    with open('JSON\ '+ 사용자이름 +'.json', 'w', encoding='utf-8') as make_file:
                        json.dump(player_data, make_file, indent="\t")

            elif 회사명 == 회사명_2:
                    with open('JSON\주식.json', 'r+') as f:
                        json_data = json.load(f)
                    주식2_가격 = json_data['tusik']['tusik2']
                    전체가격1 = (int(주식량) * int(주식2_가격))
                    
                    with open('JSON\ '+ 사용자이름 +'.json', 'r') as f:
                        json_data = json.load(f)
                    player_칭호 = json_data['player']['\uce6d\ud638']
                    플래이어자본 = json_data['player']['MONEY']
                    플래이어2주식1 = json_data['player']['TU_1']
                    플래이어2주식2 = json_data['player']['TU_3']
                    플래이어_건물1 = json_data['player']['building']
                    플래이어_코인1 = json_data['player']['COIN_1']
                    플래이어_코인2 = json_data['player']['COIN_2']
                    결과_1= (int(플래이어자본) - int(전체가격1))
                    if 결과_1 <= -1 :
                        await message.channel.send("보유하신 자금보다 더 많이 구매 하실 수 없습니다.")
                        return 
                    else :
                        await message.channel.send("구매 하셨습니다."+" │현재 자금>"+ str(결과_1) )
                        결과_1= (int(플래이어자본) - int(전체가격1))
                        유저아이디 = (message.author.id)
                        jack = str(유저아이디)
                        player_data = dict()
                        player = dict()
                        player["NAME"] = jack
                        player["칭호"] = player_칭호
                        player["MONEY"] = 결과_1
                        player["TU_1"] = 플래이어2주식1 
                        player["TU_2"] = 주식량
                        player["TU_3"] = 플래이어2주식2
                        player["building"] = 플래이어_건물1
                        player["COIN_1"] = 플래이어_코인1
                        player["COIN_2"] = 플래이어_코인2
                        player_data["player"] = player
                        with open('JSON\ '+ 사용자이름 +'.json', 'w', encoding='utf-8') as make_file:
                            json.dump(player_data, make_file, indent="\t")


        if message.content.startswith("+판매"):
            msg_l = message.content.split()
            try:
                판메주식량 = msg_l[2]
            except:
                await message.channel.send("+판매 <회사명> <주식의 수>")
                return
            회사명 = msg_l[1]
            if 회사명 == 회사명_1:
                with open('JSON\주식.json', 'r+') as f:
                    json_data = json.load(f)
                주식1_가격 = json_data['tusik']['tusik1']
                전체가격1 = (int(판메주식량) * int(주식1_가격))
                with open('JSON\ '+ 사용자이름 +'.json', 'r') as f:
                        json_data = json.load(f)
                player_칭호 = json_data['player']['\uce6d\ud638']
                플래이어자본 = json_data['player']['MONEY']
                플래이어2주식1 = json_data['player']['TU_1']
                플래이어2주식2 = json_data['player']['TU_2']
                플래이어2주식3 = json_data['player']['TU_3']
                플래이어_건물1 = json_data['player']['building']
                플래이어_코인1 = json_data['player']['COIN_1']
                플래이어_코인2 = json_data['player']['COIN_2']
                결과_1= (int(플래이어자본) + int(전체가격1))
                주식수 = (int(플래이어2주식1) - int(판메주식량))
                if 주식수 <= -1 :
                    await message.channel.send("보유하신 주식보다 더 많이 판매 하실 수 없습니다.")
                        
                else :
                    await message.channel.send("판매 하셨습니다."+" │현재 자금>"+ str(결과_1) )
                    유저아이디 = (message.author.id)
                    jack = str(유저아이디)
                    player_data = dict()
                    player = dict()
                    player["NAME"] = jack
                    player["칭호"] = player_칭호
                    player["MONEY"] = 결과_1
                    player["TU_1"] = 주식수
                    player["TU_2"] = 플래이어2주식2
                    player["TU_3"] = 플래이어2주식3
                    player["building"] = 플래이어_건물1
                    player["COIN_1"] = 플래이어_코인1
                    player["COIN_2"] = 플래이어_코인2
                    player_data["player"] = player
                    with open('JSON\ '+ 사용자이름 +'.json', 'w', encoding='utf-8') as make_file:
                        json.dump(player_data, make_file, indent="\t")

            elif 회사명 == 회사명_2:
                with open('JSON\주식.json', 'r+') as f:
                    json_data = json.load(f)
                주식_가격 = json_data['tusik']['tusik2']
                전체가격1 = (int(판메주식량) * int(주식_가격))
                with open('JSON\ '+ 사용자이름 +'.json', 'r') as f:
                        json_data = json.load(f)
                player_칭호 = json_data['player']['\uce6d\ud638']
                플래이어자본 = json_data['player']['MONEY']
                플래이어2주식1 = json_data['player']['TU_1']
                플래이어2주식2 = json_data['player']['TU_2']
                플래이어2주식3 = json_data['player']['TU_3']
                플래이어_건물1 = json_data['player']['building']
                플래이어_코인1 = json_data['player']['COIN_1']
                플래이어_코인2 = json_data['player']['COIN_2']
                결과_1= (int(플래이어자본) + int(전체가격1))
                주식수 = (int(플래이어2주식2) - int(판메주식량))
                if 주식수 <= -1 :
                    await message.channel.send("보유하신 주식보다 더 많이 판매 하실 수 없습니다.")
                        
                else :
                    await message.channel.send("판매 하셨습니다."+" │현재 자금>"+ str(결과_1) )
                    유저아이디 = (message.author.id)
                    jack = str(유저아이디)
                    player_data = dict()
                    player = dict()
                    player["NAME"] = jack
                    player["칭호"] = player_칭호
                    player["MONEY"] = 결과_1
                    player["TU_1"] = 플래이어2주식1
                    player["TU_2"] = 주식수
                    player["TU_3"] = 플래이어2주식3
                    player["building"] = 플래이어_건물1
                    player["COIN_1"] = 플래이어_코인1
                    player["COIN_2"] = 플래이어_코인2
                    player_data["player"] = player
                    with open('JSON\ '+ 사용자이름 +'.json', 'w', encoding='utf-8') as make_file:
                        json.dump(player_data, make_file, indent="\t")

        if message.content.startswith("+칭호"):
            msg_l = message.content.split()
            try:
                판메주식량 = msg_l[2]
            except:
                embed=discord.Embed(title="상점 명령어 목록", description="개발중", color=0xB700FF)
                embed.set_author(name=" 더블 초코 칭호 상점")
                embed.add_field(name="*** +칭호 구메 ***", value= ("구메가능한 칭호의 목록을 띄웁니다"), inline=False)
                embed.add_field(name="*** +칭호 목록 ***", value= ("구메한 칭호의 목록을 띄움니다"), inline=False)
                embed.add_field(name="*** +칭호 거래 ***", value= ("소유한 칭호를 거래합니다"), inline=False)
                embed.add_field(name="*** +칭호 제작 ***", value= ("칭호 제작 일정량의 골드를 사용하여 제작합니다"), inline=False)
                await message.channel.send(embed=embed)
                return

if __name__ == "__main__":
    client = chatbot()
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("input TOKEN")
