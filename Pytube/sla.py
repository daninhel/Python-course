import webview
from pytube import YouTube

video = {
    'url': 'https://youtu.be/3Wo4L2dPS58',
    'title': '',
    'thumbnail': '',
}

# Função para capturar a URL do campo de entrada e baixar o vídeo
def YtDownload():
    # Obtém o valor do campo de entrada no HTML
    video['url'] = webview.evaluate_js('document.getElementById("floatingInput").value')
    
    if video['url']:
        try:
            youtube = YouTube(video['url'])
            video['title'] = youtube.title
            print(f'Título do vídeo: {video["title"]}')
            
            youtube.streams.get_highest_resolution().download()

        except Exception as e:
            print(f"Erro ao obter informações do vídeo: {str(e)}")
    else:
        print("Por favor, insira uma URL válida.")

def main():
    webview.create_window('Youtube Downloader', './index.html')
    webview.start()

if __name__ == '__main__':
    main()
    ...