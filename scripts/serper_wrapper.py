import http.client
import json
import os
import urllib.parse

class SerperClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("SERPER_API_KEY")
        if not self.api_key:
            raise ValueError("SERPER_API_KEY is not set")

    def search(self, query, type="search"):
        conn = http.client.HTTPSConnection("google.serper.dev")
        payload = json.dumps({
            "q": query
        })
        headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }
        
        endpoint = "/places" if type == "places" else "/search"
        
        try:
            conn.request("POST", endpoint, payload, headers)
            res = conn.getresponse()
            data = res.read()
            return json.loads(data.decode("utf-8"))
        except Exception as e:
            print(f"Error querying Serper: {e}")
            return {}

    def places_search(self, query):
        """Wrapper specifically for Places API"""
        return self.search(query, type="places")

    def xray_search(self, role, industry, location):
        """Constructs and runs an X-Ray search for LinkedIn"""
        query = f'site:linkedin.com/in/ "{role}" "{industry}" "{location}"'
        return self.search(query, type="search")
