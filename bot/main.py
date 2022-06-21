import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token
import httpx

# авторизация
vk_session = vk_api.VkApi(token = main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})

# прослушивание сообщения
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            print(msg)
            id = event.user_id
            URL = f'http://127.0.0.1:4444/get/{msg}'

            r = httpx.get(URL)
            print(r.content.decode())

            sender(id, r.text)


            # if msg in ['привет', 'Привет', 'Здарова', 'здарова', 'Здравствуй', 'здравствуй']:
            #     sender(id, 'здарова')
            # if msg in ['хочу анекдот', 'расскажи анекдот', 'анекдот', 'рассказывай анекдот']:
            #     sender(id, 'Зашёл солдат в деревню, пить захотелось, взрослые все в поле. Спросил пацана. Вынесет попить? Пацан выносит кувшин с квасом. Едренный у вас квас. Осушив всю крынку. А у вас его много? В бочке вчера крыса утонула, мамка полезла доставать, ей ровно по титьки было. Солдат икнул и выронил глиняный кувшин. А малец плачет, а во что я теперь какать буду')
