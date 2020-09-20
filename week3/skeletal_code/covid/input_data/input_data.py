import requests

def get_input_data(input_url):
    '''
    input: url
    output: dict
    '''
    output = {}
    response = requests.get(input_url)
    output = response.json()
    if isinstance(output, dict):
        #print(output)
        return output

    print("getting input data from API")
    #raise ValueError
    return False

#test case
# + Successful return 200 OK
# Wrong URL or URL does not exist
# URL is correct but resource is not present