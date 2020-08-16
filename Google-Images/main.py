
import requests
Image_path = "testing.jpg" # Your File With PATH HERE
def main():
    filePath = Image_path
    searchUrl = 'http://www.google.com/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers["Location"]
    print(fetchUrl)
if __name__ == '__main__':
    main()
