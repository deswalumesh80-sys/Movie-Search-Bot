from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.Response(text="Movie Search Bot is Live 24/7!")

async def web_server():
    web_app = web.Application()
    web_app.add_routes(routes)
    return web_app
  
