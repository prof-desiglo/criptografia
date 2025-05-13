from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 1. Gerar par de chaves (pública e privada)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Serializar a chave privada em formato PEM (sem senha)
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Serializar a chave pública em formato PEM
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Mostrar as chaves como texto (decodificadas de bytes para string)
print("Chave Privada:")
print(pem_private.decode())

print("Chave Pública:")
print(pem_public.decode())

# 2. Mensagem a ser criptografada
mensagem = b"Segredo muito importante"
print(mensagem)

# 3. Criptografar com a chave pública
mensagem_criptografada = public_key.encrypt(
    mensagem,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(mensagem_criptografada)

# 4. Descriptografar com a chave privada
mensagem_original = private_key.decrypt(
    mensagem_criptografada,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Mensagem original:", mensagem_original.decode())