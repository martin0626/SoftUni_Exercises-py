class Email:
    def __init__ (self, sender, reciever, content):
        self.sender = sender
        self.reciever = reciever
        self.content = content
        self.send = False

    def is_sent (self):
        self.send = True

    def get_info (self):
        return f'{self.sender} says to {self.reciever}: {self.content}. Sent: {self.send}'

emails = []
command = input()
while command != 'Stop':
    sender, reciever, content = command.split()
    email = Email(sender, reciever, content)
    command = input()
    emails.append(email)

sended_emails = [int(x) for x in input().split(', ')]
for x in sended_emails:
    emails[x].is_sent()

for email in emails:
    print (email.get_info())






