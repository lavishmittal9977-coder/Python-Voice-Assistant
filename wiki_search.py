import wikipedia
import requests
#def search_wikipedia(query):
#    try:
#        result=wikipedia.summary(query,sentences=2)
#        return result
#    except wikipedia.exceptions.DisambiguationError:
#        return "There is a multiple results for this Topic."
#    except wikipedia.exceptions.PageError:
#        return "Sorry,I could not find any information about this Topic."
#    except Exception:
#        return "Sorry,Something went wrong."


def search_wikipedia(query):
    url="https://en.wikipedia.org/api/rest_v1/page/summary/"+query.replace(" ","_")
    headers={
        "User-Agent":"VoiceAssistant/1.0 (Python project)"
    }
    response=requests.get(url,headers=headers,timeout=10
                          )
    
    if response.status_code==200:
        data=response.json()
        return data["extract"]
    elif response.status_code==404:
        return "Sorry,I could not find this topic."
    else:
        return "Sorry,Wikipedia is not responding."





