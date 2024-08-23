class withdraw737():
	def u():
		u = str(u)
	def com(u):
	    u = str(u)
	    try:
	        amount = int(message.text)
	        bal = float(User.getData('balance'))
	    except:
	        bot.replyText(
	            u, "*❗️ Invalid amount send positive number and without decimals numbers only*", parse_mode="markdown")
	        return

	    if amount < 1:
	        bot.replyText(u, "❗️ *Minimum withdraw amount is 1 ETB*",
	                      parse_mode="markdown")
	        return

	    if amount > float(bal):
	        bot.replyText(u, "❗️ *Amount is bigger than your balance*",
	                      parse_mode="markdown")
	        return

	    # Enter your channel username instead of None
	    payment_channel = "@at_MakeMonyPLC"
	    username = str(Bot.info().username)
	    #u = str(u)
	    amount = str(amount)
	    currency = "ETB"  # Enter your currency instead of None
	    balance = bal-float(amount)
	    User.saveData("balance", balance)

	    if payment_channel != "None":
	        bot.replyText(
	            chat_id=payment_channel,
	            text=f"""
				<b>✅ New Withdraw Paid
				        
				🙅 User :- {u}
				💵 Amount :- </b>{amount}<b> {currency}
				🗽 Status :- Paid
				        
				🤖 Bot link</b> :- @{username}""",
				parse_mode="html"
				        )
	    else:
	        bot.replyText(
	            chat_id=u,
	            text=f"""
			    <b>✅ Withdraw paid 
				        
				🙅 User :- {u}
				💵 Amount :-</b> {amount} <b>{currency}
				🗽 Status :- Paid
				        
				🤖 Bot link</b> :- @{username}""",
		            parse_mode="html"
		        )

	com(u)
class support:
	bot.replyText(
    chat_id=u,
    text="☎️ *Contact us in public group for help* t.me/MakeMonyPLC ",
    parse_mode="markdown"
	)

class setwallet:
	Number = message.text


	def wallet():
	    if Number != int():
	        User.saveData('wallet', message.text)
	        bot.replyText(u, "*🟩 Success*", parse_mode="markdown")

	    else:
	        Bot.replyText(u, "⚠️ Invalid Phone Number")


	wallet()	
class setwallet:
	bot.replyText(u, "♦️ *Send Your Telebir wallet number*", parse_mode="markdown")
	Bot.handleNextCommand("/setwallet")

class withdraw:
	def withdraw():
	    wall = User.getData("wallet")
	    bal = User.getData("balance")

	    Mini_Withdraw = "1"

	    if bal == None:
	        return
	    if wall == None:
	        markup = InlineKeyboardMarkup()
	        markup.add(InlineKeyboardButton(
	            text='✅ Set wallet', callback_data='setwallet'))
	        bot.replyText(u, "<b>❇️ Current wallet:</b> <code>Not set</code>️n<b>‼️ Please set your wallet first For withdraw</b>",
	                      parse_mode="html", reply_markup=markup)
	        return
	    if bal >= 1:
	        bot.replyText(u, "<b>⚠️ Enter amount to withdraw Your   ETB cash.</b>",
	                      parse_mode="html")
	        Bot.handleNextCommand("withdraw737")
	    else:
	        bot.replyText(
	            u, "<i>❌ Your balance low you should have at least "+Mini_Withdraw+" ETB to Withdraw</i>", parse_mode="html")
	        return


	withdraw()

class setwalletbtn:
	wallet = User.getData("wallet")

	markup = InlineKeyboardMarkup()
	markup.add(InlineKeyboardButton(
	              text='⚙️ Set Wallet', 
	              callback_data='setwallet')
	)

	bot.replyText(
	    chat_id = message.chat.id,
	    text = f"""<b>❇️ Current wallet: <code>{wallet}</code>
	🔰 To change wallet click '⚙️ Set wallet' button</b>""",
	    reply_markup = markup,
	    parse_mode = "html"
	)
class stutes:
	users =  str(Bot.getData('total_users'))

	bot.replyText(u, f"*📊 Total bot members*: {users} *users*", parse_mode="markdown")

class service:
	bot.replyText(u, """*This Bot is made by Eyosafit Elias (t.me/Eyosafitelias)

	*Make your Own bot(No Ads and No Downtime) with Simple Python, Join now* Eyosafit Elias (CEO),""")
	parse_mode = "markdown"

class referal:
	per_refer = "5 <i>ETB</i>"
	total_refer = str(User.getData("ref_count"))
	get_bot = "ViralTG_bot"
	u = str(u)
	link = f"https://t.me/{get_bot}?start={u}"
	msg = f"""
	⚡️ <b><u>Per Refer</u></b> = {per_refer}
	👩‍✈️ <b><i>Your Total Refferals</i></b>: {total_refer} <b>users</b>

	➡️ <b><i>Your Referral Link</i></b> = {link}

	⚠️ <b><u>Fake & Cheat Referral Not Pay</u>
	🤑 <i>You Can Get Unlimited LTC By Reffer Your Friends</i></b> 🤑
	"""

	bot.replyText(u, msg, parse_mode="html")
class profile:
	balance = str(User.getData("balance"))
	wallet = str(User.getData('wallet'))
	user = str(u)

	msg = f"""🧕 <b>User</b>: {user}
	🔑 <b>Wallet</b>: <code>{wallet}</code>
	💳 <b>Balance</b>: {balance} <i>(ETB)</i>"""

	bot.replyText(u, msg, parse_mode="html")

class nothing:
	bot.replyText(u, "*❌ Command not found*", parse_mode="markdown")
	bot.replyText(u, """*This Bot is created by Eyosafit Elias (@Eyosafitelias)


	*Make your Own bot(No Ads) with Simple Python, inbox me now  @Eyosafitelias (CEO)""",
	              parse_mode="markdown")

class Join:
	def check():
	    channels = ['@at_MakeMonyPLC', '@MakeMonyPLC']
	    for i in channels:
	        check = bot.getChatMember(str(i), u)
	        if check.status != 'left':
	            pass
	        else:
	            return False
	    return True


	if check() == True:
	    keyboard = ReplyKeyboardMarkup(True)
	    keyboard.row("💻 Profile", "♦️ Referral", "🔧 Set Wallet")
	    keyboard.row("📤 Withdraw", "📊 Stats", "📞 Support")
	    keyboard.row("🚀 About Our Service")
	    bot.replyText(
	        chat_id=message.chat.id,
	        text="*🏡 Main Menu*",
	        reply_markup=keyboard,
	        parse_mode="markdown"
	    )
	else:
	    bot.replyText(u, "*❌ You need to join our channels First.*",
	                  parse_mode="markdown")

class start:
	text = """<b>⛔️ Must Join All Our Channel

	✅  @at_MakeMonyPLC
	✅  @MakeMonyPLC
	❇️ After Joining, Click On '🟢 Joined'</b>"""

	is_invited = User.getData("is_invited")

	u = str(u)
	already = User.getData('bot_user')
	if already != None:
	    passb
	else:
	    User.saveData('balance', 5)
	    User.saveData('ref_count', 0)
	    User.saveData('withdrawn', 0)
	    User.saveData('bot_user', True)
	    if Bot.getData('total_users') == None:
	        Bot.saveData('total_users', 1)
	    else:
	        t = int(Bot.getData('total_users'))+1
	        Bot.saveData('total_users', t)

	# bot.replyText(u, str(Bot.getData('total_users')))

	keyboard = ReplyKeyboardMarkup(True)
	keyboard.row('🟢 Joined')

	refer = message.text.split(" ")

	if message.text == "/start":
	    if is_invited == None:
	        User.saveData('is_invited', True)
	    bot.replyText(
	        chat_id=u,
	        text=text,
	        parse_mode="html",
	        reply_markup=keyboard
	    )
	else:
	    if str(u) == refer[1]:
	        if is_invited == None:
	            User.saveData("is_invited", True)
	        bot.replyText(
	            chat_id=u,
	            text=text,
	            parse_mode="html",
	            reply_markup=keyboard
	        )
	    else:
	        if is_invited == None:
	            refer_balance = User.getData("balance", user=refer[1])
	            count = User.getData('ref_count', user=refer[1])
	            if refer_balance == None:
	                bot.replyText(
	                    chat_id=u,
	                    text="<b>Invalid referral.</b>"
	                )
	            refer_balance = float(refer_balance)
	            refer_balance += 5
	            count = int(count)
	            count += 5
	            bot.replyText(
	                chat_id=refer[1],
	                text=f"<b>🎁 +5 ETB For new Refer</b>",
	                parse_mode="html"
	            )
	            User.saveData("ref_count", data=count, user=refer[1])
	            User.saveData("balance", data=refer_balance, user=refer[1])
	            bot.replyText(
	                chat_id=u,
	                text=f"<b>🎁 You are invited by {refer[1]}</b>",
	                parse_mode="html"
	            )
	        refer_balance = User.getData("balance", user=refer[1])
	        User.saveData("is_invited", True)
	        bot.replyText(
	            chat_id=u,
	            text=text,
	            parse_mode="html",
	            reply_markup=keyboard
	        )

