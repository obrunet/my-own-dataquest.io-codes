## 2. Authenticating with the API ##

# import requests already done
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params = { "t": "day"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers, params = params)
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

# Explore the python_top dictionary.
# print(python_top['data'])
# print(python_top['data']['children'])

# Extract the list containing all of the posts
python_top_articles = python_top['data']['children']

# Find the post with the most upvotes & assign the ID 
most_upvoted, most_upvotes = 0, 0
for article in python_top_articles:
    if article['data']['ups'] > most_upvotes:
        most_upvotes = article['data']['ups']
        most_upvoted = article['data']['id']



## 4. Getting Post Comments ##

endpoint = ("https://oauth.reddit.com/r/python/comments/") + most_upvoted
comments = requests.get(endpoint, headers = headers).json()

## 5. Getting the Most Upvoted Comment ##

# Querying the comments endpoint returns a list. 
# The first item in the list contains information about the post, 
# The second item contains information about the comments.
comments_list = comments[1]['data']['children']
# Find the most upvoted top-level comment
most_ups = 0
for comment in comments_list:
    if comment['data']['ups'] > most_ups:
        most_ups = comment['data']['ups']
        most_upvoted_comment = comment['data']['id']


## 6. Upvoting a Comment ##

req = {'dir' : 1, 'id' : most_upvoted_comment}
response = requests.post("https://oauth.reddit.com/api/vote", headers = headers, json = req)
status = response.status_code