class Airport:
    def __init__(self):
        self.plane = []

    def enqueue(self, plane, priority=False):
        if priority:
            self.plane.insert(0, plane)
        else:
            self.plane.append(plane) 

    def is_empty(self):
        return len(self.plane) == 0

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.plane.pop(0)

air = Airport()
air.enqueue(345)
print("Flight", air.dequeue(), "requests landing")
air.enqueue(190)
print("Flight", air.dequeue(), "requests landing")
air.enqueue(188)
print("Flight", air.dequeue(), "requests takeoff")
air.enqueue(345)
print("CONTROL:", air.dequeue(), "land")
air.enqueue(621)
print("Flight", air.dequeue(), "requests emergency landing")
air.enqueue(621, priority=True)
print("CONTROL:", air.dequeue(), "land")
air.enqueue(511)
print("Flight", air.dequeue(), "requests takeoff")
air.enqueue(190)
print("CONTROL:", air.dequeue(), "land")
air.enqueue(188)
print("CONTROL:", air.dequeue(), "takeoff")
air.enqueue(511)
print("CONTROL:", air.dequeue(), "takeoff")
air.enqueue(810)
print("Flight", air.dequeue(), "requests takeoff")
air.enqueue(810)
print("CONTROL:", air.dequeue(), "takeoff")

