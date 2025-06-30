#!/usr/bin/env python3
"""
API data consumption and processing module.

This module demonstrates how to fetch data from a REST API using the requests library
and process the data by converting it to different formats like CSV.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print their titles.

    This function sends a GET request to the JSONPlaceholder API,
    checks the response status, and prints all post titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # Send GET request to the API
        response = requests.get(url)

        # Print the status code
        print(f"Status Code: {response.status_code}")

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON
            posts = response.json()

            # Print all post titles
            for post in posts:
                print(post['title'])
        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
    except KeyError as e:
        print(f"Error processing post data: {e}")


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save them to a CSV file.

    This function fetches posts from the API, structures the data,
    and saves it to a CSV file with id, title, and body columns.
    """
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # Send GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON
            posts = response.json()

            # Structure the data into a list of dictionaries
            structured_posts = []
            for post in posts:
                structured_post = {
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                }
                structured_posts.append(structured_post)

            # Write data to CSV file
            with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
                # Define the fieldnames based on dictionary keys
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write the header
                writer.writeheader()

                # Write all posts
                writer.writerows(structured_posts)

            print(f"Successfully saved {len(structured_posts)} posts to posts.csv")

        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")
    except KeyError as e:
        print(f"Error processing post data: {e}")


if __name__ == "__main__":
    print("Fetching and printing posts:")
    fetch_and_print_posts()

    print("\nFetching and saving posts to CSV:")
    fetch_and_save_posts()
