class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.side = 0

    def return_front(self):
        return self.front

    def return_back(self):
        return self.back
