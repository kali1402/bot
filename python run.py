import asyncio
import discord
import random

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NzMwMDc5NTQ2OTI5NDQ3MDEy.Xwdb9g.FRscnD-HMoj0Ea3_RBUVdySRwOY"

# 봇이 구동되었을 때 보여지는 코드
# @client.event
# async def on_ready():
#     print("다음으로 로그인합니다")
#     print(client.user.name)
#     print(client.user.id)
#     print("================")


# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    유저첫문장채팅 = message.content.startswith
    유저채팅 = message.content
    봇채팅 = message.channel.send

    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if 유저첫문장채팅('!명령어'):
        embed = discord.Embed(
            title="안녕하세요! Skin봇입니다.", description="명령어들은 아래에서 보실 수 있습니다.\n건의할사항은 Skin Essentials#3571 으로 디엠주세요.", color=0x62c1cc)
        embed.add_field(
            name="인터넷", value="`!네이버`, `!구글`, `!유튜브`", inline=False)
        embed.add_field(
            name="미니게임", value="`!가위바위보 도움말`, `![가위,바위,보]`, `!강화 도움말`, `!강화 [확률]`", inline=False)
        await 봇채팅(embed=embed)

    # 가위바위보
    if 유저채팅 == "!가위바위보 도움말":
        await 봇채팅("가위바위보를 시작할려면 ex) !가위 (가위,바위,보 중에 선택하세요)")

    elif 유저첫문장채팅("!"):
        플레이어가위바위보 = 유저채팅.split("!")[1]
        if 플레이어가위바위보 == "가위" or 플레이어가위바위보 == "바위" or 플레이어가위바위보 == "보":
            봇가위바위보랜덤 = random.randint(1, 3)
            if 봇가위바위보랜덤 == 1:  # 봇이 가위를 낸 경우,
                봇가위바위보 = "가위"
            elif 봇가위바위보랜덤 == 2:
                봇가위바위보 = "바위"
            else:
                봇가위바위보 = "보"

            await 봇채팅("플레이어 : "+플레이어가위바위보+"\n봇 : "+봇가위바위보)

    # 강화
    if 유저첫문장채팅("!강화"):
        강화 = random.randint(1, 100)
        강화확률 = 유저채팅.split(" ")[1]

        await 봇채팅("강화확률 "+강화확률+"%")

        if (강화 < int(강화확률)):
            await 봇채팅(강화확률+"% 강화에 성공하셨습니다.")
        else:
            await 봇채팅(강화확률+"% 강화에 실패하셨습니다.")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='!명령어'))

client.run(token)
