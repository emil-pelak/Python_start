class Widget:
    def __init__(self, label):
        self.label = label

class Button(Widget):
    def __init__(self, label, size):
        super().__init__(label)
        self.size = size

    def handle_click(self):
        return 'Klik!'

b = Button('Ok', (100, 50))
c = Button('Cancel', (200, 100))

print(b.label, b.size)
print(b.handle_click())