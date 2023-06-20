class Observer:
    def update(self):
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

class ConcreteObserver(Observer):
    def update(self):
        print("Observer notified!")

subject = Subject()
observer = ConcreteObserver()

subject.subscribe(observer)
subject.notify() # Output: "Observer notified!"