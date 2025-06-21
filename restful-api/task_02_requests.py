#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
          print(post['title'])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        posts = r.json()

        listed_posts = []
        for post in posts:
            listed_posts.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        with open("posts.csv", "w",encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(listed_posts)