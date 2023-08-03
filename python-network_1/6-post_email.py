#!/usr/bin/python3
"""script to send post request to passed url with email and display
body as respons"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
