import tornado.ioloop
import tornado.web
import os
from tornado import util

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("./templates/main/index.html")


def main():
    application = tornado.web.Application([
        (r"/", MainHandler)
    ],
        autoreload=True
    )

    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()