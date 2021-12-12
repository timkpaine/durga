import sys
import requests
import tornado.ioloop
import tornado.web
from tornado import gen
from .logging import LOG as log
from .utils import parseArgs


class PeerApplication(tornado.web.Application):
    def __init__(self, tracker=None, *args, **kwargs):
        self._t = tracker
        resp = requests.post(self._t, {})
        self._id = resp.text
        log.info("Registered with tracker %s, given id %s", self._t, self._id)
        super(PeerApplication, self).__init__(
            [
                (r"/", PeerHandler),
            ],
            *args,
            **kwargs
        )


class PeerHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("peer")

    @gen.coroutine
    def post(self):
        test = yield print("test")  # to understand coroutines
        log.info(test)
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))


def main(*args, **kwargs):
    application = PeerApplication(kwargs.get("tracker", "http://0.0.0.0:8889/register"))

    port = kwargs.get("port", 8888)

    log.info("Peer listening on port: %s", port)
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    args, kwargs = parseArgs(sys.argv)
    main(*args, **kwargs)
