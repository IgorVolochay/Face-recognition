import requests

def pars_person():
    for i in range(1):
        img_data = requests.get("https://thispersondoesnotexist.com/image").content
        
        with open(f'SomePerson_{i}.jpg', 'wb') as handler:
            handler.write(img_data)

if __name__ == '__main__':
        pars_person()
