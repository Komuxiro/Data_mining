import json
import twitter
from urllib.parse import unquote

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

for _ in range(5):
    print('Length of statuses', len(statuses))
    try:
        next_result = search_result['search_metadata']['next_results']
    except KeyError as e:  # если next_results не определена, значит результатов нет
        break

    # Создадим словарь из next_results, имеющий следующую форму
    # ?max_id = 847960489447628799&q=%23RIPSelena&count=100&include_entities=1

    kwargs = dict([kv.split('=') for kv in unquote(next_result[1:]).split('&')])
    search_result = twitter_api.searche.tweets(**kwargs)

statuses += search_result['statuses']

# Выведем один из полученных результатов, выбрав один элемент из списка

print(json.dumps(statuses[0], indent=1))
