import requests, urllib
from django.shortcuts import render
import json
# Create your views here.

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View

class HomePageView(View):


    def dispatch(request, *args, **kwargs):
    	
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Temperature</title>
            </head>
            <body>
                <h1>The average Temperature.</h1>
                <p>{{}}</p>
            </body>
            </html>
        ''');

        
        s = str(args)
        # print(s[24])
        # print(s[28])
        # print(s[32])

        n = s[24]
        a = s[28]
        w = s[32]

        count, sm = 0, 0

        if n=='1':
        	# print('inside if condition');
        	res_acc = requests.get("http://127.0.0.1:5000/accuweather?latitude=44&longitude=33")
        	res_acc = res_acc.json()
        	#y = json.loads(res_acc);
        	sm += int(res_acc['simpleforecast']['forecastday'][0]['high']['fahrenheit'])
        	count += 1
        	# print(sm)

        if a=='1':
        	res_noa = requests.get("http://127.0.0.1:5000/noaa?latlon=44,33")
        	res_noa = res_noa.json()
        	sm += int(res_noa['today']['high']['fahrenheit'])
        	count += 1
        	# print(count)
        
        api_end = "http://127.0.0.1:5000/weatherdotcom"
        data_d = {"lat":33.3,"lon":44.4}
        headers = {'content-type': 'application/json'}
        json_data = json.dumps(data_d)
        #print(json_data['lat'])
        	
        if w=='1':
        	res_we = requests.post(api_end, data=json_data, headers = headers)
        	res_we = res_we.json()
        	sm += int(res_we['query']['results']['channel']['condition']['temp'])
        	count += 1
        	# print(sm)

        	# res_w = res_we.text
        	# print(res_w)

        avg = sm/count
        print(avg)

       
        

        return HttpResponse(response_text)



