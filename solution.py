#Excercise 1
from symtable import Class


name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"The user {name} is {age} years old")
#   Excersice 2
number = int(input("Enter a number: "))
if number % 4 == 0:
    print(f"The number {number} is divisible by 4")
elif number % 2 == 0:
    print(f"The number {number} is even")

else:
    print(f"The number {number} is odd")
# Extras
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    result = num1 / num2
    print(f"The result of dividing {num1} by {num2} is {result}")
except ZeroDivisionError:
    print("Error since you cannot divide by zero")

# Excersice 3
def newlist(x):
    mylist = []
    n = len(x)
    for i in range(n):
        if i == 0:
            mylist.append(x[i])
        elif i == n - 1:
            mylist.append(x[i])
    return mylist
# another soltuin return x[[x[0] , x[-1]]]
# another soltuin return x[[x[0] , x[n-1]]]

mylist = input("Please enter a list of numbers").split()
mylist = [int(x) for x in mylist]
reuslt = newlist(mylist)
print(f"The new list is {reuslt}")

#Excersice 4
def Numberinlist(x, y):
    if y in x:
        return True
    else:
        return False
Thelist = input("Please enter a list of numbers").split()
Thelist = [int(x) for x in Thelist]
number  = int(input("Please enter a number "))
res = Numberinlist(Thelist, number)
print(res)

# Meduim questions 
#fisrt question
Suminlist = input("Please enter a list of numbers").split()
Suminlist = [int(x) for x in Suminlist]
for i in range(len(Suminlist)):
    for j in range(i+1 , len(Suminlist)):
        for k in range(j+1 , len(Suminlist)):
            sum  = Suminlist[i] + Suminlist[j] + Suminlist[k]
            if sum == 0:
                nnewlist = []
                nnewlist.append(Suminlist[i])
                nnewlist.append(Suminlist[j])
                nnewlist.append(Suminlist[k])
                print(f"THe number that make the sum zero are {nnewlist}")
#After fix the first medium code 
Suminlist = input("Please enter a list of numbers: ").split()
Suminlist = [int(x) for x in Suminlist]

all_triplets = []

for i in range(len(Suminlist)):
  for j in range(i + 1, len(Suminlist)):
    for k in range(j + 1, len(Suminlist)):
      sum = Suminlist[i] + Suminlist[j] + Suminlist[k]
      if sum == 0:
        # Create the triplet list and sort it so duplicates look identical
        nnewlist = sorted([Suminlist[i], Suminlist[j], Suminlist[k]])

        if nnewlist not in all_triplets:
          all_triplets.append(nnewlist)

print(f"The numbers that make the sum zero are {all_triplets}")

#second question
def countwords(text):
    words = text.split()
    wordcount = {}
    for word in words:
        word = word.lower()
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount

text = input("Please enter a text: ")
wordcount = countwords(text)
print(wordcount)

#question 3
class Book:
    def __init__(self, title, author, year, is_checked_out=False):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = is_checked_out

    def check_out(self):
        if self.is_checked_out:
            print(f"The book {self.title} is already checked out.")
        else:
            self.is_checked_out = True
            print(f"The book {self.title} has been checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"The book {self.title} has been returned.")
        else:
            print(f"The book {self.title} was not checked out.")

    def __str__(self):
        return (  f"Title: {self.title}, Author: {self.author}, "f"Year: {self.year}, Checked Out: {self.is_checked_out}"
        )


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"The book {book.title} has been added to the library.")

    def list_books(self):
        for book in self.books:
            print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

        print(f"The book {title} was not found in the library.")
        return None
    def availablebooks(self):
        available_books = [book for book in self.books if not book.is_checked_out]
        return available_books


b1 = Book("1984", "George Orwell", 1949)
b2 = Book("The Alchemist", "Paulo Coelho", 1988)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)

lib.list_books()

b1.check_out()
lib.list_books()

found = lib.find_book("1984")
print(found)
available_books = lib.availablebooks()
print("Available books:")
for book in available_books:
    print(book)
    
