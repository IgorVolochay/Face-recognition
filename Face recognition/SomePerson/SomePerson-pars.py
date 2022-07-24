import requests

def pars_person():
    for i in range(100):
        img_data = requests.get("https://thispersondoesnotexist.com/image").content
        if len(str(i)) == 1:
            c = "00" + str(i)
        elif len(str(i)) == 2:
            c = "0" + str(i)
        else:
            c = str(i)
        with open(f'SomePerson_{c}.jpg', 'wb') as handler:
            handler.write(img_data)

if __name__ == '__main__':
        pars_person()