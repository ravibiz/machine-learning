class Publisher:
    def __init__(self):
        pass

    def register(self):
        pass

    def unregister(self):
        pass

    def notifyAll(self):
        pass


class TechForum(Publisher):

    def __init__(self):
        self.users = []
        self.postname = None

    def register(self, user):
        if user not in self.users:
            self.users.append(user)

    def unregister(self, user):
        self.users.remove(user)

    def notifyAll(self):
        for user in self.users:
            user.notify(self.postname)

    def writeNewPost(self, postname):
        self.postname = postname
        self.notifyAll()


class Subscriber:
    def __init__(self):
        pass

    def notify(self):
        pass


class User1(Subscriber):
    def notify(self, postname):
        print("User1 notified of a new post %s", postname)


class User2(Subscriber):
    def notify(self, postname):
        print("User2 notified of a new post %s", postname)

if __name__ == "__main__":

    techForum = TechForum()
    user1 = User1()
    user2 = User2()

    techForum.register(user1)
    techForum.register(user2)

    techForum.writeNewPost("POST:Command pattern")

    techForum.unregister(user2)

    techForum.writeNewPost("POST:Observer pattern")
