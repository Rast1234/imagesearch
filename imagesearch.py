#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'rast'

import requests
from sys import argv

helpStr = "Google image lookup tool. Usage:\n" \
          "    {0} your-image-to-search-for"

def main():

    try:
        image = argv[1]
    except:
        print(helpStr.format(argv[0]))
        return

    url = "http://www.google.ru/imghp"
    postUrl = "http://www.google.ru/searchbyimage/upload"

    headers = {'User-agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) \\'
                                    'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1',
               'origin': 'http://www.google.ru',
               'referer': 'http://www.google.ru/imghp'
        }

    # crusade for cookies
    grail = requests.get(url, headers = headers)

    # required input name and file name
    fileDict = {'encoded_image': (image, open(image, 'rb'))}

    # submit file via multipart/form-data, other fields not required
    r = requests.post(postUrl, files=fileDict, cookies=grail.cookies, headers=headers)

    # get the last redirect url, thank you Wireshark!
    result = r.history[-1].url
    print(result)

if __name__ == '__main__':
    main()

