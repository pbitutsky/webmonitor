import requests
import os

URL_TO_MONITOR = "" #change this to the URL you want to monitor

def webpage_was_changed(): 
    """Returns true if the webpage was changed, otherwise false."""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Pragma': 'no-cache', 'Cache-Control': 'no-cache'}
    response = requests.get(URL_TO_MONITOR, headers=headers)

    # create the previous_content.txt if it doesn't exist
    if not os.path.exists("previous_content.txt"):
        open("previous_content.txt", 'w+').close()
    
    filehandle = open("previous_content.txt", 'r')
    previous_response_html = filehandle.read() 
    filehandle.close()

    if previous_response_text == response.text:
        return False
    else:
        filehandle = open("previous_content.txt", 'w')
        filehandle.write(response.text)
        filehandle.close()
        return True
