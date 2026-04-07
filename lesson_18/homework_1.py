import requests


BASE_URL = "https://images-api.nasa.gov"
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

# Отримання файлів по nasa_id
def get_list_of_photos(search_url, search_params):
    items = requests.get(search_url, params=search_params).json()["collection"]["items"]
    return [item["data"][0]['nasa_id'] for item in items]


#отримати список URL для файлів
def get_asset_url(nasa_id):
    get_asset_url = f"{BASE_URL}/asset/{nasa_id}"
    url = requests.get(get_asset_url).json()["collection"]["items"]
    for item in url:
        if item["href"].endswith(".jpg"):
            return item["href"]
        else:
            raise FileNotFoundError


#завантажити файл
def download_image(url, nasa_id):
    response = requests.get(url).content
    try:
        with open(f"{nasa_id}.jpg", "wb") as f:
            f.write(response)
    except FileNotFoundError:
        pass


#завантажити вказану кількість файлів
def get_N_photos(amount, list):
    counter = 0
    for nasa_id in list:
        if counter < amount:
            download_image(get_asset_url(nasa_id), nasa_id)
            counter += 1
        else:
            pass

get_N_photos(10, get_list_of_photos(search_url, search_params))