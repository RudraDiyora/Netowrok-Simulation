import time


def update():
    # Open the file in read mode
    file_path = '/Users/abc/Desktop/Network Sim/Requests.py'
    with open(file_path, 'r') as file:
        content = file.read()

    # Modify the content
    updated_content = content.replace(content, content)

    # Open the file in write mode and write the updated content
    with open(file_path, 'w') as file:
        file.write(updated_content)


def sendCR(client, tree):
    import Requests
    Requests.sendConnectionRequest(client, tree)