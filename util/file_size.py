# Credit @harshil8981.
# Please Don't remove credit.
# Born to make history @harshil8981 !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @harshil8981  🥰
# for any error please contact me -> telegram@Mrkiller_1109 or insta @Mrking_motivational 
# rip paid developers 🤣 - >> No need to buy paid source code while @Mrkiller_1109 is here 😍😍
def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    """ Returns a human readable string representation of bytes """
    return str(bytes) + units[0] if int(bytes) < 1024 else human_size(int(bytes)>>10, units[1:])
