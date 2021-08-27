def compute_square_area(side_length):
    return pow(side_length, 2)

class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        
        
    def compute_area(self):
        return pow(self, side_length, 2)

    
    
if __name__ == "__main__"
    example_square = Square(15)
    print(example_square.compute_area())

class Email:
    def __init__(self, to, subject, body):
        self.to = to
        self.subject = subject
        self.body = body

    def send(self):
        print("Sending email with subject: {self.subject} and body: {self.body} to: {self.to}")

        
        
if __name__ == "__main__":
    greeting_email = Email("bob@nasa.gov", "Welcome!", "Welcome to epicpython.io!")
    greeting_email.send()
    

























