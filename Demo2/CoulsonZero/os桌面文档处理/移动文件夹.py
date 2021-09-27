from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# pip install watchdog if you want to use this package

import os
import jsonpath
import time

class MyHander(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src=folder_to_track+'/'+filename
            new_destination = folder_destination+'/'+filename
            os.rename(src,new_destination)

folder_to_track='/Users/21059/Desktop/myFolder'
folder_destination='/Users/21059/Desktop/newFolder'
event_handler=MyHander()
observer= Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


class KepboardInterrupt(object):
    pass


try:
    while True:
        time.sleep(10)
except KepboardInterrupt:
    observer.stop()
observer.join()
