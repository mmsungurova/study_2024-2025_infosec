import random
key_text = 'Тест Ключа етс'
















text_1 = "С Новым Годом!"

def get_key(text):
    l = [chr(i) for i in range(0x0410, 0x042F + 1)] + [chr(i) for i in range(0x0030, 0x0039 + 1)]
    key = "".join([random.choice(l) for i in range(len(text))])
    return key

def encrypt(text, key):
    return "".join([chr(ord(key[i])^ord(text[i])) for i in range(len(key))])

def decrypt(text, key):
    k = encrypt(text, key[:len(text)])
    return k + get_key(key[len(text):])


key = get_key(key_text)
encrypted = encrypt(text_1, key)

print(encrypted)

fragment = "С новым" # известный фрагмент сообщения
part_key = decrypt(fragment, encrypted) # ключ на основе фрагмента сообщения
guess = encrypt(encrypted, part_key) # предположительный текст
print(guess) 