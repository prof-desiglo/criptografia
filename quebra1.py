from pycipher import Caesar

# Mensagem cifrada
mensagem_cifrada = "FRTERQB"

# Tenta todas as 26 chaves possíveis
print("Tentando todas as chaves (0 a 25):\n")
for chave in range(26):
    mensagem_decifrada = Caesar(key=chave).decipher(mensagem_cifrada)
    print(f"Chave {chave:2}: {mensagem_decifrada}")