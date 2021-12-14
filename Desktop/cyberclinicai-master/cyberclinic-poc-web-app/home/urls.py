from django.urls import path
from home.views import *

urlpatterns = [
    path('',home,name='home'), # URL for home page
    path('api/mlmodel/version-1',callApi,name='mlmodel'), # To recieve input from user and to give the output
    path('retrain',retrain,name='retrain'), # To get the feedback from practitioner
    path('internel/api/v1/get-data-details',sendDataDetails,name='mlmodel_data_fetch'), # To send feedback data
]