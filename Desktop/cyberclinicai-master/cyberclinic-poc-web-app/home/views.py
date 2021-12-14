from typing import final
from django.shortcuts import render,redirect
import json
from django.views.decorators.csrf import csrf_exempt
from home.mlmodel import recom_model # File and Function using to call the MLFlow API
from django.http import JsonResponse
from home.models import *
from django.core import serializers


# This function has been used to render the home page 
def home(request):
    return render(request,'home.html')


# CSRF Exempt is a method that is required if we are trying to escape from csrf token that is used by django
# This function has been used to take the input from the user end , then it will be pass to the MLflow API through
# a function named recom_model which is written in mlmodels.py file. Once we are recieving the response from the
# Mlflow API, we have a model called Feedback from this we are fetching the previous feedbacks provide by some practitioner
# for this cluster no. Then we are adding that also in the response which need to be send to front end as response.

@csrf_exempt
def callApi(request):
    if request.method == 'POST':
        input_data = json.loads(request.body.decode('utf-8'))
        response = recom_model(input_data['input']) # Function from mlmodel.py file used to call mlflow model API
        myprevdata = {
            "metric":"Previous_Feedback",
            "questions":[]
            }
        response_result = json.loads(response.json())
        prv_feedback = Feedback.objects.filter(cluster=response_result['prediction_class'])
        for i in prv_feedback:
            to_be_added = {}
            if i.main_id:
                to_be_added['index'] = i.main_id
            else:
                to_be_added['index'] = None
            to_be_added['Practitioner'] = i.value
            myprevdata['questions'].append(to_be_added)
        response_result['Recommendations'].insert(0,myprevdata)
        result = json.dumps(response_result)
        return JsonResponse(result,safe=False)
    else:
        response = {
            'status':404,
            'message':"Only POST method is allowed"
        }
        return JsonResponse(response,safe=False)



# This function has been used to store the feedback provided by the practitioner. We have a model named Feedback which is refering to the 
# Feedback table, inside this table we are storing all the feedbacks provided by the practitioner . We have a feature using which practitioner
# can provide his/her custom recommendation. Here we are checking for that particular cluster label whether that recommendation was provided
# earlier or not, if it was provided then we are increasing the count and if it was not provided earlier we are creating a new record. 
@csrf_exempt
def retrain(request):
    if request.method == 'POST':
        input_data = json.loads(request.body.decode('utf-8'))
        print(input_data)
        if input_data['name'] == 'custom':
            if Feedback.objects.filter(value=input_data['answer']).exists():
                print("test 1")
                feedback = Feedback.objects.get(value=input_data['answer'])
                feedback.count += 1
                feedback.save()
            else:
                print("test 2")
                feedback = Feedback(value=input_data['answer'],custom=True,cluster=input_data['classLabel'])
                feedback.save()
        else:
            if Feedback.objects.filter(value=input_data['answer']).exists():
                print("Test 3")
                feedback = Feedback.objects.get(value=input_data['answer'])
                feedback.count += 1
                feedback.main_id = input_data['value']
                feedback.save()
            else:
                print("test 4")
                feedback = Feedback(value = input_data['answer'],cluster=input_data['classLabel'])
                print("Done")
                feedback.main_id = input_data['value']
                feedback.save()
        response = {
            'status':200,
            'message':"Thank you for your feedback!"
        }
        return JsonResponse(response,safe=False)
    else:
        response = {
            'status':404,
            'message':"Only POST method is allowed"
        }
        

# This is basically an API which is sending the feedback data which can be used by the data scientist to retarin the model.
def sendDataDetails(request):
    feedback = Feedback.objects.all()
    feedback_list = serializers.serialize('json', feedback)
    return JsonResponse(feedback_list,safe=False)

