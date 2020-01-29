from aiohttp import web
import aiohttp_debugtoolbar
from redis_model import *


async def activity(request):
    key = request.match_info.get('key')
    print(key)
    data = get_values(key)
    print(data)

    return web.json_response(str(data))


async def activity_post(request):
    data = await request.json()

    if validate_json_activity(data):
        add_value(data)

    return web.json_response(data)


async def activity_list(request):
    data = get_all_value()
    return web.json_response(str(data))


def validate_json_activity(jsons={}):
    validate = ['activity_type', 'user_id', 'timestamp']
    for i in validate:
        if i not in jsons.keys():
            return False
        else:
            return jsons


app = web.Application()
app.router.add_get('/activity/{key}', activity)
app.router.add_post('/activity_post/', activity_post)
app.router.add_get('/activity_list/', activity_list)

web.run_app(app, port=8002)
