class CredReader(Exception):
    def __init__(self):
        #print("default construcor works")
        self.path = './.env'

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def config(self, key):
        if(len(key)==0):
            raise Error("Key cant be empty")
        else:
            try:
                f = open(self.path, 'r')
            except FileNotFoundError as err:
                print("File not found")
                exit()
            #print(f.name, self.path)
            for line in f:
                if key in line:
                    if (line.index(key)!=0):
                        raise KeyNotFound("Required key does not exist!")
                    else:
                        length = len(line)
                        startIndex = len(key)+2
                        endIndex = length - 1
                        value = line[startIndex:endIndex]
                    #print(f'{line} startIndex:{startIndex}\nendIndex:{endIndex}\nvalue:{value}')
            f.close
            return(value)


class Error(Exception):
    pass

class KeyNotFound(Exception):
    pass