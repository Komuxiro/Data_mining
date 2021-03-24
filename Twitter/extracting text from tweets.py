import json
import twitter
from collections import Counter
from urllib.parse import unquote


# Сщздадим функции для оценки лексического разнообразия твитов
# Функция для вычисления лексического разноообразия
def lexical_diversity(tokens):
    return len(set(tokens)) / len(tokens)


# Функция для вычисления среднего числа слов в твите
def average_words(statuses):
    total_words = sum([len(s.split()) for s in statuses])
    return total_words / len(statuses)


# Заполнить значениями полученными в API

CONSUMER_KEY = 0
CONSUMER_SECRET = 0
OAUTH_TOKEN = 0
OAUTH_TOKEN_SECRET = 0

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

# Переменной присвоим тег по которому будет искать твиты

q = '#MentionSomeoneImportantForYou'
count = 100

search_result = twitter_api.search.tweets(q=q, count=count)
statuses = search_result['statuses']

status_text = [status['text'] for status in statuses]
screen_names = [user_mention['screnn_name'] for status in statuses
                for user_mention in status['entities']['user_mentions']]
hashtags = [hashtag['text'] for status in statuses
            for hashtag in status['entities']['hashtags']]

# Получим коллекцию всех слов из всех твитов

words = [w for t in status_text for w in t.split()]

# Извлечем первые 5 элементов из каждой коллекции
print(json.dumps(status_text[0:5], indent=1))
print(json.dumps(screen_names[0:5], indent=1))
print(json.dumps(hashtags[0:5], indent=1))
print(json.dumps(words[0:5], indent=1))

# Проведем частотный анализ слов
for item in [words, screen_names, hashtags]:
    c = Counter(item)
    print(c.most_common()[:10])  # выведем топ 10
    print()

# Выведем результат функций
print(lexical_diversity(words))
print(lexical_diversity(screen_names))
print(lexical_diversity(hashtags))
print(lexical_diversity(status_text))
