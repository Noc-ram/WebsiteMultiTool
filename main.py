import webbrowser

def print_ascii_art():
    ascii_art = r"""
 █     █░▓█████  ▄▄▄▄     ██████  ██▓▄▄▄█████▓▓█████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒██    ▒ ▓██▒▓  ██▒ ▓▒▓█   ▀    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒█░ █ ░█ ▒███   ▒██▒ ▄██░ ▓██▄   ▒██▒▒ ▓██░ ▒░▒███      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀    ▒   ██▒░██░░ ▓██▓ ░ ▒▓█  ▄    ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
░░██▒██▓ ░▒████▒░▓█  ▀█▓▒██████▒▒░██░  ▒██▒ ░ ░▒████▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒▒ ▒▓▒ ▒ ░░▓    ▒ ░░   ░░ ▒░ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
  ▒ ░ ░   ░ ░  ░▒░▒   ░ ░ ░▒  ░ ░ ▒ ░    ░     ░ ░  ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
  ░   ░     ░    ░    ░ ░  ░  ░   ▒ ░  ░         ░        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
    ░       ░  ░ ░            ░   ░              ░  ░                ░ ░      ░ ░      ░  ░
                      ░                                                                    
   made with love by snxxok on visualstudio
    """
    print(ascii_art)

def open_website(choice):
    urls = {
        '1': 'https://soundcloud.com',
        '2': 'https://www.youtube.com',
        '3': 'https://www.spotify.com',
        '4': 'https://chat.openai.com/chat',
        '5': 'https://www.curseforge.com',
        '6': 'https://store.steampowered.com',
        '7': 'https://github.com',
        '8': 'https://stackoverflow.com',
        '9': 'https://www.wikipedia.org',
        '10': 'https://www.reddit.com',
        '11': 'https://www.netflix.com',
        '12': 'https://www.amazon.com',
        '13': 'https://www.twitter.com',
        '14': 'https://www.linkedin.com',
        '15': 'https://www.duolingo.com',
        '16': 'https://www.khanacademy.org'
    }
    
    if choice in urls:
        webbrowser.open(urls[choice])
    else:
        print("Bro something 1-16")

def main():
    print_ascii_art()
    
    print("Choose a Website:")
    print("1. SoundCloud")
    print("2. YouTube")
    print("3. Spotify")
    print("4. ChatGPT")
    print("5. CurseForge")
    print("6. Steam")
    print("7. GitHub")
    print("8. Stack Overflow")
    print("9. Wikipedia")
    print("10. Reddit")
    print("11. Netflix")
    print("12. Amazon")
    print("13. Twitter")
    print("14. LinkedIn")
    print("15. Duolingo")
    print("16. Khan Academy")
    
    choice = input("Choose a website to open in your browser: ")
    open_website(choice)

if __name__ == "__main__":
    main()
