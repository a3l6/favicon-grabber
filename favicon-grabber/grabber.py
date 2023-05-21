import os


def download_favicon(url: str, path: str="favicons/", size: int=64):
    os.system("mkdir {path}")
    link: str = f"https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://{url}&size={str(size)}"
    filename: str = f"{url}.png"

    os.system(f"cd {path} && curl \"{link}\" --output {filename}")

def download_favicons(urls: list[str], path: str="favicons", size: int=64):
    os.system("mkdir {path}")
    for url in urls:
        link: str = f"https://t2.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://{url}&size={str(size)}"
        filename: str = f"{url}.png"

        os.system(f"cd {path} && curl \"{link}\" --output {filename}")