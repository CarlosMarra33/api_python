from cryptography.fernet import Fernet


def _encode(password, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(password.encode())

    return cipher_text


def _check_key(email):
    x = open("key.txt", "r")
    content = x.readlines()
    x.close()
    for i in content:
        if i.split(" ")[0] == email:
            # print(email)
            return i.split(" ")[2]
    return 0


class Security:
    def start_encode(email, password):
        key = Fernet.generate_key()
        data_arch = open("key.txt", "r")
        content = data_arch.readlines()
        content.append(f"{email} | {key.decode()} \n")
        data_arch = open("key.txt", "w")
        data_arch.writelines(content)
        data_arch.close()
        return _encode(password, key)

    def decode(email, password):
        if _check_key(email) != 0:
            cipher_suite = Fernet(_check_key(email).encode())
            plain_text = cipher_suite.decrypt(password)
            return plain_text
        else:
            return b"0"
