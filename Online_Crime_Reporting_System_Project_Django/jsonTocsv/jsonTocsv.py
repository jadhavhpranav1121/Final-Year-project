from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys

email = 'youremail@here.com'
input_filename =  'c:\\temp\\input.json'
output_filename = 'c:\\temp\\output.csv'

#read json
with open(input_filename) as json_file:
    json = json_file.read()
    api_url = 'https://data.page/api/getcsv'
    post_fields = {'email': email, 'json': json}
    request = Request(api_url, urlencode(post_fields).encode(),    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    })
    csv = urlopen(request).read().decode()

#write csv
with open(output_filename, "w") as f:
    f.write(csv)
    f.close()