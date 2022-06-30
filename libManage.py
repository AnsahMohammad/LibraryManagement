from time import time
class library:
    __books = []
    __users = {}
    __admin = {"God":123}
    __login = 0
    __adminOnline = 0
    __registerLog = {}
    present_user = None
    __borrowed = {}
    __borrowedHistory = {}

    def __init__(self, name, books,admin="God",pass_=123):
      self.name = name
      self.__books = books
      self.__admin[admin] = pass_
      print("Library deployed successfully! ")

    def __log(self,user,book,action):
        localLog = [book,action,time()]
        if user in list(self.__registerLog.keys()):
          k = self.__registerLog[user]
          k.append(localLog)
          self.__registerLog[user] = k
        else:
          self.__registerLog[user] = [self.present_user]

    def signup(self,username,password):
      if username in list(self.__users.keys()):
        print("username already exist")
        return 0
      else:
        self.__users[username] = password
        self.__registerLog[username] = [] 
        print("signup successful ")
        return 1

    def login(self,name,password):
      if self.__users[name] == password:
        print("Login success")
        self.present_user = name
        self.__login = 1
        return 1
      else:
        return 0

    def AdminLogin(self,name,password):
      if self.__admin[name] == password:
        self.__adminOnline = 1
        self.__login = 0
        self.present_user = name
        print("Loggined as Admin-{} Successfully ".format(name))
      else:
        print("Authentication Failed")

    def Logout(self):
      print("{} logged out Successfully".format(self.present_user))
      self.__adminOnline = 0
      self.present_user = None
      self.__login = 0

    def addbook(self,book):
      if self.__login == 1:
        if book in self.__books:
          print("sorry, the book is already here! ")
          return 0
        else:
          self.__books.append(book)
          print("Book '"+book+"' has been added successfully")
          self.__log(self.present_user,book,"added")
          return 1
      else:
        print("you're not Logged-in")
        return 0

    def importBooks(self,books):
      if self.__adminOnline == 1:
        for each in books:
          if each not in self.__books and each not in list(self.__borrowed.keys()):
            self.__books.append(each)
          else:
            print("{} already exists".format(each))
        
        self.__log(self.present_user,books,"Imported")
        print("Books have been successfully imported !")
        return 1
      else:
        print("Sorry Authentication Failed")

    def showBorrowed(self):
      if self.__adminOnline == 1:
        print(self.__borrowed)
      else:
        print("Authentication Failed")
    
    def showBorrowHistory(self,book):
      if self.__adminOnline == 1:
        if book in list(self.__borrowedHistory.keys()):
          print(self.__borrowedHistory[book])
        else:
          print("{} has no borrow history".format(book))
      else:
        print("Authentication Failed")

    def displayBooks(self):
      if(self.__login == 1 or self.__adminOnline == 1):
        print(self.__books)
        print("\n")
      else:
        print("not logged in to use this functions")

    def showAdmin(self):
      print(list(self.__admin)[0])

    def showLog(self,user):
      if self.__adminOnline == 1:
        print(self.__registerLog[user])
      elif user == self.present_user:
        print(self.__registerLog[user])
      else:
        print("Sorry Information classified")

    def borrowBook(self,bookName):
      if(self.__login == 1 and bookName in self.__books):
        self.__log(self.present_user,bookName,"Borrowed")
        self.__books.remove(bookName)
        self.__borrowed[bookName] = self.present_user
        if bookName in list(self.__borrowedHistory.keys()):
          k = self.__borrowedHistory[bookName]
          k.append(self.present_user)
          self.__borrowedHistory[bookName] = k
        else:
          self.__borrowedHistory[bookName] = [self.present_user]
          
        print("Borrow of {} has been Successful".format(bookName))
        return 1
      else:
        if self.__login != 1:
          print("Please Login")
        else:
          print("Book not available")
        return 0

    def returnBook(self,bookName):
      if self.__login == 1 and self.__borrowed[bookName]==self.present_user :
        self.__log(self.present_user,bookName,"Returned")
        self.__books.append(bookName)
        self.__borrowed[bookName] = ""
        print("Return of {} has been Successful".format(bookName))
      else:
        print("Return Failed")