import bcrypt

def hash_password(plain_text_pass):
        pass_bytes = plain_text_pass.encode("utf-8")
        for a in pass_bytes:
          print(str(pass_bytes))
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(pass_bytes, salt)
        return hashed_pass

passwd = "a"
pass_hash = hash_password(passwd)
print(f'Password: {passwd} Hash: str{pass_hash}')