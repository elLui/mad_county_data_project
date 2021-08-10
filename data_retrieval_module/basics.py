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

    # return response object
    return res


def save_page_as_text_binary(res):
    # create or overwrite a file for data storage
    # TODO :: future add option to name or dynamically name file for storage
    response_file = open('mad_county_data.txt', 'wb')

    for chunk in res.iter_content(100_000):
        # iterate and write content at 100_000 bytes per cycle
        response_file.write(chunk)