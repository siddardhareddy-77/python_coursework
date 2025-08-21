'''
class details():

    def __init__(self,name,mail,password):
        self.name = name
        self._mail = mail
        self.__password = password

    def getpassword(self):
        return self.__password
    
    def setpassword(self,new_password):
        self.__password = new_password

shiva = details('sihva','shiva@gmail.com','shiva@123')
print(shiva.name)
shiva.name = 'ram'
print(shiva.name)

print(shiva._mail)
shiva._mail = 'ram@gmail.com'
print(shiva._mail)
'''

'''
class bank():
    def __init__(self):
        self.name = "xyz"
        self._balance = 0

    @property
    def noresbalnce(self):
        return self._balance
    
    @noresbalnce.setter
    def noresbalance(self,amount):
        self._balance+=amount

b = bank()
print(b.noresbalance)
b.noresbalance = 5000
print(b.noresbalance)

print(b.name)
b.name = "abc"
print(b.name)
'''

'''
class status:
    def uploading(self,imageurl):
        self.image = imageurl
        print(f'{self.image} is uploaded to status')

class status1:
    def addcaption(self,text=None):
        self.caption = text
        print(f'{self.caption} is added to status')

class status2(status):
    def like(self):
        self.like =self
        print(f'{self.like} is liked')

class status3(status1,status2):
    def addmusic(self,music):
        self.music = music
        print(f'{self.music} is added to status')

shiva = status()
shiva.uploading('selfie.png')

ram = status1()
ram.addcaption('Hello!!!')
'''

'''
class Insta:
    def __init__(self,username):
        self.username = username
        self.post = []
        print(f'{self.username.center(40,'-')}')

    def uploadpost(self,image):
        self.post.append(image)
        print(f'{image} is posted')

class Insta1(Insta):
    def __init__(self,username,bio):
        super().__init__(username)
        self.bio = bio
        print('bio added')

    def uploadpost(self,post,music):
        super().uploadpost(post)
        self.music = music
        

aa = Insta('aa11')
bb = Insta1('bb22','ss')
'''

'''
class insta:
    def __init(self,username):
        self.username = username
        print(f'{self.username} user is created - P1')

class insta1:
    def __init__(self,username):
        self.username = username
        print(f'{self.username} user is created - P2')

class insta2(insta,insta1):
    def __init__(self,username):
        super().__init__(username)
        print('creating users from V3')

i = insta2('username----asdf')
'''

'''
class normaluser:
    def playvideo(self,name):        
        print(f'\n{name} is playing video with :\n1.Normal Quality\n2.Ads run\n3.No Background Video\n4.Limited Video Download\n5.Music with ads')
    def like(self):
        pass
    def comments(self):
        pass
    def share(self):
        pass
    def title(self):
        pass
    def subscribe(self):
        pass

class premiumuser(normaluser):
    def playvideo(self, name):
        print(f'\n{name} is playing video with : \n1.High Quality\n2.No Ads\n3.Background Video\n4.Unlimitedvideo Download\n5.Music with no Ads')

aa = normaluser()
bb = premiumuser()

aa.playvideo('aa')
bb.playvideo('bb')
'''

'''
class number:
    def __init__(self,n):
        self.n = n

    def __add__(self,other):
        return self.n+other.n
    
    def __sub__(self,other):
        return self.n-other.n

number1 = number(10)
number2 = number(20)

print(number1+number2)
print(number2-number1)
'''

'''
class PostViewer:
    def __init__(self, owner_name,private_account=False):
        self.owner_name = owner_name
        self._private_account = private_account
        self.posts = []
        self.followers = []
    
    def add_post(self, photo_url):
        self.posts.append(photo_url)
        print(f"{self.owner_name} added a new post.")

    def set_privacy(self,private_status):
        self.__private_account = private_status

        if private_status:
            print(f"{self.owner_name}'s account is now Private.")

        else:
            print(f"{self.owner_name}'s account is now Public.")

    def follow(self, follower_name):

        if follower_name not in self.followers: 
            self.followers.append(follower_name) 
            print(f"{follower_name} is now following {self.owner_name}.")
        else:
            print(f"{follower_name} is already following {self.owner_name}.")
    def view_posts(self, viewer_name):
        if not self._private_account or viewer_name in self.followers:
            print(f"Posts by {self.owner_name}:") 
            for post in self.posts:
                print(post)
        else:
            print(f"{self.owner_name}'s account is private. Follow them to view posts.")

aa = PostViewer('aa',True)

aa.add_post('bb')
aa.set_privacy(False)
'''


