    # Credit @harshil8981.
    # Please Don't remove credit.
    # Born to make history @harshil8981 !

    # Thank you MrkillerDeveloper for helping us in this Journey
    # 🥰  Thank you for giving me credit @harshil8981 🥰

    # for any error please contact me -> telegram@Mrkiller_1109 or insta @Mrking_motivational

from pyrogram import Client, filters
from database.users_chats_db import db

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("😔**Sorry ! No thumbnail found...**😔") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**Thumbnail deleted successfully**✅️")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    LazyDev = await message.reply_text("Please Wait ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await LazyDev.edit("**Thumbnail saved successfully**✅️")
	