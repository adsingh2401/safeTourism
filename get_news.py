import requests
import json
import datetime
import os

def get_news_main(location):
    apiKey = os.environ['NEWSAPI']
    #location = 'jaipur'
    q = '{0}'.format(location)
    pageSize = 50
    sortBy = 'popularity'
    country = 'in'
    #calculate date for news query
    today_date = datetime.datetime.now()
    week_before_date = datetime.datetime.now() - datetime.timedelta(days=7)
    from_date = week_before_date.strftime('%Y-%m-%d')
    to_date = today_date.strftime('%Y-%m-%d')

    #open file to write response
    #obj = open('resp.json', 'wb')

    #Using NewsAPI.org to get news using API
    response = requests.get('https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy={}&pageSize={}&apiKey={}'.format(q, from_date, to_date, sortBy, pageSize, apiKey))

    #If status code == 200 write response in json file
    if response.status_code == 200:
        #obj.write(response.json())
        print("Fetching news...")
        with open('resp.json', 'w') as outfile:
            json.dump(response.json(), outfile)
        #Write headlines to headlines file
        obj = open('headlines.txt', 'w')
        #load response in json string
        resp = json.loads(response.content)
        #for index in range(resp['totalResults']):
        if resp['totalResults'] >= 50:
            r = 50
        else:
            r = resp['totalResults']
        for index in range(r):
            print(".", end="")
            data = resp['articles'][index]['description'] + ".\n"
            #print(type(data))
            obj.write(data)
        print("Total Fetched: {}".format(r))
        obj.close()
    else:
        print("Error response code: {}".format(response.status_code))
        print("Error response: {}".format(str(response.content)))

#get_news()