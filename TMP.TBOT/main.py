import bot
from services import caching

def main() -> None:
    print('Starting cache thread...')
    caching.initialize()
    
    print('Starting Bot...')
    bot.runner()
    print('Stopped Bot.')
    # caching.dispose()
    # print('Stopped cache thread.')
    

if __name__ == "__main__":
    main()