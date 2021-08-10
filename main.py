"""
    Project goals - scrape public data regarding Madison County Detention Center for visualization.

 initial todo will increase according to project demands and learning structure

 TODO :: set-up web scraping and data collection for http://smartweb.madisoncountysheriffal.org/SmartWEBClient/Jail.aspx

 TODO :: set-up database structure to store information

 @author elluis.codes@gmail.com
 @version 08102021

 python3.9

"""
from data_retrieval_module.basics import page_retrieval, save_page_as_text_binary

from selenium import webdriver


def sele_browser(url_input):
    """
    installed ChromeDriver from:
    https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.107/
    using Chrome version :: Version 92.0.4515.131 (Official Build) (64-bit)
    :param url_input:
    :return:
    """

    browser = webdriver.Chrome()

    print(type(browser))

    browser.get(url_input)





if __name__ == '__main__':
    """
    using main for initial set-up and debugging

    TODO :: once project gets off the ground begin setting up unittest
    """
    url = "https://smartweb.madisoncountysheriffal.org/SmartWEBClient/Jail.aspx"

    sele_browser(url)

















    # response_object = page_retrieval(url)
    # save_page_as_text_binary(response_object)
