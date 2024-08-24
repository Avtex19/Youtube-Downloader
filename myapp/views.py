from urllib.error import HTTPError
from django.shortcuts import render
from pytube import YouTube
from pytube.exceptions import RegexMatchError


def youtube(request):
    message = ""
    if request.method == 'POST':
        link = request.POST.get('link')
        try:
            video = YouTube(link)
            stream = video.streams.get_lowest_resolution()
            stream.download()
            message = "Download successful!"
        except RegexMatchError:
            message = "Invalid YouTube URL."
        except HTTPError:
            message = "HTTP Error: Could not download the video."
        except Exception as e:
            message = f"An error occurred: {e}"

        return render(request, 'home.html', {'message': message})

    return render(request, 'home.html', {'message': message})
