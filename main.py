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

if __name__ == '__main__':
    """
    using main for initial set-up and debugging

    TODO :: once project gets off the ground begin setting up unittest
    """

    response_object = page_retrieval("http://smartweb.madisoncountysheriffal.org/SmartWEBClient/Jail.aspx")

    save_page_as_text_binary(response_object)
