import json
import http.client


def lambda_handler(event, context):
    print(event)
    conn = http.client.HTTPSConnection('v2.jokeapi.dev')
    payload = ''
    headers = {}
    conn.request('GET', '/joke/Any?type=twopart', payload, headers)
    res = conn.getresponse()
    data = res.read()

    json_response = json.loads(data)

    return {
        'partOne': json_response['setup'],
        'partTwo': json_response['delivery']
    }
