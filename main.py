"""
    Project goals - scrape public data regarding Madison County Detention Center for visualization.

 initial todo will increase according to project demands and learning structure

 TODO :: set-up web scraping and data collection for http://smartweb.madisoncountysheriffal.org/SmartWEBClient/Jail.aspx

 TODO :: set-up database structure to store information

 @author elluis.codes@gmail.com
 @version 08102021

 python3.9

"""
import requests


def page_retrieval(url):
    # send a request to download the page from url
    res = requests.get(url)

    try:
        # verify that page download occurred before continuation
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem : %s' % exc)

        # test functions
        # print(type(res))
        #
        # print(res.status_code)
        #
        # print(len(res.text))
        #
        # print(res.text[200:])
        #
        # print(res.text[:200])


def save_page_as_text_binary(res):
    # create or overwrite a file for data storage
    # TODO :: future add option to name or dynamically name file for storage
    response_file = open('mad_county_data.txt', 'wb')

    for chunk in res.iter_content(100_000):
        # iterate and write content at 100_000 bytes per cycle
        response_file.write(chunk)








if __name__ == '__main__':
    """
    using main for initial set-up and debugging

    TODO :: once project gets off the ground begin setting up unittest
    """

    basic_page_retrieval("http://smartweb.madisoncountysheriffal.org/SmartWEBClient/Jail.aspx")
