import os,sys
# change the path accoring to the test folder in system
#sys.path.append('/home/ubuntu/setup/src/fogflow/test/UnitTest/v2')
from datetime import datetime
import copy
import json
import requests
import time
import pytest
import datav2
import sys


# change it by broker ip and port
brokerIp="http://localhost:8070"


# testCase 1
'''
  Testing  subscription with attributes and using ID
'''
def test_getSubscription1():
        #update request to create entity at broker
        url=brokerIp+"/ngsi10/updateContext"
        headers={'Content-Type':'application/json'}
        r=requests.post(url,data=json.dumps(datav2.subdata1),headers=headers)
        print(r.status_code)
        print(r.content)

        #subsciption request in v2 format
        url=brokerIp+"/v2/subscriptions"
        headers= {'Content-Type': 'application/json'}
        r=requests.post(url,data=json.dumps(datav2.subdata2),headers=headers)
        print(r.status_code)
        resp_content=r.content
        resInJson= resp_content.decode('utf8').replace("'", '"')
        resp=json.loads(resInJson)
        resp=resp['subscribeResponse']
        sid=resp['subscriptionId']
        print(sid)

        #update to trigger notification
        url=brokerIp+"/ngsi10/updateContext"
        r=requests.post(url,data=json.dumps(datav2.subdata3),headers=headers)
        print(r.status_code)
        print(r.content)

        #validation based on subscriptionId
        url="http://localhost:8888/validateNotification"
        r=requests.post(url,json={"subscriptionId" : sid})
        print(r.content)
        assert r.status_code == 200


# testCase 2
'''
  Testing subscription with attributes and with Header : User-Agent
'''
def test_getsubscription2():
        #update request to create entity at broker
        url=brokerIp+"/ngsi10/updateContext"
        headers={'Content-Type':'application/json'}
        r=requests.post(url,data=json.dumps(datav2.subdata4),headers=headers)
        print(r.status_code)
        print(r.content)

        #subsciption request in v2 format
        url=brokerIp+"/v2/subscriptions"
        headers= {'Content-Type': 'application/json','User-Agent':'lightweight-iot-broker'}
        r=requests.post(url,data=json.dumps(datav2.subdata5),headers=headers)
        print(r.status_code)
        resp_content=r.content
        resInJson= resp_content.decode('utf8').replace("'", '"')
        resp=json.loads(resInJson)
        resp=resp['subscribeResponse']
        sid=resp['subscriptionId']
        print(sid)

        #update to trigger notification
        url=brokerIp+"/ngsi10/updateContext"
        r=requests.post(url,data=json.dumps(datav2.subdata6),headers=headers)
        print(r.status_code)
        print(r.content)

        #vaidation based on subscriptionId
        url="http://localhost:8888/validateNotification"
        r=requests.post(url,json={"subscriptionId" : sid})
        print(r.content)
        assert r.status_code == 200

# testCase 3
'''
  Testing with subscribing , updating and deleting and validating
'''
def test_getsubscription3():
        #update request to create entity at broker
        url=brokerIp+"/ngsi10/updateContext"
        headers={'Content-Type':'application/json'}
        r=requests.post(url,data=json.dumps(datav2.subdata7),headers=headers)
        print(r.status_code)
        print(r.content)

        #subsciption request in v2 format
        url=brokerIp+"/v2/subscriptions"
        headers= {'Content-Type': 'application/json','User-Agent':'lightweight-iot-broker'}
        r=requests.post(url,data=json.dumps(datav2.subdata8),headers=headers)
        print(r.status_code)
        resp_content=r.content
        resInJson= resp_content.decode('utf8').replace("'", '"')
        resp=json.loads(resInJson)
        resp=resp['subscribeResponse']
        sid=resp['subscriptionId']
        print(sid)

        #update to trigger Notification
        url=brokerIp+"/ngsi10/updateContext"
        r=requests.post(url,data=json.dumps(datav2.subdata8),headers=headers)
        print(r.status_code)
        print(r.content)

        #delete the subscription
        url=brokerIp+"/v2/subscription/"+sid
        r=requests.delete(url)
        print(r.status_code)
        print(r.content)
        print("The subscriptionId "+sid+" is deleted successfully")

        #validate based on get subscriptionId
        url=brokerIp+"/v2/subscription/"+sid
        r=requests.get(url)
        #print(r.status_code)
        print(r.content)
        assert r.status_code == 404
        print("The subscriptionId "+sid+" coud not be fetched via get since deleted")

