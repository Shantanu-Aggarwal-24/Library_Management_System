class Library:
    def __init__(self, listOfBooks):
        self.books = list(listOfBooks.keys())
        self.qty = list(listOfBooks.values())

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        
        # for book in self.books: 
        #     print(" *",book)  

        for i in range(len(self.books)):
            print(f"* {self.books[i]} : {self.qty[i]}")
            
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            # self.books.remove(bookName)
            for i in range(len(self.books)):
                if(self.books[i] == bookName):
                   self.qty[i] =self.qty[i] - 1
                   ind = i
                
            if(self.qty[ind] == 0):
                self.books.remove(bookName)
                self.qty.remove(self.qty[ind])

            print(self.books)
            print(self.qty)
            return True
            
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            print(self.books)
            print(self.qty)
            return False

    def returnBook(self, bookName):
        # self.books.append(bookName)
        for i in  range(len(self.books)):
            if(self.books[i] == bookName):
                self.qty[i] = self.qty[i] + 1
                break
        else:
            self.books.append(bookName)        
            self.qty.append(1)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        print(self.books)
        print(self.qty)

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library({
        "Algorithms": 3,
        "Django":5,
         "C++": 6,
         "Python":10
    })
    student = Student()
    # centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        

# ["Algorithms", "Django", "Clrs", "Python Notes"]
