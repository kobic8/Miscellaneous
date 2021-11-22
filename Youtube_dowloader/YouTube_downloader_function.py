from pytube import YouTube


def download(link):
    print("downloading")
    YouTube(link).streams.first().download()
    print("Vid is successfully downloaded")


if __name__ == '__main__':
    base_link = "https://www.youtube.com/watch?v=PB_0-d3Sp5s&list=PL_c9BZzLwBRLpDEpYRFXKBN-2ZCsAx0ps&index="
    for vid in range(11, 17):
        VidLink = base_link + str(vid)
        print(VidLink)
        download(VidLink)
