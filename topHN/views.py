from django.shortcuts import render
# from utils import topS

import requests

def topS(): 
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    response = requests.get(url)
    top_stories_ids = response.json()
    top_stories = []
    for story_id in top_stories_ids[:10]: # fetch top 20 stories
        story_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
        story_data = requests.get(story_url).json()
        top_stories.append(story_data)
    return top_stories

def stories(request):
    got = topS()
    return render(request,"topHN/news_list.html",{
        "items": got
    })
