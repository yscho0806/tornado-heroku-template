import tornado.ioloop
import tornado.web
import os
# from tornado_swagger.setup import setup_swagger

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        """
        ---
        tags: 
        - Admin 페이지 API
        summary: 특정 음성 데이터 베이스의 전체 길이를 조회합니다.
        description: 데이터베이스 고유 ID를 이용하여 등록된 음성 데이터의 전체 길이를 조회합니다.
        operationId: getDbDur
        requestBody:
          description: 특정 음성 데이터 베이스의 전체 길이를 조회합니다.
          content:
          required: true
        responses:
          '200':
            description: OK
          '400':
            description: Invalid database ID
        """
        self.render("./templates/main/index.html")


def main():
    routes= [
        (r"/", MainHandler)
    ]
    # setup_swagger(routes,swagger_url="/doc")
    application = tornado.web.Application(routes,
        autoreload=True
    )

    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
