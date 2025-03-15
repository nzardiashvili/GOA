student1 = {
    "name": "ნინო",
    "surnume": "zardiashvili",
    "age": 14,
    "adverage_score": 10
}

student2 = {
    "name": "qeti",
   "surnume": "goginashvili",
   "age": 15,
   "adverage_score": 10
}
print("მოსწავლე 1-ის ინფორმაცია: ")
for key, value in student1.items():
    print("{key}: {value}")
    print("მოსწავლე 2-ის ინფორმაცია: ")
    for key, value in student2.items():
        print("{key}: {value}")