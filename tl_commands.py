import hexchat

__module_name__ = "TL Commands"
__module_version__ = "2.8"
__module_description__ = "FLS commonly used commands"
__author__ = 'Piratpalle'


def warn(msg):
    """Print a red, local-only message. Only you see it — it is never sent to the channel."""
    print(f"\x0304{msg}\x0f")


def is_user_in_channel(username):
    """Check if a user is present in the current channel or if we're in a PM"""
    channel = hexchat.get_info('channel')
    
    # If we're in a PM (channel name doesn't start with #), skip check
    if not channel.startswith('#'):
        return True
    
    # In a channel, check if the user is present
    users = hexchat.get_list('users')
    for user in users:
        if user.nick.lower() == username.lower():
            return True
    return False

#------
# Rules
#------
def rules_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /rules <username>")
        return hexchat.EAT_ALL
    
    #username = word[1]
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    response = (
        f"\x0314{username}, Here are a few links to help you get started. "
        "\x02Site Rules\x02: https://wiki.torrentleech.org/doku.php/siterules | "
        "\x02Wiki\x02: http://wiki.torrentleech.org/doku.php | "
        "\x02New User Guide\x02: https://wiki.torrentleech.org/doku.php/newly_invited_users | "
        "\x02How long do I need to seed\x02: http://wiki.torrentleech.org/doku.php/user_classes | "
        "\x02How to maintain a good ratio\x02: https://forums.torrentleech.org/t/how-to-maintain-your-ratio/78082 | "
        "\x02HnR\x02: https://wiki.torrentleech.org/doku.php/hnr | "
        "\x02Our Forum\x02: https://forums.torrentleech.org/ | "
        "\x02Freeleech - (bookmark this - Use it to built ratio)\x02: https://www.torrentleech.org/torrents/browse/index/facets/tags%3AFREELEECH_added%3A%255BNOW%252FMINUTE-10MINUTES%2520TO%2520NOW%252FMINUTE%252B1MINUTE%255D - "
        "Please ensure you give them all a good read!\x03"
    )
    
    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

# Register the command
hexchat.hook_command("rules", rules_cmd, help="/rules <username> - give the user our rules links")

#----------
# Speedtest
#----------
def speedtest_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /speedtest <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL

    # Send the formatted welcome message    
    line1 = (
        f"1.: {username}, Open speedtest.net in a new tab"
    )
    
    line2 = (
        "2.: Run the test and wait for it to complete"
    )
    
    line3 = (
        "3.: Once finished, copy the URL from your browser's address bar (it will look like speedtest.net/result/XXXXXXX)"
    )

    line4 = (
        "4.: Paste that link here"
    )    

    hexchat.command(f"say {line1}")
    hexchat.command(f"say {line2}")
    hexchat.command(f"say {line3}")
    hexchat.command(f"say {line4}")
    return hexchat.EAT_ALL

# Register both commands
hexchat.hook_command("speedtest", speedtest_cmd, help="/speedtest <username> - Request speedtest results")

#--------
# Welcome
#--------
def hi_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /hi <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL    
    
    # Send the formatted welcome message
    response = f"Welcome {username}, Can you please confirm your \x02site username\x02 and explain what the \x02issue\x02 is?"
    
    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

# Register both commands
hexchat.hook_command("hi", hi_cmd, help="/hi <username> - Welcome message")

#------
# Issue
#------
def issue_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /issue <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL    
    
    # Send the formatted welcome message
    response = f"I've forwarded your issue to the mods, {username}, but it looks like they're away. Could you come back later (say, in 3–4 hours) or tomorrow? Whatever works best for you."
    
    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

# Register both commands
hexchat.hook_command("issue", issue_cmd, help="/issue <username> - issue message")

#----
# Bye
#----
def bye_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /bye <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces
    
    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    # Send the formatted welcome message
    response = f"Is there anything else I can help with, {username}? If not, you are free to leave again. Have a good day or evening. You can now \x02close the chat window\x02 or type \x02/part\x02. "
    
    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

# Register both commands
hexchat.hook_command("bye", bye_cmd, help="/bye <username> - Leave message")

#------
# Idler
#------
def idler_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /idler <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces
    
    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    # Send the formatted welcome message
    response = f"Please speak up {username}, if you need assistance. Idling is not allowed in this channel to respect the privacy of other users."
    
    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

# Register both commands
hexchat.hook_command("idler", idler_cmd, help="/idler <username> - Idler message")

#---------
# New User
#---------
def newuser_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /newuser <username>")
        return hexchat.EAT_ALL
    
    #username = word[1]
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    response = (
        f"\x0314{username}, You have been enabled. Here are a few links to help you get started. "
        "\x02Site Rules\x02: https://wiki.torrentleech.org/doku.php/siterules | "
        "\x02Wiki\x02: http://wiki.torrentleech.org/doku.php | "
        "\x02New User Guide\x02: https://wiki.torrentleech.org/doku.php/newly_invited_users | "
        "\x02How long do I need to seed\x02: http://wiki.torrentleech.org/doku.php/user_classes | "
        "\x02How to maintain a good ratio\x02: https://forums.torrentleech.org/t/how-to-maintain-your-ratio/78082 | "
        "\x02HnR\x02: https://wiki.torrentleech.org/doku.php/hnr | "
        "\x02Our Forum\x02: https://forums.torrentleech.org/ | "
        "\x02Freeleech - (bookmark this - Use it to built ratio)\x02: https://www.torrentleech.org/torrents/browse/index/facets/tags%3AFREELEECH_added%3A%255BNOW%252FMINUTE-10MINUTES%2520TO%2520NOW%252FMINUTE%252B1MINUTE%255D - "
        "Please ensure you give them all a good read!\x03"
    )
    
    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

# Register the command
hexchat.hook_command("newuser", newuser_cmd, help="/newuser <username> - welcome message to user")

#---------------
# Ratio Enabled
#---------------
def ratio_cmd(word, word_eol, userdata):
    if len(word) < 3:
        warn("Usage: /ratio <username> <days>")
        return hexchat.EAT_ALL
    
    username = word[1].strip() # Use word[1] and remove any leading/trailing spaces
    days = word[2]

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
    
    # Send the message in parts to avoid line wrapping issues with bold formatting
    line1 = (
        f"{username}, Your account is now enabled. You have {days} days to fix your ratio! "
        "Here are a few links to help you get started. "
        "\002The wiki\002: https://wiki.torrentleech.org/doku.php | "
        "\002New User Guide\002: https://wiki.torrentleech.org/doku.php/newly_invited_users | "
        "\002Common mistakes\002: https://wiki.torrentleech.org/doku.php/common_mistakes | "
        "\002How to maintain a good ratio\002: https://forums.torrentleech.org/t/how-to-maintain-your-ratio/78082 - "
        "Please ensure you give them all "
    )
    
    line2 = (
        "a good read! | "
        "\002Client Related\002: https://seedit4.me/kb/articles/qbittorrent-autobrr-setup/152 | "
        "https://wiki.torrentleech.org/doku.php/autobrr | "
        "https://seedit4.me/kb/articles/optimizing-seedbox-upload-speeds-and-building-ratio/146 | "
        "\002If you have torrents in your client -> Your passkey was reset, so any torrents you still have open in your client will not be able to connect.\002"
    )
    
    line3 = (
        "\002You can redownload the .torrent files from your profile or update them in your client manually.\002"
    )
    
    hexchat.command(f"say {line1}")
    hexchat.command(f"say {line2}")
    hexchat.command(f"say {line3}")
    return hexchat.EAT_ALL

# Register the command
hexchat.hook_command("ratio", ratio_cmd, help="/ratio <username> <days> - ratio notification")

#---------------
# HnR Enabled
#---------------
def hnr_cmd(word, word_eol, userdata):
    if len(word) < 3:
        warn("Usage: /hnr <username> <days>")
        return hexchat.EAT_ALL
    
    username = word[1].strip() # Use word[1] and remove any leading/trailing spaces
    days = word[2]

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
          
    # Send the message in parts to avoid line wrapping issues with bold formatting
    line1 = (
        f"{username}, Your account is now enabled. You have {days} days to fix your HnR! "
        "Here are a few links to help you get started. "
        "\002The wiki\002: https://wiki.torrentleech.org/doku.php | "
        "\002New User Guide\002: https://wiki.torrentleech.org/doku.php/newly_invited_users | "
        "\002Common mistakes\002: https://wiki.torrentleech.org/doku.php/common_mistakes | "
        "\002How to maintain a good ratio\002: https://forums.torrentleech.org/t/how-to-maintain-your-ratio/78082 - "
        "Please ensure you give them all a good read! | "
    )
    
    line2 = (
        "\002Client Related\002: https://seedit4.me/kb/articles/qbittorrent-autobrr-setup/152 | "
        "https://wiki.torrentleech.org/doku.php/autobrr | "
        "https://seedit4.me/kb/articles/optimizing-seedbox-upload-speeds-and-building-ratio/146 | "
        "\002If you have torrents in your client -> Your passkey was reset, so any torrents you still have open in your client will not be able to connect.\002"
    )
    
    line3 = (
        "\002You can redownload the .torrent files from your profile or update them in your client manually.\002"
    )
    
    hexchat.command(f"say {line1}")
    hexchat.command(f"say {line2}")
    hexchat.command(f"say {line3}")
    return hexchat.EAT_ALL

# Register the command
hexchat.hook_command("hnr", hnr_cmd, help="/hnr <username> <days> - ratio notification")

#----------
# Freeleech
#----------
def fl_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /fl <username>")
        return hexchat.EAT_ALL
    
    # Use word[1] instead of word_eol[1] to get just the first argument
    # word_eol[1] includes everything after the command, which adds spaces
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces  

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL    

    line1 = (
        f"{username}, You can find current FREELEECH torrents here: https://www.torrentleech.org/torrents/browse/index/facets/tags%3AFREELEECH_added%3A%255BNOW%252FMINUTE-10MINUTES%2520TO%2520NOW%252FMINUTE%252B1MINUTE%255D It's a good idea to bookmark this link. Remember: FREELEECH torrents still need to be seeded according to the requirements for your user class. You can read more about seeding rules here: http://wiki.torrentleech.org/doku.php/user_classes"
    )
    line2 = (
        "1.: \"popular torrent\" is not what you think it means. For example A torrent can be \"popular\" in terms of times downloaded, but if you download it after most people already have it, you will not get any upload from it. You want to grab a torrent with in 10 minutes after upload, ideally "
    )
    line3 = (
        "2.: Many people use AutoBrr to monitor our announce channel, found here #tlannounces. That way they don't need to manually browse the site, you might want to look into that: https://wiki.torrentleech.org/doku.php/autobrr - more about Autobrr here: https://autobrr.com "
    )
    line4 = (
        "3.: The freeleech link I posted above is a great way to build ratio with. Freeleech torrents uploaded to the site in the past 10 minutes. If the freeleech page is empty, none have been uploaded in the past 10 minutes."
    )

    hexchat.command(f"say {line1}")
    hexchat.command(f"say {line2}")
    hexchat.command(f"say {line3}")
    hexchat.command(f"say {line4}")

    return hexchat.EAT_ALL

# Register the command
hexchat.hook_command("fl", fl_cmd, help="/fl <message> - Freeleech Link")

#------
# Promo
#------
def promo_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /promo <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    line1 = f"{username}, You can use this promoreg: https://www.torrentleech.org/user/account/promoreg"
    
    line2 = f"Before you begin, please make sure to read the full Affiliate Invite Rules and Potential Issues guide, with special attention to Rule #9. You can find it here: https://my.seedit4.me/kb/articles/affiliate-invite-rules-and-potential-issues-to-be-aware-ofAffiliate%20invite%20rules/144"
    

    hexchat.command(f"say {line1}")
    hexchat.command(f"say {line2}")
    return hexchat.EAT_ALL

hexchat.hook_command("promo", promo_cmd, help="/promo <username> - promo registration link")

#--------------------
# Change Mail Address
#--------------------
def chgmail_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /chgmail <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    response = f"{username}, Email change: Send me an PM with the current mail and new mail address: https://www.torrentleech.org/user/messages/index/new/piratpalle"

    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

# Register the command
hexchat.hook_command("chgmail", chgmail_cmd, help="/chgmail <username> - email change instructions")

#---------
# TL Links
#---------
def link_cmd(word, word_eol, userdata):
    # Check if we have at least one argument
    if len(word) < 2:
        warn("Usage: /link <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    response = f"{username}, Here are some usefull links: \002Wiki\002: http://wiki.torrentleech.org/doku.php | \002New User Guide\002: https://wiki.torrentleech.org/doku.php/newly_invited_users | \002How long do I need to seed\002: http://wiki.torrentleech.org/doku.php/user_classes | \002Common Mistakes\002: https://wiki.torrentleech.org/doku.php/common_mistakes | \002How to maintain a good ratio\002: https://forums.torrentleech.org/t/how-to-maintain-your-ratio/78082 | \002Our Forum\002: https://forums.torrentleech.org/ | \002Freeleech - (bookmark this)\002: https://www.torrentleech.org/torrents/browse/index/facets/tags%3AFREELEECH_added%3A%255BNOW%252FMINUTE-10MINUTES%2520TO%2520NOW%252FMINUTE%252B1MINUTE%255D"
    
    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

# Register the command
hexchat.hook_command("link", link_cmd, help="/link <username> - Shows TL links") 

#-------------
# IRC Register
# due to spamming the chan with joins and parts fix your scripts so it does not happen again once the ban is lifted if it does happen again the next ban will be 7 days then 14 then life
#-------------
def irc_cmd(word, word_eol, userdata):
    # Check if we have at least one argument
    if len(word) < 2:
        warn("Usage: /irc <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
    
    intro = f"{username}, here is how to register your iRC nick "
    line1 = "1.: your iRC nickname should be the same as your TL site username. You can set it with \002/nick <site username>\002 (Change <site username>) "
    line2 = "2.: Register your irc nickname : \"\002/msg NickServ REGISTER password email\002\" - You need to replace \"\002password\002\" and \"\002email\002\" "
    line3 = "3.: If you close your client, and rejoins you need to identify to NickServ, first \002/nick <site username>\002 then \"\002/msg NickServ IDENTIFY your_password\002\" "
    line4 = "4.: To join our main channel, #torrentleech. You need to msg TL-Monkey -> \"\002/msg TL-Monkey !invite <YOUR IRCKEY>\002\" How to get IRCKEY, see link below "
    line5 = "More info here : https://wiki.torrentleech.org/doku.php/joining_irc"

    hexchat.command(f"say {intro}")
    hexchat.command(f"say {line1}")
    hexchat.command(f"say {line2}")
    hexchat.command(f"say {line3}")
    hexchat.command(f"say {line4}")
    hexchat.command(f"say {line5}")
    return hexchat.EAT_ALL

# Register the command
hexchat.hook_command("irc", irc_cmd, help="/irc <username> - Shows TL iRC Guides")     
#------
# Slots
#------
def slots_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /slots <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    response = f"{username}, Read more here on how slots works: https://wiki.torrentleech.org/doku.php/slots"

    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

hexchat.hook_command("slots", slots_cmd, help="/slots <username> - slots link")

#----
# HnR
#----
def hnrhelp_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /hnrhelp <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
    
    line1 = "1: You need to clear as many HnR torrents as you can with either surplus or TL-Points! sort your HnR list from smallest to largest (See link to see where to press: https://i.imgur.com/sFnIsDE.png)"
    line2 = "2: Then redownload these big torrents _Which are freeleech_ and seed them properly!"
    line3 = f"3: When you have done steps 1-2, then you can focus on leeching something new! HnR : List : https://www.torrentleech.org/profile/{username}/hnr -> You need to use ALL your Surplus first and then TL-Points until all is used or HnR page is empty! <-"
    line4 = f"{username}, Read more here on how HnR works: https://wiki.torrentleech.org/doku.php/hnr"

    hexchat.command(f"say {line1}")
    hexchat.command(f"say {line2}")
    hexchat.command(f"say {line3}")
    hexchat.command(f"say {line4}")
    return hexchat.EAT_ALL

hexchat.hook_command("hnrhelp", hnrhelp_cmd, help="/hnrhelp <username> - hnr link")

#-----------------------
# User class and seeding
#-----------------------
def class_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /class <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    response = f"{username}, Read more here on how User classes works: http://wiki.torrentleech.org/doku.php/user_classes"

    hexchat.command(f"say {response}")
    return hexchat.EAT_ALL

hexchat.hook_command("class", class_cmd, help="/class <username> - user class link")

#-------------
# Image upload
#-------------
def imgur_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /imgur <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
        
    line1  = f"{username}, You can share image(s) with us, by uploading it to: https://imgur.com/upload"
    line2 = "After you have uploaded the image(s), share the URL here in the channel or in PM"

    hexchat.command(f"say {line1}")
    hexchat.command(f"say {line2}")
    return hexchat.EAT_ALL

hexchat.hook_command("imgur", imgur_cmd, help="/imgur <username> - upload of images")

#--------
# Pending
#--------
def pending_cmd(word, word_eol, userdata):
    if len(word) < 2:
        warn("Usage: /pending <username>")
        return hexchat.EAT_ALL
    
    username = word[1].strip()  # Use word[1] and remove any leading/trailing spaces

    # Check if user is in channel
    if not is_user_in_channel(username):
        warn(f"Error: User '{username}' is not in the channel")
        return hexchat.EAT_ALL
    
    line1 = "1: Open an incognito window"
    line2 = "2: Copy the link from the email you just received"
    line3 = "3: Paste it into the incognito window"

    hexchat.command(f"say {line1}")
    hexchat.command(f"say {line2}")
    hexchat.command(f"say {line3}")
    return hexchat.EAT_ALL

hexchat.hook_command("pending", pending_cmd, help="/pending <username> - confirm pending account")

#---------
# Commands list
#---------
def cmds_cmd(word, word_eol, userdata):
    own_nick = hexchat.get_info('nick')
    
    # Open a query window with yourself
    hexchat.command(f"QUERY {own_nick}")
    
    # Find the query context and print into it
    ctx = hexchat.find_context(channel=own_nick)
    if ctx:
        ctx.prnt("=== TL Commands ===")
        ctx.prnt("/rules <user>     - Site rules + links")
        ctx.prnt("/hi <user>        - Welcome message")
        ctx.prnt("/bye <user>       - Leave/close message")
        ctx.prnt("/issue <user>     - Forward issue to mods")
        ctx.prnt("/idler <user>     - Warn idler")
        ctx.prnt("/speedtest <user> - Request speedtest")
        ctx.prnt("/newuser <user>   - New user welcome + links")
        ctx.prnt("/ratio <user> <days>  - Ratio enabled message")
        ctx.prnt("/hnr <user> <days>    - HnR enabled message")
        ctx.prnt("/hnrhelp <user>   - HnR help steps")
        ctx.prnt("/fl <user>        - Freeleech info")
        ctx.prnt("/chgmail <user>   - Email change instructions")
        ctx.prnt("=== General Information ===")
        ctx.prnt("/link <user>      - Useful TL links")
        ctx.prnt("/irc <user>       - IRC registration guide")
        ctx.prnt("/slots <user>     - Slots info link")
        ctx.prnt("/class <user>     - User class info link")
        ctx.prnt("/promo <user>     - Promo registration link")        
        ctx.prnt("/imgur <user>     - Image upload instructions")
        ctx.prnt("/pending <username> - confirm pending account")
        ctx.prnt("===================")
    return hexchat.EAT_ALL

hexchat.hook_command("cmds", cmds_cmd, help="/cmds - List all TL commands")