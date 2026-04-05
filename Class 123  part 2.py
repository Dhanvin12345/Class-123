class Bird:
    def __init__(self):
        print("Bird")
        
    def whoisthis(self):
        print("I am a penguin")

    def swim(self):
        print("swim faster")

class Penguin(Bird):

    def __init__(self):
        super().__init__()

        print("Penguin")

    def whoisthis(self):
        print("I am peggy")

    def run(self):
        print("run faster")

object = Penguin()
object.whoisthis()
object.swim()
object.run()