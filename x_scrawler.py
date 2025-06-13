import requests
import os

# Set your Bearer Token (Get this from your X/Twitter developer account)
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

def create_headers(bearer_token):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers

def get_tweets(query, max_results=10):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {
        'query': query,
        'max_results': max_results,
        'tweet.fields': 'id,text,created_at,author_id'
    }
    headers = create_headers(BEARER_TOKEN)
    response = requests.get(search_url, headers=headers, params=query_params)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code}, {response.text}")
    return response.json()

if __name__ == "__main__":
    # Example: search for "OpenAI"
    query = "OpenAI"
    tweets = get_tweets(query)
    print(tweets)
