import requests

# URL to send the GET request to
url = 'http://127.0.0.1:8000/api/hello'

# Replace with your actual token
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI1IiwianRpIjoiOThlZWUzZmJhNTBkNDQzZDg3ZjBlZTZlZTdjZGE2ODE3NDc2YjEwOTk1N2JmNzQ5MTBlNTgyMDgxZWYyMGE0OWNhOTZhNzZmZjNjM2IyNjUiLCJpYXQiOjE3MzE4NDU2NDYuNjQ5MTA4LCJuYmYiOjE3MzE4NDU2NDYuNjQ5MTE2LCJleHAiOjE3NjMzODE2NDYuNjIwNzkyLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.eBPaaVGTmgpoaNGrMPT8cJMcKCiJQjhtJ6IkyKkVSXUKGIP3RiIU71OParBuDwW6yqCMZjZCRnBuZIIfmMjVni89lrKufsOgVSQruaARGiD7G5e-5IvRmeDHEHrts4fPWyvkI4SVjRz3FF1Tl4Ucf1E57Y87BQIB0Uz8bHP1n4TLOXcw7P2qTNvgmmlx6lF76_AyqvYXeH6bUCdO1nGIZ22g8-glh_Ul8KQgUBYtljKnz6c_PpG-Pw0X17U6dhMVDUWWr-_FBUjaDFbXexuU7vxMfJEIPWYDfcPTcNozq3u1cgRSjhICOOsuQdsxTi-7Le6vADDF8LQkppUeHunDbgpn3RKBJHnTGzQg7SeglLH2KKBmkg782h-EkLnA5fhc6QGZLSPz1Nw5TrP-xbm8Z_DgW2sWbKUVhvKSuOsvAJmJstuN537NDmuhmvqEqtWeVfadlc8FmZG_eU1cwQalDRNLbEWbdJZPCN9fR9rsJtSd78t5Rk8d6IX1Cwc5Y-Ud4r3kT2lOTYGXd3csfNuQHy4xC7ITUHOZeqT5cG2zly1eehk_RHVY4E-m8d_REUoRJtsFTobsJaVN7a5Gu8z-5Hp53sdUA7YT63R3kCjH8S6qIJe6kMnqqIJLXwwtSsQD1c2KQSdqShDZe56hm9TTrH9U2cjzIU-Wvgw_BPTx_LY'

# Send the GET request to the API with the Authorization header
headers = {'Authorization': f'Bearer {token}'}
response = requests.get(url, headers=headers)

# Check the response status code and handle accordingly
if response.status_code == 200:
    # Print the response text (body) from the API
    resp = response.text
    print(resp)
else:
    # Print the status code and the error message (in case of failure)
    print(f"Failed to get data from API. Status code: {response.status_code}")
    print(response.text)
