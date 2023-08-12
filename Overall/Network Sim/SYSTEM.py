from Clients import *
import Clients
import os
import Requests
import NetworkHandeler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        # Call your function here
        your_function(file_path)
class NetworkTree:
    clients = {}
    r = None
    TreeInfo = {
        "TreeIP":"123.0.0.1",
        "TreePort":None,
        "Data":"DATA.JSON"
    }

    def __init__(self, name):
        self.name = name
     #   addIfs()

    def add(self):
        addIfs()

    def addClient(self, client):
        self.clients[client] = False
        with open("Network Sim/Clients/"+str(client), "r") as original_file:
            original_content = original_file.read()
        with open("Network Sim/Connection.py", "r") as new_code_file:
            new_code_content = new_code_file.read()
        modified_content = new_code_content + "\n" + original_content
        with open("Network Sim/Clients/"+str(client), "w") as modified_file:
            modified_file.write(modified_content)

        #CLIENT().TreeData["TreeIP"] = self.TreeInfo["TreeIP"]

    def connectClinet(self, client):
        if client in self.clients:
            NetworkHandeler.sendCR(client, self)
        else:
            NetworkHandeler.sendCR(client, self)


    def connectionFailed(self, client):
        print(client)
def your_function(file_path):
   # addIfs()
    NetworkTree("Testing")
    NetworkTree.addClient(NetworkTree, "Test.py")
    print('sup')
    NetworkTree.connectClinet(NetworkTree, "Test.py")
    print(NetworkTree.clients)
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
    path = "/Users/abc/Desktop/Overall/Network Sim/Clients"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print('part 2')

    # print('adsfadf')
    # a = input("file to connect:    ")
    # try:
    #     NetworkTree.connectClinet(NetworkTree, str(a))   
    # except:
    #     print("file does not exist")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
