while True:
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzабвгдеєжзиіїйклмнопрстуфхцчшщьюяабвгдеєжзиіїйклмнопрстуфхцчшщьюя12345678901234567890'
    k = int(input("Введіть ключ"))
    if k == 0:
        k = + 1
    text = input("Введіть текст, який хочете зашифрувати: ").lower()
    result = ""
    for letter in text:
        place = alphabet.find(letter)
        newplace = place + k
        if letter in alphabet:
            result = result + alphabet[newplace]
        else:
            result = result + letter
    print("Ваший зашифрований текст: ", result)

