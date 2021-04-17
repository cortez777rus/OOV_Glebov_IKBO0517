class Event_bus(object):
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_name, callback):
        if event_name not in self.subscribers.keys():
            self.subscribers[event_name] = [callback]
        else:
            self.subscribers[event_name].append(callback)

    def publish(self, event_name, data):
        if event_name in self.subscribers.keys():
            for callback in self.subscribers[event_name]:
                callback(data)

    def unsubscribe(self, event_name, callback):
        if event_name in self.subscribers.keys():
            self.subscribers[event_name].remove(callback)
            if len(self.subscribers[event_name]) == 0:
                del self.subscribers[event_name]

bus = Event_bus()
callback1 = lambda x: print("call1: " + x)
callback2 = lambda x: print("call2: " + x)

bus.subscribe("first", callback1)
bus.subscribe("first", callback2)
bus.subscribe("second", callback1)
bus.subscribe("second", callback2)

bus.publish("first", "event1")
bus.publish("second", "event2")

bus.unsubscribe("first", callback1)
