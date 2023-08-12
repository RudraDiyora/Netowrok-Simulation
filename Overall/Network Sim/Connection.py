class CLIENT:
    TreeData = {
        'TreeIP':None,
        'TreePort':None,
        'TreeFile':"NetworkTree.py"
    }
    Connected = False
    def connect(self, tree):
        self.Connected = True
        import os
        file = os.path.basename(__file__)
        name = file
        tree.clients[name] = True
        print("Connection Success")
