from isbntools.app import *
import Barcoder
bformat = ['default','labels','bibtex','csl', 'csv','json','opf','endnote','ris','refworks','msword']
def get_isbn(name):
    isbn = isbn_from_words(name)
    return isbn
def get_info(i,isbnNumber):
    bookData =  registry.bibformatters[bformat[i]](meta(isbnNumber))
    return bookData
print('''
....Book Finder....
1. Find Book by Name
2. Find Book by ISBN 
3. Find ISBN by Name
4. Find Book by Scaning barcode
Press q to exit
''')
while 1:
    opt1 = input("$ ")
    if opt1 == 'q':
        break
    opt1 = int(opt1)
    if opt1==1:
        bookName = input("Enter the Name of the Book: ")
        if bookName == 'q':
            break
        ISBN = get_isbn(bookName)
        print("Select the Output format(recomended 2):")
        for i ,val in enumerate(bformat):
            print(f'{i+1}. {val}')
        formatNUM = 1
        formatNUM = int(input("$ ")) - 1
        if formatNUM == 'q':
            break
        print(get_info(formatNUM,ISBN))
    elif opt1==2:
        isbnNumber = input("Enter the ISBN number: ")
        if isbnNumber == 'q':
            break
        print("Select the Output format:")
        for i ,val in enumerate(bformat):
            print(f'{i+1}. {val}')
        formatNUM = int(input("$ ")) - 1
        if formatNUM == 'q':
            break
        print(get_info(formatNUM,isbnNumber))
    elif opt1==3:
        bookName = input("Enter the Name of the Book: ")
        if bookName == 'q':
            break
        ISBN = get_isbn(bookName)
        print("ISBN Number is "+ISBN)
    elif opt1==4:
        print("Scan the Barcode of Book!")
        ISBN = Barcoder.main()
        print("Select the Output format(recomended 2):")
        for i ,val in enumerate(bformat):
            print(f'{i+1}. {val}')
        formatNUM = 1
        formatNUM = int(input("$ ")) - 1
        if formatNUM == 'q':
            break
        print(get_info(formatNUM,ISBN))
    else:
        print("Invalid Input")


