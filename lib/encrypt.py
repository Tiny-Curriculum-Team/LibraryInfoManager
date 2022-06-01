import base64
import hashlib
from os.path import join
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5


def generate_rsa_keys() -> None:
    random_generator = Random.new().read
    rsa = RSA.generate(2048, random_generator)

    private_key_pem = rsa.exportKey()
    with open(join('.pem', 'private_key.pem'), 'wb') as f:
        f.write(private_key_pem)

    public_key_pem = rsa.publickey().exportKey()
    with open(join('.pem', 'public_key.pem'), 'wb') as f:
        f.write(public_key_pem)


def rsa_encrypt(message: str) -> str:
    rsakey = RSA.importKey(open(join('.pem', 'public_key.pem')).read())
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    encrypted_message = base64.b64encode(cipher.encrypt(message.encode('utf-8')))
    return encrypted_message.decode('utf-8')


def md5_encrypt(message: str) -> str:
    hashlib_objection = hashlib.md5()
    hashlib_objection.update(message.encode(encoding='utf-8'))
    return hashlib_objection.hexdigest()
