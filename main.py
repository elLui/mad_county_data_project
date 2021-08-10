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
from selenium.webdriver.support.ui import Select


def sele_browser(url_input):
    """
    :param url_input:
    :return:
    """
    # using Firefox ver 91.0
    browser = webdriver.Firefox()

    print(type(browser))

    browser.get(url_input)

    """
    selecting element id from page options follow:
    
    value="0" Current Inmates Only
    value="1" Released Inmates Only
    value="2" Both Current And Released
    """
    search_type = Select(browser.find_element_by_id("TypeSearch"))
    search_type.select_by_value('2')

    first_submit = browser.find_element_by_name("btnSumit")
    first_submit.click()

    # TODO :: once initial query is submitted bottom of page has a load more button that appears -
    # TODO :: need to consider being able to load the entire catalog vs. making loops to extract portions
    # TODO :: based on alphabetical rankings


if __name__ == '__main__':
    """
    using main for initial set-up and debugging

    TODO :: once project gets off the ground begin setting up unittest
    """
    url = "http://smartweb.madisoncountysheriffal.org/SmartWEBClient/Jail.aspx"

    sele_browser(url)










    # response_object = page_retrieval(url)
    # save_page_as_text_binary(response_object)
