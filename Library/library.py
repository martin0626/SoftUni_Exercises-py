class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user):
        if user in self.user_records:
            self.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, id, new_username):
        for user in self.user_records:
            if user.user_id == id:
                if user.username != new_username:
                    if user.username in self.rented_books:
                        self.rented_books[new_username] = self.rented_books[user.username]
                        del(self.rented_books[user.username])
                    user.username = new_username
                    return f"Username successfully changed to: {new_username} for userid: {id}"
                else:
                    return "Please check again the provided username - it should be different than the username used so far!"

        return f"There is no user with id = {id}!"