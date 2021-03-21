import twitter

# Заполнить значениями полученными в API

CONSUMER_KEY = 0
CONSUMER_SECRET = 0
OAUTH_TOKEN = 0
OAUTH_TOKEN_SECRET = 0

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)
'''
Вывод ничего не покажет, кроме того что переменная определена и авторизация продена.
Пример: twitter.api.Twitter object at 0x....
'''
print(twitter_api)

# Получим список актуальных тем

WORLD_WOE_ID = 1  # переменная идентификатор для всего мира
US_WOE_ID = 23424977  # переменная идентификатор для USA

world_trends = twitter_api.trends.place(_ID=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_ID=US_WOE_ID)

# Вычислим пересечение двух множест актуальных тем

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])
common_trends = world_trends_set.intersection(us_trends_set)

print(common_trends)
