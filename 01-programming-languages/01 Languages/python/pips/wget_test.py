# This is just a simple wget example
import wget
url = "https://pypi.org/static/images/logo-small.8998e9d1.svg"
filename = wget.download(url)
print(filename)
