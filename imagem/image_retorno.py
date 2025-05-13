from PIL import Image
import stepic

# 1. Carregar a imagem base (precisa ser PNG)
imagem_original = Image.open("Tux.png").convert("RGB")
imagem_original.save("imagem.png")

# 2. Mensagem a ser escondida
mensagem = "Esta é uma mensagem secreta!"

# 3. Codificar a mensagem na imagem
imagem_com_mensagem = stepic.encode(imagem_original, mensagem.encode('ISO-8859-1'))

# 4. Salvar a nova imagem com a mensagem escondida
imagem_com_mensagem.save("imagem_oculta.png")

print("Mensagem escondida com sucesso!")

codigo = stepic.decode(imagem_com_mensagem)
print(codigo)