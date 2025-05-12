from pycipher import Vigenere

# Mensagem e chave
mensagem = "Minha mensagem Secreta!"
chave = "SEGREDO"

# Criptografando
cifrada = Vigenere(chave).encipher(mensagem)
print("Mensagem cifrada:", cifrada)

# Descriptografando
decifrada = Vigenere(chave).decipher(cifrada)
print("Mensagem decifrada:", decifrada)

# Descriptografando com chave errada
decifrada = Vigenere("ERRO").decipher(cifrada)
print("Mensagem decifrada:", decifrada)

