import http.client

host = "127.0.0.1:5000"
conn = http.client.HTTPConnection(host)
conn.request("GET", "/")

response = conn.getresponse()
print("Status code: ", response.status)
if (response.status == 200):
    with open("confidential.txt", "wb") as file:
        file.write(response.read())

conn.close()