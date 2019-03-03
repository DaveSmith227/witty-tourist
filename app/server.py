from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import uvicorn, aiohttp, asyncio
from io import BytesIO
from captions import witty_finder
from captions import witty_intro

from fastai import *
from fastai.vision import *

model_file_url = 'https://drive.google.com/uc?export=download&id=1V8lgAAHWM5HP7ezSYRoGgTVSthRPjqUk'
model_file_name = 'wt-stage-4-resnet50-13-classes-256.pkl'
path = Path(__file__).parent

classes = ['the Golden Gate Bridge',
           'the Oakland Bay Bridge',
           'a cable car',
           'Lombard Street',
           'Alcatraz',
           'the Painted Ladies at Alamo Square',
           'the Palace of Fine Arts',
           'the sea lions at Pier 39',
           'the Transamerica Pyramid',
           'Muir Woods',
           'Coit Tower',
           'Fisherman\'s Wharf',
           'Ghirardelli Square'
          ]
          
app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='app/static'))

async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f: f.write(data)

async def setup_learner():
    await download_file(model_file_url, path/model_file_name)
    learn = load_learner(path, model_file_name)
    return learn

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_learner())]
learn = loop.run_until_complete(asyncio.gather(*tasks))[0]
loop.close()

@app.route('/')
def index(request):
    html = path/'view'/'index.html'
    return HTMLResponse(html.open().read())

@app.route('/analyze', methods=['POST'])
async def analyze(request):
    data = await request.form()
    img_bytes = await (data['file'].read())
    img = open_image(BytesIO(img_bytes))
    prediction = learn.predict(img)[0]
    intro = witty_intro()
    witty_caption = witty_finder(prediction)
    return JSONResponse({'intros': intro,'result': str(prediction), 'caption': witty_caption})

if __name__ == '__main__':
    if 'serve' in sys.argv: uvicorn.run(app=app, host='0.0.0.0', port=5042)

