class Review:
    def __init__(self, rate, text):
        self.rating = rate
        self.text = text

    def __str__(self):
        return f'rate: {self.rating}, text: {self.text}'
