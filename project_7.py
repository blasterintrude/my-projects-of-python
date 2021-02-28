class person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("talk")
    


chakri = person("chakradhar")
print(chakri.name)
chakri.talk()