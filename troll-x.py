import os
import random
import requests

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
USER_TO_TROLL = "target_username"  # Replace with the X/Twitter username (without @) you want to reply to

JOKES = [
    "Why did the computer show up at work late? It had a hard drive!",
    "I'm not lazy, I'm just on energy-saving mode.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I would tell you a joke about UDP, but you might not get it.",
]

def create_headers(token):
    return {"Authorization": f"Bearer {token}"}

def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = create_headers(BEARER_TOKEN)
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()["data"]["id"]

def get_latest_tweet(user_id):
    url = f"https://api.twitter.com/2/users/{user_id}/tweets"
    headers = create_headers(BEARER_TOKEN)
    params = {"max_results": 5}
    r = requests.get(url, headers=headers, params=params)
    r.raise_for_status()
    tweets = r.json().get("data", [])
    return tweets[0] if tweets else None

def reply_to_tweet(tweet_id, message):
    # You must use OAuth 1.0a user context to post tweets
    # This example prints instructions, as posting requires elevated permissions
    print(f"Would reply to tweet {tweet_id} with: {message}")
    print("To actually reply, use Tweepy or Twitter API with OAuth 1.0a and POST /2/tweets.")

if __name__ == "__main__":
    user_id = get_user_id(USER_TO_TROLL)
    tweet = get_latest_tweet(user_id)
    if tweet:
        joke = random.choice(JOKES)
        reply_to_tweet(tweet["id"], joke)
    else:
        print("No recent tweets found to reply to.")
