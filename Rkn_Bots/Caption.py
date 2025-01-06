
# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters, errors, types
from config import Rkn_Bots
from datetime import datetime
import asyncio, re, time, sys
from .database import total_user, getid, delete, addCap, updateCap, insert, chnl_ids
from pyrogram.errors import FloodWait

@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN)  & filters.command(["rknusers"]))
async def all_db_users_here(client, message):
    start_t = time.time()
    rkn = await message.reply_text("Processing...")
    uptime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - client.uptime))    
    total_users = await total_user()
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rkn.edit(text=f"**--Bot Processed--** \n\n**Bot Started UpTime:** {uptime} \n**Bot Current Ping:** `{time_taken_s:.3f} ᴍꜱ` \n**All Bot Users:** `{total_users}`")


@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        rkn = await message.reply_text("Bot Processing.\nI am checking all bot users.")
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        await rkn.edit(f"bot ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ started...")
        async for user in all_users:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except errors.InputUserDeactivated:
                deactivated +=1
                await delete({"_id": user['_id']})
            except errors.UserIsBlocked:
                blocked +=1
                await delete({"_id": user['_id']})
            except Exception as e:
                failed += 1
                await delete({"_id": user['_id']})
                pass
            try:
                await rkn.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
            except FloodWait as e:
                await asyncio.sleep(t.x)
        await rkn.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
        
# Restart to cancell all process 
@Client.on_message(filters.private & filters.user(Rkn_Bots.ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    rkn_msg = await b.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=m.chat.id)       
    await asyncio.sleep(3)
    await rkn_msg.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)

    # Assuming Rkn_Bots.RKN_PIC is a valid photo URL or file ID
    await message.reply_photo(
        photo=Rkn_Bots.RKN_PIC,
        caption=f"ʜᴇʏ, {message.from_user.mention}\n\nI ᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴʙᴏᴛ. ᴠᴇʀʏ sɪᴍᴘʟᴇ ᴛᴏ ᴜsᴇ ᴍᴇ. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏᴠᴇʀ ᴛʜᴇʀᴇ. ᴛʜᴇɴ sᴇᴛ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Bʏ Usɪɴɢ <mono>/set</mono> & <mono>/setCaption</mono> Cᴏᴍᴍᴀɴᴅ ғᴏʀ ᴇɴᴀʙʟɪɴɢ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴ.\n\n"
                f"<blockquote>ɴᴏᴛᴇ: Mᴀᴋᴇ sᴜʀᴇ I ᴀᴍ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɡʜᴛs.</blockquote>",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('➕ ADD TO CHANNEL ➕', url=f"https://t.me/{bot.me.username}?startchannel&admin=change_info+post_messages+edit_messages+delete_messages+restrict_members+invite_users+pin_messages+manage_topics+manage_video_chats+anonymous+manage_chat+post_stories+edit_stories+delete_stories")
        ], [
            InlineKeyboardButton('🍃 HELP', callback_data='help_button'),
            InlineKeyboardButton('🍁 ABOUT', callback_data='about_button')
        ]])
    )

# Handle the "HELP" button callback
@Client.on_callback_query(filters.regex('help_button'))
async def help_callback(bot, callback_query):
    help_text = """ •••[( Get Help )]•••

⚠️ ALTER ⚠️
• Add this bot to your channel with all admin permissions.
• Use this command in your channel.
• These commands work only in the channel.
• Keep the file without the forward tag.

•> /set - set a new caption in your channel
•> /del - delete your caption
•> /view - view your caption

Format:
{file_name} = original file name
{file_caption} = original file caption 
{file_size} = file original size       

Eg:- <code>/set
{file_name} or {file_caption}

⚙️ Size » {file_size}

╔═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╗
💥 𝙅𝙊𝙄𝙉 :- channel link 
💥 𝙅𝙊𝙄𝙉 :- channel link
╚═════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ════╝
</code>"""

    await callback_query.message.edit_text(
        help_text,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('🏷️ HTML TAGS', callback_data='html_tags_button'),
            InlineKeyboardButton('🔙 Back', callback_data='start')
        ], [
            InlineKeyboardButton('❌ Close', callback_data='close_help')
        ]]))

# Handle the "HTML TAGS" button callback
@Client.on_callback_query(filters.regex('html_tags_button'))
async def html_tags_callback(bot, callback_query):
    html_tags_text = """🔰 About Caption Font

➢ Bold Text
☞ <code>&lt;b&gt;{filename}&lt;/b&gt;</code>

➢ Spoiler Text
☞ <code>&lt;spoiler&gt;{filename}&lt;/spoiler&gt;</code>

➢ Block Quote Text
☞ <code>&lt;blockquote&gt;{filename}&lt;/blockquote&gt;</code>

➢ Italic Text
☞ <code>&lt;i&gt;{filename}&lt;/i&gt;</code>

➢ Underline Text
☞ <code>&lt;u&gt;{filename}&lt;/u&gt;</code>

➢ Strike Text
☞ <code>&lt;s&gt;{filename}&lt;/s&gt;</code>

➢ Mono Text
☞ <code>&lt;code&gt;{filename}&lt;/code&gt;</code>

➢ Pre Text
☞ <code>&lt;pre&gt;{filename}&lt;/pre&gt;</code>

➢ Hyperlink Text
☞ <code>&lt;a href="https://t.me/RxBotz"&gt;{filename}&lt;/a&gt;</code>"""

    await callback_query.message.edit_text(
        html_tags_text,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('🔙 Back', callback_data='help_button'),
            InlineKeyboardButton('❌ Close', callback_data='close_html_tags')
        ]]))

# Handle "CLOSE" action
@Client.on_callback_query(filters.regex('close_help'))
async def close_help_callback(bot, callback_query):
    await callback_query.message.delete()

@Client.on_callback_query(filters.regex('close_html_tags'))
async def close_html_tags_callback(bot, callback_query):
    await callback_query.message.delete()

# Handle the "ABOUT" button callback
@Client.on_callback_query(filters.regex('about_button'))
async def about_callback(bot, callback_query):
    bot_username = (await bot.get_me()).username  # Ensure the bot's username is fetched here
    ABOUT_TXT = f"""<b><blockquote>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟</blockquote>
    
‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/{bot_username}>{bot_username}</a>
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Infinix_4k'>ʀ'x ʙᴏᴛᴢ</a> 
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]</b>"""
    
    await callback_query.message.edit_text(
        ABOUT_TXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ', url='https://t.me/Drama_hindi_request')
        ], [
            InlineKeyboardButton('🔙 Back', callback_data='start'),
            InlineKeyboardButton('❌ Close', callback_data='close_about')
        ]]))

# Handle "CLOSE" action for ABOUT button
@Client.on_callback_query(filters.regex('close_about'))
async def close_about_callback(bot, callback_query):
    await callback_query.message.delete()

# Handle "BACK" to the main START message
@Client.on_callback_query(filters.regex('start'))
async def back_to_start_callback(bot, callback_query):
    bot_username = (await bot.get_me()).username  # Get the bot's username
    await callback_query.message.edit_caption(
        caption=f"ʜᴇʏ, {callback_query.from_user.mention}\n\nI ᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴʙᴏᴛ. ᴠᴇʀʏ sɪᴍᴘʟᴇ ᴛᴏ ᴜsᴇ ᴍᴇ. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ᴏᴠᴇʀ ᴛʜᴇʀᴇ. ᴛʜᴇɴ sᴇᴛ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Bʏ Usɪɴɢ <mono>/set</mono> & <mono>/setCaption</mono> Cᴏᴍᴍᴀɴᴅ ғᴏʀ ᴇɴᴀʙʟɪɴɢ ᴀᴜᴛᴏᴄᴀᴘᴛɪᴏɴ.\n\n"
                f"<blockquote>ɴᴏᴛᴇ: Mᴀᴋᴇ sᴜʀᴇ I ᴀᴍ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.</blockquote>",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton('➕ ADD TO CHANNEL ➕', url=f"https://t.me/{bot_username}?startchannel&admin=change_info+post_messages+edit_messages+delete_messages+restrict_members+invite_users+pin_messages+manage_topics+manage_video_chats+anonymous+manage_chat+post_stories+edit_stories+delete_stories")
        ], [
            InlineKeyboardButton('🍃 HELP', callback_data='help_button'),
            InlineKeyboardButton('🍁 ABOUT', callback_data='about_button')
        ]]))
    

# Command to set a custom caption
@Client.on_message(filters.command(["set_caption", "set"]) & filters.channel)
async def set_caption(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "<b>Provide a caption to set</b>\n<u>Example:</u> ⬇️\n\n<code>/set_caption {file_name}\n\n{file_caption}\n\nsize » {file_size}\n\nJoin :- @RxBotz</code>"
        )
    chnl_id = message.chat.id
    caption = message.text.split(" ", 1)[1]
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chk_data:
        await updateCap(chnl_id, caption)
        return await message.reply(f"Caption updated successfully:\n\n`{caption}`")
    else:
        await addCap(chnl_id, caption)
        return await message.reply(f"Caption added successfully:\n\n`{caption}`")

# Command to delete a custom caption
@Client.on_message(filters.command(["delcaption", "del_caption", "delete_caption", "del"]) & filters.channel)
async def del_caption(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply("<b>Caption deleted successfully. Default caption will be used.</b>")
    except Exception as e:
        rkn = await msg.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await rkn.delete()

# Extract language from the caption
def extract_language(default_caption):
    language_pattern = r'\b(Hindi|English|Tamil|Telugu|Malayalam|Gujarati|Kannada|Indonesian|Danish|Urdu|Korean|Chinese|Japanese|Hin|Tam|Tel|Ben|Guj|Mal|Mar|Kan|Eng|Kor|Chi|jap)\b'  # Extend with more languages if necessary
    languages = set(re.findall(language_pattern, default_caption, re.IGNORECASE))
    if not languages:
        return "Hindi-English"
    return ", ".join(sorted(languages, key=str.lower))

# Extract year from the caption
def extract_year(default_caption):
    match = re.search(r'\b(19\d{2}|20\d{2})\b', default_caption)
    return match.group(1) if match else None

# Generate greetings based on the current time
def generate_wish():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 17:
        return "Good Afternoon"
    elif 17 <= current_hour < 21:
        return "Good Evening"
    else:
        return "Good Night"

# Command to display HTML tags example
@Client.on_message(filters.command("tags") & filters.channel)
async def tags(bot, message):
    html_tags_text = """🔰 Usᴇ ᴛʜɪs ʜᴛᴍʟ ᴛᴀɢs
➢ Bold Text
☞ <code>&lt;b&gt;{filename}&lt;/b&gt;</code>

➢ Spoiler Text
☞ <code>&lt;spoiler&gt;{filename}&lt;/spoiler&gt;</code>

➢ Block Quote Text
☞ <code>&lt;blockquote&gt;{filename}&lt;/blockquote&gt;</code>

➢ Italic Text
☞ <code>&lt;i&gt;{filename}&lt;/i&gt;</code>

➢ Underline Text
☞ <code>&lt;u&gt;{filename}&lt;/u&gt;</code>

➢ Strike Text
☞ <code>&lt;s&gt;{filename}&lt;/s&gt;</code>

➢ Mono Text
☞ <code>&lt;code&gt;{filename}&lt;/code&gt;</code>

➢ Pre Text
☞ <code>&lt;pre&gt;{filename}&lt;/pre&gt;</code>

➢ Hyperlink Text
☞ <code>&lt;a href="https://t.me/RxBotz"&gt;{filename}&lt;/a&gt;</code>"""
    
    await message.reply(html_tags_text)

# Command to list all available caption placeholders
@Client.on_message(filters.command("placeholders") & filters.channel)
async def list_placeholders(bot, message):
    placeholders_text = """
<b>Available Caption Placeholders:</b>

➢ <code>{file_name}</code> - The name of the file (e.g., movie name, song title, etc.)

➢ <code>{file_size}</code> - The size of the file in human-readable format (e.g., 2.5 MB, 3 GB, etc.)

➢ <code>{file_caption}</code> - The caption of the file (may include word replacements and removals)

➢ <code>{language}</code> - The language(s) extracted from the file name or caption (e.g., English, Hindi, etc.)

➢ <code>{year}</code> - The year extracted from the file name or caption (e.g., 2021, 2019, etc.)

➢ <code>{subtitles}</code> - Display "ESub" or "MSub" based on the presence of subtitles in the file name or caption. If neither is found, it will show nothing.

➢ <code>{wish}</code> - A time-based greeting (e.g., Good Morning, Good Afternoon, Good Evening).

➢ <code>{duration}</code> - The total duration of the media in HH:MM:SS format (e.g., 01:50:34).

<b>Note:</b> Yᴏᴜ ᴄᴀɴ ᴄᴜsᴛᴏᴍɪᴢᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ ᴛᴇᴍᴘʟᴀᴛᴇ ʙʏ ᴜsɪɴɢ ᴛʜᴇsᴇ ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀs ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ғɪʟʟ ɪɴ ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴛʜᴇ ғɪʟᴇ.
For example: <code>{file_name} {year} {language} {subtitles}</code>
"""
    await message.reply(placeholders_text)
    
# Command to list all available bot commands and their usage
@Client.on_message(filters.command("Cmd") & filters.channel)
async def list_commands(bot, message):
    command_list = """
<b>Available Bot Commands:</b>

<code>/rem_words</code> - Set a list of words to be removed from the caption.

<code>/rem_words_off</code> - Turns off the removable words feature for the channel.

<code>/replace_words</code> - Replace a word with another in the channel caption.

<code>/del_replace_word</code> - Disable the word replacement feature.

<code>/view</code> - View the current caption, prefix, suffix, removable words, replace words, and more.

<code>/tags</code> - View a list of HTML tags for text formatting (e.g., Bold, Italic, etc.).

<code>/Cmd</code> - Get a list of available bot commands with descriptions.

<code>/placeholders</code> - View a list of available placeholders and their usage in captions. 
"""
    await message.reply(command_list)

# Command to set words replacement (original word -> replacement word)
@Client.on_message(filters.command("replace_words") & filters.channel)
async def replace_words(bot, message):
    chnl_id = message.chat.id
    if len(message.command) < 3:
        return await message.reply(
            "<b>Provide the word to replace and the word to replace it with</b>\n<u>Example:</u> ⬇️\n\n<code>/replace_words oldword newword</code>"
        )
    
    original_word, replacement_word = message.text.split(" ", 2)[1:]
    
    # Fetch existing data from the database
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chk_data:
        # Update word replacement mapping in the database
        replace_words = chk_data.get("replace_words", [])
        replace_words.append((original_word, replacement_word))
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$set": {"replace_words": replace_words}}
        )
        return await message.reply(f"Word replacement set for this channel ✅: {original_word} -> {replacement_word}")
    else:
        await chnl_ids.insert_one({"chnl_id": chnl_id, "replace_words": [(original_word, replacement_word)]})
        return await message.reply(f"Word replacement set for this channel ✅: {original_word} -> {replacement_word}")


# Command to turn off replace words
@Client.on_message(filters.command("del_replace_word") & filters.channel)
async def del_replace_word(bot, message):
    chnl_id = message.chat.id
    
    try:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$unset": {"replace_words": ""}}
        )
        return await message.reply("Word replacements list has been reset for this channel.")
    except Exception as e:
        rkn = await message.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await rkn.delete()


# Command to view current caption settings
@Client.on_message(filters.command("view") & filters.channel)
async def view_caption(bot, message):
    chnl_id = message.chat.id
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    
    if chk_data:
        current_caption = chk_data.get("caption", "No custom caption set.")
        prefix = chk_data.get("prefix", "None")
        suffix = chk_data.get("suffix", "None")
        removable_words = chk_data.get("removable_words", None)
        replace_words = chk_data.get("replace_words", None)
        
        if removable_words:
            removable_words_text = ", ".join(removable_words)
        else:
            removable_words_text = "None"
        
        if replace_words:
            replace_words_text = ", ".join([f"{original} -> {replacement}" for original, replacement in replace_words])
        else:
            replace_words_text = "None"
        
        return await message.reply(
            f"<b>Channel Details</b>\n\n"
            f"<b>Removable Words:</b> {removable_words_text}\n"
            f"<b>Replace Words:</b> {replace_words_text}\n\n"
            f"<b>Caption Template:</b>\n{current_caption}"
        )
    else:
        return await message.reply("<b>No custom caption set. Using the default caption.</b>")


# Command to set removable words
@Client.on_message(filters.command("rem_words") & filters.channel)
async def rem_words(bot, message):
    chnl_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply(
            "<b>Provide words to remove</b>\n<u>Example:</u> ⬇️\n\n<code>/rem_words test mkv</code>"
        )
    
    words_to_remove = message.text.split(" ", 1)[1]
    words_list = re.findall(r'\S+', words_to_remove)
    
    chk_data = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chk_data:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$set": {"removable_words": words_list}}
        )
        return await message.reply(f"Words to remove set for this channel ✅: {', '.join(words_list)}")
    else:
        await chnl_ids.insert_one({"chnl_id": chnl_id, "removable_words": words_list})
        return await message.reply(f"Words to remove set for this channel ✅: {', '.join(words_list)}")


# Command to turn off removable words
@Client.on_message(filters.command("rem_words_off") & filters.channel)
async def rem_words_off(bot, message):
    chnl_id = message.chat.id
    
    try:
        await chnl_ids.update_one(
            {"chnl_id": chnl_id},
            {"$unset": {"removable_words": ""}}
        )
        return await message.reply("Removable words list has been reset for this channel.")
    except Exception as e:
        rkn = await message.reply(f"Error: {e}")
        await asyncio.sleep(5)
        await rkn.delete()


# Function to format duration in HH:MM:SS
def format_duration(duration_seconds):
    # Ensure that duration is an integer and not a floating-point number
    duration_seconds = int(duration_seconds)  # Cast to integer to discard decimals
    
    hours = duration_seconds // 3600
    minutes = (duration_seconds % 3600) // 60
    seconds = duration_seconds % 60
    
    # Return the formatted duration
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Automatically edit captions for files by removing words, applying replacements, and adding {year}, {language}, {subtitles}, and {duration}
@Client.on_message(filters.channel)
async def auto_edit_caption(bot, message):
    chnl_id = message.chat.id
    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size  # Get file size in bytes

                # Get duration (in seconds) for video or audio
                duration_seconds = getattr(obj, "duration", None)

                # Convert file size to human-readable format
                if file_size < 1024:
                    file_size_text = f"{file_size} B"
                elif file_size < 1024**2:
                    file_size_text = f"{file_size / 1024:.2f} KB"
                elif file_size < 1024**3:
                    file_size_text = f"{file_size / 1024**2:.2f} MB"
                else:
                    file_size_text = f"{file_size / 1024**3:.2f} GB"

                file_name = re.sub(r"@\w+\s*", "", file_name).replace("_", " ").replace(".", " ")

                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                prefix = cap_dets.get("prefix", "")
                suffix = cap_dets.get("suffix", "")
                removable_words = cap_dets.get("removable_words", [])
                replace_words = cap_dets.get("replace_words", [])
                current_caption = cap_dets.get("caption", "")

                # Process word replacements
                for original, replacement in replace_words:
                    file_name = file_name.replace(original, replacement)
                
                # Remove words based on the removable words list
                for word in removable_words:
                    file_name = file_name.replace(word, "")
                
                # Apply prefix and suffix to the caption
                if prefix:
                    file_name = f"{prefix} {file_name}"
                
                if suffix:
                    file_name = f"{file_name} {suffix}"

                # Extract language and year from the file name
                language = extract_language(file_name)  # Extract language from file name
                year = extract_year(file_name)  # Extract year from file name

                # Process word replacements in the caption as well (for {file_caption})
                caption_text = message.caption or "No caption"
                for original, replacement in replace_words:
                    caption_text = caption_text.replace(original, replacement)

                # Remove words from the caption based on removable words list
                for word in removable_words:
                    caption_text = caption_text.replace(word, "")

                # Add time-based wish
                wish = generate_wish()

                # Subtitle Extraction: Check for "ESub" or "MSub"
                subtitles = ""
                if "ESub" in file_name or "ESub" in caption_text:
                    subtitles = "ESub"
                elif "MSub" in file_name or "MSub" in caption_text:
                    subtitles = "MSub"
                
                # Get the duration in HH:MM:SS format if available
                duration_text = ""
                if duration_seconds:
                    duration_text = format_duration(duration_seconds)

                try:
                    replaced_caption = current_caption.format(
                        file_name=file_name,
                        file_size=file_size_text,
                        file_caption=caption_text,  # Updated caption with replacements and removals
                        language=language,
                        year=year,
                        wish=wish,
                        subtitles=subtitles,  # Include subtitles (ESub or MSub)
                        duration=duration_text  # Add the duration placeholder
                    )
                    await message.edit(replaced_caption)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
    return
                
