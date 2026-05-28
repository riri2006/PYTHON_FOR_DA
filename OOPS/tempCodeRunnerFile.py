class insta:
    def __init__(self,username, followers):
        self.username = username
        self.followers = followers

    def gain_followers(self, gained):
        self.followers += gained
        print(self.followers)

    def lose_followers(self, lose):
        self.followers -= lose
        print(self.followers)  

    def show_followers(self):  
        print(self.followers) 

m = insta("vedant", 2000)
m.gain_followers(1000)
m.lose_followers(1500)  
m.show_followers()