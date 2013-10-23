# -*- coding: utf-8 -*-
__author__ = 'rast'


import mechanize
import cookielib
from sys import argv


def main():
    # Browser
    image = argv[1]

    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(False)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Want debugging messages?
    br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) \\'
                                    'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    # Open some site, let's pick a random one, the first that pops in mind:
    r = br.open('http://google.ru/imghp')
    html = r.read()

    # Show the source
    #print(html)
    # or
    #print(br.response().read())

    # Show the html title
    #print(br.title())

    # Show the response headers
    #print(r.info())
    # or
    #print(br.response().info())

    # Show the available forms
    #for f in br.forms():
    #    print(f)

    #print("------------")
    # Select the first (index zero) form
    br.select_form(nr=0)
    #br.form.set_all_readonly(False)
    #print(br.form)

    br.form.new_control('text', "image_url", {})
    br.form.new_control('text', "image_content", {})
    br.form.new_control('text', "filename", {})
    br.form.new_control('file', "encoded_image", {})
    br.form.add_file(open(image), filename=image, name="encoded_image")
    br.form.action = "http://www.google.ru/searchbyimage/upload"
    br.form.method = "POST"
    br.form.fixup()

    #print(br.form)

    br.submit()
    #print(br.response().read())
    print(dir(br.response()))
    print(br.response().geturl())

    # Looking at some results in link format
    #for l in br.links(url_regex='stockrt'):
    #    print(l)


if __name__ == '__main__':
    main()

