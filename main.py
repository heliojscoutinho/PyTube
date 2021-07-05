# Instalar o pytube (pip install pytube)

from pytube import YouTube

#Digite o link do vídeo.
link = input("Digite o link do vídeo: ")
#Digite o diretório onde será salvo o vídeo.
path = input("Digite o diretório onde será salvo: ")
yt = YouTube(link)

#Detalhes
print("Título do vídeo: ", yt.title)
print("Tempo de vídeo: ", yt.length, "segundos.")

#Pegar a melhor resolução.
ys = yt.streams.get_highest_resolution()

#Download
print("Efetuando o download...")
ys.download(path)
print("Download finalizado!")