#!/usr/bin/python3 

class ContextManager(object):
    def __init__(self):
        self.entered = False


    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        self.entered = False





if __name__ == "__main__":
    #cm = ContextManager();
    #print("before with: cm.entered = ", cm.entered)

    with ContextManager() as cm:
        print ("inside with: cm.entered = ", cm.entered)

    print("after cm.entered = ", cm.entered)


