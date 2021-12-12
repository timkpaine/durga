import sys
import tornado.ioloop
import tornado.web
from tornado import gen
from .logging import LOG as log
from .utils import parseArgs, _gen_random


class TrackerHandler(tornado.web.RequestHandler):
    """Tracker Handler
    Extends:
        tornado.web.RequestHandler
    """

    def get(self):
        self.write("trackers")


class TrackerRegisterHandler(tornado.web.RequestHandler):
    """Handler for registering new peers
    Extends:
        tornado.web.RequestHandler
    """

    def initialize(self, peers=None):
        self._peers = peers if peers else {}

    @gen.coroutine
    def post(self):
        # test = yield print('test')  # to understand coroutines
        host = self.request.host
        log.info("New request from %s", host)

        id = _gen_random(self._peers, 0, 10000)
        self._peers[id] = host

        log.info("Registering peer %d from %s", id, host)
        self.set_header("Content-Type", "text/plain")
        self.write(str(id))


class TrackerApplication(tornado.web.Application):
    def __init__(self, trackers=None, peers=None, *args, **kwargs):
        self._trackers = trackers if trackers else []
        self._peers = peers if peers else {}
        super(TrackerApplication, self).__init__(
            [
                (r"/", TrackerHandler),
                (r"/register", TrackerRegisterHandler, {"peers": self._peers}),
            ]
        )


def main(*args, **kwargs):
    port = kwargs.get("port", 8889)
    application = TrackerApplication()
    log.info("Tracker listening on port: %s", port)
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    args, kwargs = parseArgs(sys.argv)
    main(*args, **kwargs)
