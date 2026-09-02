import http.client

host = "127.0.0.1:5000"

conn = http.client.HTTPConnection(host)

conn.request("GET", "/user-profiles")

response = conn.getresponse()
print("Status code:", response.status)
print("Response body:\n", response.headers)