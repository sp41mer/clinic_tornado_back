import tornado.ioloop
import tornado.web
import json
__author__ = 'sp41mer'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        reply = {
            'lol': 'kek'
        }
        self.write(json.dumps(reply))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

