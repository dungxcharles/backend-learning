import http.client

print("Requesting ...")

HOST = "httpbin.org"
conn = http.client.HTTPConnection(HOST)

conn.request("GET", "/", headers={"host": HOST})

response = conn.getresponse()

print(response.status, end=" ")
print(response.reason)
print(response.getheaders)