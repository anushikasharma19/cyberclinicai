import requests
import json

url = 'https://adb-4447139959491338.18.azuredatabricks.net/model/Cyberclinic_Recom_Model/Production/invocations'

token = '' # This is the databricks access that is required to access the mlflow API

headers = {
    'Content-Type': 'application/json; format=pandas-split',
    'Authorization':f'Bearer {token}'
}

# Function which will send the input to model and will also accept the response from that model and then will return the response.
def recom_model(input_data):
    data = json.dumps({'columns': ['model_input'], 'data': [['{}'.format(input_data)]]})
    response = requests.post(url, headers=headers, data=data)
    return response


