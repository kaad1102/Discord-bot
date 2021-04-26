import discord
from discord.ext import commands
import asyncio
from discord.utils import find, get
import random
TOKEN = "ODIzNTYxODUxMDgxNTg4NzU2.YFinvg.8X-WKiZeBIClv0qEoMuPWVNxdrc"
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='command_info')
async def command_help(ctx, command):
    if command == '!voice_mute':
        await ctx.send('`С помощью этой команды вы можете заглушить пользователя голосового чата. Требуемая роль:` **admin**')
    if command == '!voice_unmute':
        await ctx.send('`С помощью этой команды вы можете снять заглушку пользоваеля голосового чата. Требуемая роль:` **admin**')
    if command == '!text_mute':
        await ctx.send('`С помощью этой команды вы можете запретить пользователю отправлять сообщения в текстовый чат. Требуемая роль:` **admin**')
    if command == '!text_unmute':
        await ctx.send('`С помощью этой команды вы можете дать пользователю возможность снова писать в текстовый чат. Требуемая роль:` **admin**')
    if command == '!help_me':
        await ctx.send('`С помощью этой команды вы можете узнать информацию о доступных вам возможностях бота.`')
    if command == '!ban':
        await ctx.send('`С помощью этой команды вы можете забанить человека на сервере. Требуемая роль:` **admin**')
    if command == '!unban':
        await ctx.send('`С помощью этой команды вы можете разбанить человека на сервере. Требуемая роль:` **admin**')
    if command == '!kick':
        await ctx.send('`С помощью этой команды вы можете выкинуть человека с сервера. Требуемая роль:` **admin**')
        
@bot.command(name='help_me')
async def help(ctx):
    role_for_check = discord.utils.find(lambda namef: namef.name == 'admin', ctx.message.guild.roles)
    if role_for_check in ctx.author.roles:
        await ctx.send('>>> Доступные вам команды:\n**!help_me** \n**!voice_mute** \n**!voice_unmute** \n**!text_mute** \n**!text_unmute** \n**!ban** \n**!unban** \n**!command_info** \n**!kick**')
    else:
        await ctx.send('>>> Доступные вам команды: \n**!help_me** \n**!command_info**')
@bot.command(name='voice_mute')
async def voice_mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Voice Muted')
    role_for_check = discord.utils.find(lambda namef: namef.name == 'admin', ctx.message.guild.roles)
    if role_for_check in ctx.author.roles:
        await member.add_roles(role)
        await ctx.send(f"**Пользователь {member.mention} был заглушён!**")
    else:
        await ctx.send('`У вас недостаточно прав!`')
    
    
@bot.command(name='voice_unmute')
async def voice_unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Voice Muted')
    role_for_check = discord.utils.find(lambda namef: namef.name == 'admin', ctx.message.guild.roles)
    if role_for_check in ctx.author.roles:
        await member.remove_roles(role)
        await ctx.send(f"**Пользователь {member.mention} снова может говорить!**")
    else:
        await ctx.send('`У вас недостаточно прав!`')
        
        
@bot.command(name='text_mute')
async def text_mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Text Muted')
    role_for_check = discord.utils.find(lambda namef: namef.name == 'admin', ctx.message.guild.roles)
    if role_for_check in ctx.author.roles:
        await member.add_roles(role)
        await ctx.send(f"**Пользователь {member.mention} был заглушён в текстовых чатах!**")
    else:
        await ctx.send('`У вас недостаточно прав!`')
        
        
@bot.command(name='text_unmute')
async def text_unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Text Muted')
    role_for_check = discord.utils.find(lambda namef: namef.name == 'admin', ctx.message.guild.roles)
    if role_for_check in ctx.author.roles:
        await member.remove_roles(role)
        await ctx.send(f"**Пользователь {member.mention} снова может писать в текстовые чаты!**")
    else:
        await ctx.send('`У вас недостаточно прав!`')
        
        
@bot.command(name='ban')
async def ban(ctx, member: discord.Member):
    role_for_check = discord.utils.find(lambda namef: namef.name == 'admin', ctx.message.guild.roles)
    if role_for_check in ctx.author.roles:
        await ctx.send(f"Пользователь **{member}** был забанен")
        await ctx.guild.ban(member)
    else:
        await ctx.send('`У вас недостаточно прав!`')
        
@bot.command(name='unban')
async def unban(ctx, name):
    role_for_check = discord.utils.find(lambda namef: namef.name == 'admin', ctx.message.guild.roles)
    if role_for_check in ctx.author.roles:
        bans = await ctx.guild.bans()
        name_list = ["{0.name}".format(entry.user) for entry in bans]
        list_id = ["{0.id}".format(entry.user) for entry in bans]
        dictf = {}
        for i in range(len(name_list)):
            for y in range(len(list_id)):
                dictf.update({name_list[i]: list_id[y]})
        if name in name_list:
            id = dictf.get(name)
            user = await bot.fetch_user(int(id))
            await ctx.guild.unban(user)
        else:
            await ctx.send('**Этот пользователь не находится в бане!**')
    else:
        await ctx.send('`У вас недостаточно прав!`')
        
        
@bot.command(name='kick')
async def kick(ctx, member: discord.Member):
    role_for_check = discord.utils.find(lambda namef: namef.name == 'admin', ctx.message.guild.roles)
    if role_for_check in ctx.author.roles:    
        await member.kick()
    else:
        await ctx.send('`У вас недостаточно прав!`')
@bot.event
async def on_member_join(member):
    member_id = member.id
    user = bot.get_user(member_id)
    await user.send('Приветствую на Discord сервере "Проверка бота!" Желаю отлично провести время!')
    await bot.process_commands(member)







# КАРТОЧНАЯ ИГРА \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
@bot.command(name='play')
async def play(ctx):
    await ctx.send('`Приветствую вас в карточной игре "Дурак"! Введите команду !ready, чтобы вступить в игру!`')

participants = []
@bot.command(name='ready')
async def ready(ctx):
    roleID = 834798705110417469
    role = discord.utils.get(ctx.guild.roles, id = roleID)
    number = 0
    for member in role.members: #проверяет кол-во пользователей, участвующих в игре
        number += 1
    if number <= 1:
        if ctx.message.author not in participants:
            await ctx.send('**Вы участвуете в игре. Команды для игры: !my_cards - выдает карты, !take - взять карты из колоды, !result - получение результата после двух ходов, !trump - узнать козырь игры.**')
            await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles, name='Участник игры'))
            participants.append(ctx.message.author)
        else:
            await ctx.send('**Вы уже участник!**')
    else:
        await ctx.send('**Вы опоздали, игра уже началась!**')
piki = ['шесть пики', 'семь пики', 'восемь пики', 'девять пики', 'десять пики',
        'валет пики', 'дама пики', 'король пики', 'туз пики']
bubi = ['шесть буби', 'семь буби', 'восемь буби', 'девять буби', 'десять буби',
        'валет буби', 'дама буби', 'король буби', 'туз буби']
chervi = ['шесть черви', 'семь черви', 'восемь черви', 'девять черви', 'десять черви',
         'валет черви', 'дама черви', 'король черви', 'туз черви']
kresti = ['шесть крести', 'семь крести', 'восемь крести', 'девять крести', 'десять крести',
         'валет крести', 'дама крести', 'король крести', 'туз крести']
cards_first_player = []
cards_second_player = []
all_cards = chervi + bubi + piki + kresti
count_1 = 0
count_2 = 0
@bot.command(name='my_cards')
async def cards(ctx):
    roleID = 834798705110417469
    role = discord.utils.get(ctx.guild.roles, id = roleID)
    id_part = [item.id for item in role.members]
    first_participant_id = id_part[0]
    second_participant_id = id_part[1]
    global cards_first_player
    global cards_second_player
    global all_cards
    global count_1
    global count_2
    if ctx.author.id == first_participant_id:
        count_1 += 1
        if count_1 < 2:
            memb = await bot.fetch_user(user_id=ctx.author.id)
            cards_first_player = random.sample(all_cards, 6)
            for x in cards_first_player:
                for z in all_cards:
                    if x == z:
                        all_cards.remove(z)        
            await memb.send('Ваши карты:' + ", ".join(map(str, cards_first_player)))
            await ctx.send('**Карты были выданы. Чтобы походить, введите комманду !throw_1**')
        else:
            memb = await bot.fetch_user(user_id=ctx.author.id)
            await memb.send('Ваши карты:' + ", ".join(map(str, cards_first_player)))
            await ctx.send('**Карты были выданы. Чтобы походить, введите комманду !throw_1**')
    elif ctx.author.id == second_participant_id:
        count_2 += 1
        if count_2 < 2:
            memb1 = await bot.fetch_user(user_id=ctx.author.id)
            cards_second_player = random.sample(all_cards, 6)
            for x in cards_second_player:
                for z in all_cards:
                    if x == z:
                        all_cards.remove(z)
            await memb1.send('Ваши карты:' + ", ".join(map(str, cards_second_player)))
            await ctx.send('**Карты были выданы. Чтобы походить, введите комманду !throw_2**')
        else:
            memb1 = await bot.fetch_user(user_id=ctx.author.id)
            await memb1.send('Ваши карты:' + ", ".join(map(str, cards_second_player)))
            await ctx.send('**Карты были выданы. Чтобы походить, введите комманду !throw_2**')
            
    else:
        await ctx.send('Вы не участвуете в игре!')
kozuri = []
kozurnaya_mast = ''
@bot.command(name='trump')
async def kozurb(ctx):
    global kozuri
    global kozurnaya_mast
    masti = ['черви', 'буби', 'крести', 'пики']
    kozurnaya_mast = random.choice(masti)
    await ctx.send('Козырь игры -' + ' ' + kozurnaya_mast)
    if kozurnaya_mast == 'пики':
        kozuri = ['шесть пики', 'семь пики', 'восемь пики', 'девять пики', 'десять пики',
        'валет пики', 'дама пики', 'король пики', 'туз пики']
    elif kozurnaya_mast == 'буби':
        kozuri = ['шесть буби', 'семь буби', 'восемь буби', 'девять буби', 'десять буби',
        'валет буби', 'дама буби', 'король буби', 'туз буби']
    elif kozurnaya_mast == 'черви':
        kozuri = ['шесть черви', 'семь черви', 'восемь черви', 'девять черви', 'десять черви',
         'валет черви', 'дама черви', 'король черви', 'туз черви']
    elif kozurnaya_mast == 'крести':
        kozuri = ['шесть крести', 'семь крести', 'восемь крести', 'девять крести', 'десять крести',
         'валет крести', 'дама крести', 'король крести', 'туз крести']
        
        
        

@bot.command(name='take')
async def take(ctx):
    roleID = 834798705110417469
    role = discord.utils.get(ctx.guild.roles, id = roleID)
    id_part = [item.id for item in role.members]
    first_participant_id = id_part[0]
    second_participant_id = id_part[1]
    global cards_first_player
    global all_cards
    global cards_second_player
    if len(all_cards) != 0:
        if ctx.author.id == first_participant_id:
            if len(cards_first_player) == 0:
                cd = random.sample(all_cards, 6)
                for i in cd:
                    cards_first_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_first_player) == 1:
                cd = random.sample(all_cards, 5)
                for i in cd:
                    cards_first_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_first_player) == 2:
                cd = random.sample(all_cards, 4)
                for i in cd:
                    cards_first_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_first_player) == 3:
                cd = random.sample(all_cards, 3)
                for i in cd:
                    cards_first_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_first_player) == 4:
                cd = random.sample(all_cards, 2)
                for i in cd:
                    cards_first_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_first_player) == 5:
                cd = random.sample(all_cards, 1)
                for i in cd:
                    cards_first_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_first_player) == 6:
                await ctx.send('**У вас достаточно карт.**')
            
        if ctx.author.id == second_participant_id:
            if len(cards_second_player) == 0:
                cd = random.sample(all_cards, 6)
                for i in cd:
                    cards_second_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_second_player) == 1:
                cd = random.sample(all_cards, 5)
                for i in cd:
                    cards_second_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_second_player) == 2:
                cd = random.sample(all_cards, 4)
                for i in cd:
                    cards_second_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_second_player) == 3:
                cd = random.sample(all_cards, 3)
                for i in cd:
                    cards_second_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_second_player) == 4:
                cd = random.sample(all_cards, 2)
                for i in cd:
                    cards_second_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_second_player) == 5:
                cd = random.sample(all_cards, 1)
                for i in cd:
                    cards_second_player.append(i)
                    all_cards.remove(i)
                await ctx.send(f'Оставшихся карт в колоде: {len(all_cards)}')
            if len(cards_second_player) == 6:
                await ctx.send('**У вас достаточно карт.**')
    else:
        await ctx.send('Колода пуста!')
        
hody = 1
card_value_1 = ''
mast_1 = ''
card_1 = ''
@bot.command(name='throw_1')
async def throw_1(ctx, card, mast):
    roleID = 834798705110417469
    role = discord.utils.get(ctx.guild.roles, id = roleID)
    id_part = [item.id for item in role.members]
    first_participant_id = id_part[0]
    second_participant_id = id_part[1]
    global card_value_1
    global mast_1
    global hody
    global card_1
    global card_2
    if card + ' ' + mast == 'беру карты':
        cards_first_player.append(card_2)
        await ctx.send('`Игрок пасует! Оба игрока бросают карты снова.`')
    else:
        if ctx.author.id == first_participant_id:
            if hody == 1 or hody == 4 or hody == 5 or hody == 8 or hody == 9 or hody == 12 or hody == 13 or hody == 16 or hody == 17 or hody == 20 or hody == 21 or hody ==  24:
                hody += 1
                card_1 = ''
                card_value_1 = card
                card_1 = card + ' ' + mast
                mast_1 = mast
                if card_1 in cards_first_player:
                    cards_first_player.remove(card_1)
                    await ctx.send(f'`Ваш ход был записан.`')
                else:
                    await ctx.send('`У вас нет такой карты!`')
            else: 
                await ctx.send('`Не ваш ход!`')
        else:
            await ctx.send('`Сейчас не ваш ход!`')
        
card_value_2 = ''
mast_2 = ''
card_2 = ''
@bot.command(name='throw_2')
async def throw_2(ctx, card, mast):
    roleID = 834798705110417469
    role = discord.utils.get(ctx.guild.roles, id = roleID)
    id_part = [item.id for item in role.members]
    first_participant_id = id_part[0]
    second_participant_id = id_part[1]
    global card_value_2
    global mast_2
    global hody
    global card_1
    global card_2
    beru = 'беру'
    kartu = 'карты'
    if card + ' ' + mast == beru + ' ' + kartu:
        cards_second_player.append(card_1)
        await ctx.send('`Игрок пасует! Оба игрока бросают карты снова.`')
    else:
        if ctx.author.id == second_participant_id:
            if hody == 2 or hody == 3 or hody == 6 or hody == 7 or hody == 10 or hody == 11 or hody == 14 or hody == 15 or hody == 18 or hody == 19 or hody == 22 or hody == 23:
                hody += 1
                card_2 = ''
                card_value_2 = card
                card_2 = card + ' ' + mast
                mast_2 = mast
                if card_2 in cards_second_player:
                    cards_second_player.remove(card_2)
                    await ctx.send(f'`Ваш ход был записан.`')
                else:
                    await ctx.send('`У вас нет такой карты!`')
            else: 
                await ctx.send('`Не ваш ход!`')
        else:
            await ctx.send('`Сейчас не ваш ход!`')

        
keyses = {'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'валет': 11,
          'дама': 12, 'король': '13', 'туз': 14}
@bot.command(name='result')
async def result(ctx):
    roleID = 834798705110417469
    role = discord.utils.get(ctx.guild.roles, id = roleID)
    id_part = [item.id for item in role.members]
    first_participant_id = id_part[0]
    second_participant_id = id_part[1]    
    global card_value_1
    global mast_1
    global card_value_2
    global mast_2
    global hody
    global all_cards
    global card_1
    global card_2
    global cards_first_player
    global cards_second_player
    global kozurnaya_mast
    if len(cards_first_player) != 0 and len(all_cards) != 0:
        if hody == 3 or hody == 7 or hody == 11 or hody == 15 or hody == 19 or hody == 23 or hody == 27 or hody == 31 or hody == 35 or hody == 39 or hody == 43 or hody == 47:
            if mast_1 == kozurnaya_mast and mast_2 != kozurnaya_mast:
                await ctx.send(f'`{[item.name for item in role.members][1]}, масть должна быть: {kozurnaya_mast}! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)
            elif mast_2 == kozurnaya_mast and mast_1 != kozurnaya_mast:
                await ctx.send('`Бито. Оба игрока бросают карты снова. Взять карты из колоды - !take.`')
            elif int(keyses.get(card_value_1)) < int(keyses.get(card_value_2)) and mast_2 == kozurnaya_mast and mast_1 == kozurnaya_mast:
                await ctx.send('`Бито. Оба игрока бросают карты снова. Взять карты из колоды - !take.`')
            elif int(keyses.get(card_value_1)) > int(keyses.get(card_value_2)) and mast_2 == kozurnaya_mast and mast_1 == kozurnaya_mast:
                await ctx.send(f'`{[item.name for item in role.members][1]}, ваша карта слишком мала! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)
            elif int(keyses.get(card_value_1)) > int(keyses.get(card_value_2)) and mast_1 == mast_2:
                await ctx.send(f'`{[item.name for item in role.members][1]}, ваша карта слишком мала! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)
            elif int(keyses.get(card_value_1)) < int(keyses.get(card_value_2)) and mast_1 == mast_2:
                await ctx.send('`Бито. Оба игрока бросают карты снова. Взять карты из колоды - !take.`')
            elif int(keyses.get(card_value_1)) > int(keyses.get(card_value_2)) and mast_1 != mast_2:
                await ctx.send(f'`{[item.name for item in role.members][1]}, не та масть! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)            
            elif int(keyses.get(card_value_1)) < int(keyses.get(card_value_2)) and mast_1 != mast_2:
                await ctx.send(f'`{[item.name for item in role.members][1]}, не та масть! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)
        else:
            if int(keyses.get(card_value_1)) < int(keyses.get(card_value_2)) and mast_1 == mast_2:
                await ctx.send(f'`{[item.name for item in role.members][0]}, ваша карта слишком мала! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)
            elif int(keyses.get(card_value_1)) > int(keyses.get(card_value_2)) and mast_1 == mast_2:
                await ctx.send('`Бито. Оба игрока бросают карты снова. Взять карты из колоды - !take.`')
            elif int(keyses.get(card_value_1)) > int(keyses.get(card_value_2)) and mast_1 != mast_2:
                await ctx.send(f'`{[item.name for item in role.members][0]}, не та масть! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)            
            elif int(keyses.get(card_value_1)) < int(keyses.get(card_value_2)) and mast_1 != mast_2:
                await ctx.send(f'`{[item.name for item in role.members][0]}, не та масть! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)
                
    elif len(cards_first_player) == 0 and len(all_cards) == 0:
        await ctx.send(f'`{[item.name for item in role.members][0]} выиграл!!! Поздравляю!`')
    elif len(cards_second_player) == 0 and len(all_cards) == 0:
        await ctx.send(f'`{[item.name for item in role.members][1]} выиграл!!! Поздравляю!`')
    elif len(cards_second_player) != 0 and len(all_cards) != 0:
        if hody == 1 or hody == 5 or hody == 9 or hody == 13 or hody == 17 or hody == 21 or hody == 25 or hody == 29 or hody == 33 or hody == 37 or hody == 41 or hody ==  45:
            if int(keyses.get(card_value_1)) > int(keyses.get(card_value_2)) and mast_1 == mast_2:
                await ctx.send(f'`{[item.name for item in role.members][1]}, ваша карта слишком мала! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)
            elif int(keyses.get(card_value_1)) < int(keyses.get(card_value_2)) and mast_1 == mast_2:
                await ctx.send('`Бито. Оба игрока бросают карты снова.`')
            elif int(keyses.get(card_value_1)) > int(keyses.get(card_value_2)) and mast_1 != mast_2:
                await ctx.send(f'`{[item.name for item in role.members][1]}, не та масть! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)            
            elif int(keyses.get(card_value_1)) < int(keyses.get(card_value_2)) and mast_1 != mast_2:
                await ctx.send(f'`{[item.name for item in role.members][1]}, не та масть! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)            
        else:
            if int(keyses.get(card_value_1)) < int(keyses.get(card_value_2)) and mast_1 == mast_2:
                await ctx.send(f'`{[item.name for item in role.members][0]}, ваша карта слишком мала! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)
            elif keyses.get(card_value_1) > keyses.get(card_value_2) and mast_1 == mast_2:
                await ctx.send('`Бито. Оба игрока бросают карты снова. Взять карты из колоды - !take.`')
            elif int(keyses.get(card_value_1)) > int(keyses.get(card_value_2)) and mast_1 != mast_2:
                await ctx.send(f'`{[item.name for item in role.members][0]}, не та масть! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)            
            elif int(keyses.get(card_value_1)) < int(keyses.get(card_value_2)) and mast_1 != mast_2:
                await ctx.send(f'`{[item.name for item in role.members][0]}, не та масть! Оба игрока бросают карты снова.`')
                cards_second_player.append(card_2)
                cards_first_player.append(card_1)
bot.run(TOKEN)
