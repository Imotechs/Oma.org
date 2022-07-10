import requests
access_key  = '9bcccf7a9fe864047109763cb85251e5'
base = 'http://api.mediastack.com/v1/news'
url = "https://guardianmikilior1v1.p.rapidapi.com/getEditions"
#locals
news_url = 'http://localhost:8000/docs/news/point/'


payload = "apiKey=%3CREQUIRED%3E"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "de154316e2mshd508cde7bacffa9p18f447jsnec75c8fcb1fd",
	"X-RapidAPI-Host": "Guardianmikilior1V1.p.rapidapi.com"
}
#response = requests.request("GET", url, data=payload, headers=headers)

def get_celeb_news():
    header = {
        "content-type": "application/x-www-form-urlencoded",
        #'access_key':'9bcccf7a9fe864047109763cb85251e5',
    }
    
    #stack = '?access_key=9bcccf7a9fe864047109763cb85251e5&countries=ng'
    stacks = '?access_key=9bcccf7a9fe864047109763cb85251e5&categories=technology&countries=us,ng'
    try:
        response = requests.request("GET", base + stacks, headers=header)

        print(response.text)
        response_data = response.json()

        return response_data['data']
    except:
        pass

def get_music_news():
    header = {
        "content-type": "application/x-www-form-urlencoded",
        #'access_key':'9bcccf7a9fe864047109763cb85251e5',
        }
    
    music = '?access_key=9bcccf7a9fe864047109763cb85251e5&categories=entertainment&countries=us,ng'
    try:
        response = requests.request("GET", base + music, headers=header)

        print(response.text)
        response_data = response.json()
        return response_data['data']
    except:
        pass

def local_news():
    header = {
        "content-type": "application/x-www-form-urlencoded",
        }

    response = requests.request("GET", news_url, headers=header)
    response_data = response.json()
    return response_data