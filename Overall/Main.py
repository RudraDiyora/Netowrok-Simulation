import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        # Call your function here
        your_function(file_path)
def your_function(file_path):
    print('mymymymymym')
    addIfs(file_path)
    #NetworkTree.connectClinet(NetworkTree, "Test.py")
def addIfs(file_path):
    filepath = "/Users/abc/Desktop/Overall/Network Sim/Clients"
    filelist = os.listdir(filepath)
    checked = []
    file = os.path.basename(file_path)

    client = file
    if not (client in checked):

        with open("Network Sim/requestStarter.txt", "r") as file:
            content = file.read()

        file_name_without_extension = os.path.splitext(client)[0]
        replacemenets = {
            "CLIENT_NAME":f"'{client}'",
            "FILE_NAME":f"{file_name_without_extension}"
        }
        if replacemenets["FILE_NAME"] == ".DS_Store":
            return
        for old, new in replacemenets.items():
            content = content.replace(old, new)


        with open("Network Sim/Requests.py", "a") as r:
            # r.write("\n    ")
            r.write(content)
if __name__ == "__main__":
    path = "/Users/abc/Desktop/Overall/Network Sim"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
