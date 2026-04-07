import requests

BASE_URL = 'http://127.0.0.1:8080'

#завантажити файл на сервер
def upload_image(image_path):
    image = open(image_path, "rb")
    files = {'image': image}
    response = requests.post(f'{BASE_URL}/upload', files=files)
    return response.json()


#отримати урл на файл по імені файла
def get_file_path(filename):
    headers = {
        "Content-Type": "text"
    }
    url = f'{BASE_URL}/image/{filename}'
    response = requests.get(url, headers=headers)
    return response.json()['image_url']


#отримати файл по імені файла
def get_image_by_filename(filename):
    headers = {
        "Content-Type": "image"
    }
    url = f'{BASE_URL}/image/{filename}'
    response = requests.get(url, headers=headers)
    return response.content


#видалити файл по отриманому урлу на файл
def delete_image_by_filename(file_url):
    filename = file_url.split('/')[-1]
    url = f'{BASE_URL}/delete/{filename}'
    response = requests.delete(url)
    return response.json()

file_name = 'PIA13389.jpg'
upload_image(file_name)
path = get_file_path(file_name)
delete_image_by_filename(path)