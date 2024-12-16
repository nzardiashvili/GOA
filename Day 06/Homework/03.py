name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input(" შეიყვანეტ თქვენი გვარი: ")
father_name = input("შეიყვანეღ მამათქვენის სახელი: ")
father_surname = input("შეიყვანეღ მამათქვენის გვარი: ")
favorite_color = input("სეიყვანეთ  თქვენი საყვარელი ფერი: ")
favorite_car = input("შეიყვანეთ თქვენთვის საყვარელი  მანქანა: ")
hobbies = [input("შეიყვანეთ თქვენი საყვარელი ჰობი #1: "),
           input("შეიყვანეთ თქვენი საყვარელი ჰობი #2: "),
           input("შეიყვანეთ თქვენი საყვარელი ჰობი #3: ")]
print("{name} {surname} - მამის სახელი: {father_name} {father_surname}, საყვარელიფერი {favorite_color}, საყვარელი მანქანა {favorite_car}, საყვარელი ჰობი {', '.join(hobbies)}")
