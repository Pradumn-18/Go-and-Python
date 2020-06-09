import os,sys
from datetime import datetime
import copy
import json
import requests
import time
import pytest
import sys

e_url="http://180.179.214.211:8090"

#test Case 1
'''
  Testing the /hello route
'''
def test_route1():
        url=e_url+"/hello"
        r=requests.post(url)
        print(r.status_code)
        print(r.content)
        assert r.status_code == 200
