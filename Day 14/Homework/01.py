start = int(input("შემოიყვანეტ პირველი რიცხვი: "))
end = int(input("შემოიყვანეტ მეორე რიცხვი: "))

for i in range(start, end + 1):
    if i % 2 == 0 and i % 3 == 0:
        print( "{i} 2-ისა და 3-ის ჯერადი")
    else:
        print("{i} 2-ისა და 3-ის ჯერადი")
