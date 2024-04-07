import sys
import requests

# Check if number of arguments is correct
if len(sys.argv) not in [2,3]:
    print("Improper number of arguments: at least 1 required and no more than 2")
    print("--arg 1: http server's address (required)")
    print("--arg 2: port number (default 80)")
    sys.exit(1)

# Assign port number and check for validity
if len(sys.argv) == 3:
    port = int(sys.argv[2])
else:
    port = 80

if port < 1 or port > 65535:
    print("Invalid port number")
    sys.exit(1)

url = "http://{}:{}".format(sys.argv[1], port)

# Attempt to connect to the server
try:
    reply = requests.head(url, timeout = 500)
    if reply.status_code == requests.codes.ok:
        print("Site is up")
    else:
        print("Site is down")

except requests.exceptions.Timeout:
    print("Request timed out")
    sys.exit(1)

except requests.exceptions.RequestException:
    print("Connection error")
    sys.exit(1)
