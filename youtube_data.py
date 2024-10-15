import json
import requests

API_KEY=''
API_URL = 'https://www.googleapis.com/youtube/v3/videos'


def get_trending_videos_in_kenya():
    params = {
        'part': 'snippet,statistics',
        'chart': 'mostPopular',
        'regionCode': 'KE',
        'maxResults': 10,
        'key': API_KEY
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data= response.json()
        #prints the response in a more readable format
        #print(json.dumps(data, indent=4)) #makes the response more appealing
        for item in data['items']:
            video_id = item['id']
            title = item['snippet']['title']
            channel_id = item['snippet']['channelId']
            published_at = item['snippet']['publishedAt']
            
            # Extract statistics
            view_count = item['statistics'].get('viewCount', 'N/A')
            like_count = item['statistics'].get('likeCount', 'N/A')
            comment_count = item['statistics'].get('commentCount', 'N/A')
            
            print(f"Video ID: {video_id}")
            print(f"Title: {title}")
            print(f"Channel ID: {channel_id}")
            print(f"Published At: {published_at}")
            print(f"Views: {view_count}")
            print(f"Likes: {like_count}")
            print(f"Comments: {comment_count}")
            print("-" * 40) 

        return data

    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    data = get_trending_videos_in_kenya()
    print(data)
