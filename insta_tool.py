#!/usr/bin/env python3

"""
Instagram Growth & Analytics Toolkit

A lightweight Python toolkit for learning:
- Python programming
- Data analysis
- Social media analytics
- Ethical automation concepts

Version: 0.1
"""

import argparse


TOOL_NAME = "Instagram Growth & Analytics Toolkit"
VERSION = "0.1"


def display_banner():
    print("=" * 50)
    print(TOOL_NAME)
    print("Version:", VERSION)
    print("=" * 50)


def get_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("[-] Value cannot be negative")
                continue

            return value

        except ValueError:
            print("[-] Please enter a valid number")


def get_account_information():
    print()
    print("Account Information")
    print("-" * 30)

    while True:
        account_name = input("Account name: ").strip()

        if not account_name:
            print("[-] Account name cannot be empty")
            continue

        break

    followers = get_non_negative_integer("Followers: ")
    following = get_non_negative_integer("Following: ")
    posts = get_non_negative_integer("Posts: ")
    likes = get_non_negative_integer("Likes: ")
    comments = get_non_negative_integer("Comments: ")

    return (
        account_name,
        followers,
        following,
        posts,
        likes,
        comments
    )


def get_post_information():
    print()
    print("Post Performance Analysis")
    print("-" * 30)

    while True:
        post_title = input("Post title: ").strip()

        if not post_title:
            print("[-] Post title cannot be empty")
            continue

        break

    likes = get_non_negative_integer("Likes: ")
    comments = get_non_negative_integer("Comments: ")
    shares = get_non_negative_integer("Shares: ")
    saves = get_non_negative_integer("Saves: ")
    reach = get_non_negative_integer("Reach: ")

    return (
        post_title,
        likes,
        comments,
        shares,
        saves,
        reach
    )


def calculate_engagement_rate(followers, likes, comments):
    if followers == 0:
        return 0.0

    interactions = likes + comments

    return (interactions / followers) * 100


def calculate_post_engagement_rate(
    likes,
    comments,
    shares,
    saves,
    reach
):
    if reach == 0:
        return 0.0

    interactions = likes + comments + shares + saves

    return (interactions / reach) * 100


def calculate_average_likes(likes, posts):
    if posts == 0:
        return 0.0

    return likes / posts


def calculate_average_comments(comments, posts):
    if posts == 0:
        return 0.0

    return comments / posts


def calculate_average_interactions(likes, comments, posts):
    if posts == 0:
        return 0.0

    interactions = likes + comments

    return interactions / posts


def determine_post_performance(engagement_rate):
    if engagement_rate >= 10:
        return "Excellent"

    if engagement_rate >= 5:
        return "Moderate"

    return "Needs Improvement"


def get_post_recommendation(performance):
    if performance == "Excellent":
        return (
            "Excellent engagement. Keep creating content "
            "similar to this post."
        )

    if performance == "Moderate":
        return (
            "Moderate engagement. Experiment with stronger "
            "hooks, captions, and calls to action."
        )

    return (
        "Engagement is low. Consider improving the content "
        "hook, topic, caption, and call to action."
    )


def display_account_information(
    account_name,
    followers,
    following,
    posts,
    likes,
    comments
):
    print()
    print("=" * 50)
    print("ACCOUNT INFORMATION")
    print("=" * 50)

    print(f"Account:          {account_name}")
    print(f"Followers:        {followers}")
    print(f"Following:        {following}")
    print(f"Posts:            {posts}")
    print(f"Likes:            {likes}")
    print(f"Comments:         {comments}")

    print("=" * 50)


def display_engagement_analysis(engagement_rate):
    print()
    print("=" * 50)
    print("ENGAGEMENT ANALYSIS")
    print("=" * 50)

    print(f"Engagement Rate:  {engagement_rate:.2f}%")

    print("=" * 50)


def display_account_metrics(
    average_likes,
    average_comments,
    average_interactions
):
    print()
    print("=" * 50)
    print("ACCOUNT METRICS")
    print("=" * 50)

    print(f"Average Likes/Post:   {average_likes:.2f}")
    print(f"Average Comments/Post:{average_comments:.2f}")
    print(f"Average Interactions: {average_interactions:.2f}")

    print("=" * 50)


def display_post_analysis(
    post_title,
    likes,
    comments,
    shares,
    saves,
    reach,
    engagement_rate,
    performance
):
    total_interactions = likes + comments + shares + saves

    print()
    print("=" * 50)
    print("POST PERFORMANCE")
    print("=" * 50)

    print(f"Post:               {post_title}")
    print(f"Likes:              {likes}")
    print(f"Comments:           {comments}")
    print(f"Shares:             {shares}")
    print(f"Saves:              {saves}")
    print(f"Reach:              {reach}")
    print(f"Total Interactions: {total_interactions}")

    print()
    print("=" * 50)
    print("POST ANALYSIS")
    print("=" * 50)

    print(f"Engagement Rate:    {engagement_rate:.2f}%")
    print(f"Performance:        {performance}")

    print()
    print("RECOMMENDATION")
    print("-" * 30)

    print(get_post_recommendation(performance))

    print("=" * 50)


def analyze_account():
    (
        account_name,
        followers,
        following,
        posts,
        likes,
        comments
    ) = get_account_information()

    engagement_rate = calculate_engagement_rate(
        followers,
        likes,
        comments
    )

    average_likes = calculate_average_likes(
        likes,
        posts
    )

    average_comments = calculate_average_comments(
        comments,
        posts
    )

    average_interactions = calculate_average_interactions(
        likes,
        comments,
        posts
    )

    display_account_information(
        account_name,
        followers,
        following,
        posts,
        likes,
        comments
    )

    display_engagement_analysis(
        engagement_rate
    )

    display_account_metrics(
        average_likes,
        average_comments,
        average_interactions
    )


def analyze_post():
    (
        post_title,
        likes,
        comments,
        shares,
        saves,
        reach
    ) = get_post_information()

    engagement_rate = calculate_post_engagement_rate(
        likes,
        comments,
        shares,
        saves,
        reach
    )

    performance = determine_post_performance(
        engagement_rate
    )

    display_post_analysis(
        post_title,
        likes,
        comments,
        shares,
        saves,
        reach,
        engagement_rate,
        performance
    )


def main():
    parser = argparse.ArgumentParser(
        description="Instagram Growth & Analytics Toolkit"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    subparsers.add_parser(
        "analyze",
        help="Analyze Instagram account performance"
    )

    subparsers.add_parser(
        "post",
        help="Analyze individual post performance"
    )

    args = parser.parse_args()

    display_banner()

    if args.command == "analyze":
        analyze_account()

    elif args.command == "post":
        analyze_post()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
