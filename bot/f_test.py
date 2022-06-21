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
        return Response('Улитка заходит в бар, но бармен заявляет: "У нас строгая политика в отношении улиток!" — и ногой выпихивает ее на улицу. Через неделю улитка возвращается в бар и говорит бармену: "Ну и зачем ты это сделал!?"')
    else:
        return Response("неа")

def run():
    uvicorn.run(app, host="127.0.0.1", port = 4444)

if __name__ == "__main__":
    run()