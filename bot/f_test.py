import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()

@app.get('/get/{msg}')
def get_massage(msg):
    if msg == 'привет':
       # msg = 'здарова заебал'
        return Response('здарова')
    if msg == 'хочу анекдот':
        return Response('Зашёл солдат в деревню, пить захотелось, взрослые все в поле. Спросил пацана. Вынесет попить? Пацан выносит кувшин с квасом. Едренный у вас квас. Осушив всю крынку. А у вас его много? В бочке вчера крыса утонула, мамка полезла доставать, ей ровно по титьки было. Солдат икнул и выронил глиняный кувшин. А малец плачет, а во что я теперь какать буду')
    else:
        return Response("неа")

def run():
    uvicorn.run(app, host="127.0.0.1", port = 4444)

if __name__ == "__main__":
    run()