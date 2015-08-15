import logging

from tornado import ioloop
from tornado import web
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer


class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    eventHandler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(eventHandler, "/home/kleptoman/Dokumenty", recursive=True)
    observer.start()
    application.listen(8888)
    ioloop.IOLoop.instance().start()