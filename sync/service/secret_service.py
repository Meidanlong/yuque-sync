from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode

# 固定盐值
salt = b'salt_'

# 密码
password = b'password'

# 使用PBKDF2HMAC算法，基于密码和盐值生成密钥
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = urlsafe_b64encode(kdf.derive(password))

# 创建Fernet对象
cipher_suite = Fernet(key)

# 加密
text = "需要加密的字符串".encode()
cipher_text = cipher_suite.encrypt(text)
print(cipher_text)

# 解密
plain_text = cipher_suite.decrypt(cipher_text)
print(plain_text.decode())
