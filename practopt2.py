#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
import urllib2
import sys

api_key = None


class WeatherClient(object):
    url_base = "http://api.wunderground.com/api/"
    url_service = {"hourly": "/hourly/q/CA/"}

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key


    def hourly(self, localition):
        url = (WeatherClient.url_base + str(self.api_key) + WeatherClient.url_service["hourly"] + localition + ".xml")
        f = urllib2.urlopen(url)
        data = f.read()
        f.close()
        return data


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "API key must be in CLI option"
            sys.exit(0)

    wc = WeatherClient(api_key)
    page = wc.hourly("Lleida")
    print page
