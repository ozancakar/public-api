import requests

def get_random_cat_fact():
    cat_api_url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1'
    try:
        response = requests.get(cat_api_url)
        if response.status_code == 200:
            data = response.json()
            print(data)  # Gelen veriyi kontrol etmek için
            return data['text']
        else:
            print(f"Kedi API'sine erişilemiyor. Hata kodu: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Hata oluştu: {e}")
        return None

def get_random_joke():
    joke_api_url = 'https://official-joke-api.appspot.com/jokes/random'
    try:
        response = requests.get(joke_api_url)
        if response.status_code == 200:
            data = response.json()
            return f"{data['setup']} {data['punchline']}"
        else:
            print(f"Fıkra API'sine erişilemiyor. Hata kodu: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Hata oluştu: {e}")
        return None

# Kedi bilgisi ve fıkra alma ve ekrana yazdırma
cat_fact = get_random_cat_fact()
joke = get_random_joke()

if cat_fact and joke:
    print("Rastgele Kedi Bilgisi:")
    print(cat_fact)
    print("\nRastgele Fıkra:")
    print(joke)
else:
    print("Veriler alınamadı.")
