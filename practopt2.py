#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
import urllib2
import sys
from bs4 import BeautifulSoup

api_key = None
nhours = None


class WeatherClient(object):
    url_base = "http://api.wunderground.com/api/"
    url_service = {"hourly": "/hourly/q/CA/"}

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key
        self.temperature = []
        self.cond = []
        self.feelslike = []
        self.hour = []

    # busca les caracteristiques de temps de les n hores que volem saber.
    def hourly(self, localition):
        url = (WeatherClient.url_base + str(self.api_key) + WeatherClient.\
        url_service["hourly"] + localition + ".xml")
        f = urllib2.urlopen(url)
        data = f.read()
        f.close()

        soup = BeautifulSoup(data, 'lxml')

        items = soup.find_all("feelslike")
        i = 0
        for item in items:
            if i < nhours:
                self.feelslike.append(item.find("metric").text)
            else:
                break
            i = i + 1
        items = soup.find_all("temp")
        i = 0
        for item in items:
            if i < nhours:
                self.temperature.append(item.find("metric").text)
            else:
                break
            i = i + 1

        items = soup.find_all("condition")
        i = 0
        for item in items:
            if i < nhours:
                self.cond.append(item.text)
            else:
                break
            i = i + 1

        items = soup.find_all("hour")
        i = 0
        for item in items:
            if i < nhours:
                self.hour.append(item.text)
            else:
                break
            i = i + 1

    def impresion(self):
        for i in range(len(self.temperature)):
            print "At " + self.hour[i] + " will be " + self.temperature[i] +\
             " degrees and the feelslike will be " + self.feelslike[i] +\
             " degrees."
            print "The sky will be " + self.cond[i] + ".\n"


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "API key must be in CLI option"
            sys.exit(0)

    nhours = int(input("Please, enter how many hours do you want.\n"))
    wc = WeatherClient(api_key)
    page = wc.hourly("Lleida")
    wc.impresion()
