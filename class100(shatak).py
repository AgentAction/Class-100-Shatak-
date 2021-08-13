class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
       print("Started")

    def stop(self):
        print("Stopped")

    def accelarate(self):
        print("Accelarating")

    def change_gear(self, gear_type):
        print("Gear Changed!")