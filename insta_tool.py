#!/usr/bin/env python3

"""
Instagram Growth & Analytics Toolkit

A command-line toolkit for analyzing Instagram performance
and generating ethical, data-driven growth recommendations.

This project is intended for educational purposes and
legitimate social-media analytics.
"""

import argparse
import os
from datetime import datetime


VERSION = "0.2"


# ============================================================
# GENERAL FUNCTIONS
# ============================================================

def display_banner():
    print("=" * 50)
    print("Instagram Growth & Analytics Toolkit")
    print(f"Version: {VERSION}")
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


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("[-] Value must be greater than zero")
                continue

            return value

        except ValueError:
            print("[-] Please enter a valid number")


def get_account_name():
    while True:
        name = input("Account name: ").strip()

        if not name:
            print("[-] Account name cannot be empty")
            continue

        return name


def save_report(filename, content):
    os.makedirs("reports", exist_ok=True)

    filepath = os.path.join("reports", filename)

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

        print()
        print(f"[+] Report saved: {filepath}")

    except OSError as error:
        print(f"[-] Could not save report: {error}")


# ============================================================
# ACCOUNT ANALYSIS
# ============================================================

def analyze_account():
    print()
    print("Account Information")
    print("-" * 30)

    account_name = get_account_name()

    followers = get_non_negative_integer("Followers: ")
    following = get_non_negative_integer("Following: ")
    posts = get_non_negative_integer("Posts: ")
    likes = get_non_negative_integer("Likes: ")
    comments = get_non_negative_integer("Comments: ")

    print()
    print("=" * 50)
    print("ACCOUNT INFORMATION")
    print("=" * 50)

    print(f"Account:              {account_name}")
    print(f"Followers:            {followers}")
    print(f"Following:            {following}")
    print(f"Posts:                {posts}")
    print(f"Likes:                {likes}")
    print(f"Comments:             {comments}")

    # Account engagement estimate
    if followers > 0:
        engagement_rate = (
            (likes + comments) / followers
        ) * 100
    else:
        engagement_rate = 0.0

    print()
    print("=" * 50)
    print("ENGAGEMENT ANALYSIS")
    print("=" * 50)

    print(f"Engagement Rate:      {engagement_rate:.2f}%")

    # Average performance
    if posts > 0:
        average_likes = likes / posts
        average_comments = comments / posts
        average_interactions = (
            likes + comments
        ) / posts
    else:
        average_likes = 0
        average_comments = 0
        average_interactions = 0

    print()
    print("=" * 50)
    print("ACCOUNT ANALYSIS")
    print("=" * 50)

    print(f"Average Likes/Post:   {average_likes:.2f}")
    print(f"Average Comments/Post:{average_comments:.2f}")
    print(f"Average Interactions: {average_interactions:.2f}")

    # Recommendations
    print()
    print("=" * 50)
    print("ACCOUNT RECOMMENDATIONS")
    print("=" * 50)

    if engagement_rate >= 10:
        print("[+] Engagement is strong.")
        print(
            "Continue studying your best-performing "
            "content and repeat successful themes."
        )

    elif engagement_rate >= 3:
        print("[+] Engagement is moderate.")
        print(
            "Experiment with stronger hooks, useful topics, "
            "and clearer calls to action."
        )

    else:
        print("[-] Engagement is low.")
        print(
            "Focus on improving content value, hooks, "
            "consistency, and audience interaction."
        )

    if following > followers:
        print()
        print(
            "[!] You are following more accounts than "
            "you have followers."
        )
        print(
            "Focus on creating discoverable content "
            "and attracting relevant followers."
        )

    print("=" * 50)


# ============================================================
# POST ANALYSIS
# ============================================================

def analyze_post():
    print()
    print("Post Performance Analysis")
    print("-" * 30)

    title = input("Post title: ").strip()

    if not title:
        print("[-] Post title cannot be empty")
        return

    likes = get_non_negative_integer("Likes: ")
    comments = get_non_negative_integer("Comments: ")
    shares = get_non_negative_integer("Shares: ")
    saves = get_non_negative_integer("Saves: ")
    reach = get_non_negative_integer("Reach: ")

    total_interactions = (
        likes +
        comments +
        shares +
        saves
    )

    if reach > 0:
        engagement_rate = (
            total_interactions / reach
        ) * 100
    else:
        engagement_rate = 0.0

    if engagement_rate >= 10:
        performance = "Excellent"
        recommendation = (
            "Excellent engagement. Keep creating "
            "content similar to this post."
        )

    elif engagement_rate >= 3:
        performance = "Moderate"
        recommendation = (
            "Moderate engagement. Experiment with "
            "stronger hooks, captions, and calls to action."
        )

    else:
        performance = "Needs Improvement"
        recommendation = (
            "Engagement is low. Consider improving "
            "the content hook, topic, caption, "
            "and call to action."
        )

    print()
    print("=" * 50)
    print("POST PERFORMANCE")
    print("=" * 50)

    print(f"Post:               {title}")
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
    print(recommendation)

    print("=" * 50)


# ============================================================
# POST COMPARISON
# ============================================================

def compare_posts():
    print()
    print("Post Comparison")
    print("-" * 30)

    number_of_posts = get_positive_integer(
        "Number of posts to compare: "
    )

    posts = []

    for number in range(1, number_of_posts + 1):
        print()
        print(f"Post {number}")
        print("-" * 20)

        title = input("Post title: ").strip()

        if not title:
            title = f"Post {number}"

        likes = get_non_negative_integer("Likes: ")
        comments = get_non_negative_integer("Comments: ")
        shares = get_non_negative_integer("Shares: ")
        saves = get_non_negative_integer("Saves: ")
        reach = get_non_negative_integer("Reach: ")

        interactions = (
            likes +
            comments +
            shares +
            saves
        )

        if reach > 0:
            engagement_rate = (
                interactions / reach
            ) * 100
        else:
            engagement_rate = 0.0

        posts.append({
            "title": title,
            "likes": likes,
            "comments": comments,
            "shares": shares,
            "saves": saves,
            "reach": reach,
            "interactions": interactions,
            "engagement_rate": engagement_rate
        })

    print()
    print("=" * 75)
    print("POST COMPARISON")
    print("=" * 75)

    for index, post in enumerate(posts, start=1):
        print()
        print(f"Post {index}: {post['title']}")
        print(f"Likes:              {post['likes']}")
        print(f"Comments:           {post['comments']}")
        print(f"Shares:             {post['shares']}")
        print(f"Saves:              {post['saves']}")
        print(f"Reach:              {post['reach']}")
        print(f"Interactions:       {post['interactions']}")
        print(
            f"Engagement Rate:    "
            f"{post['engagement_rate']:.2f}%"
        )

    if posts:
        best_post = max(
            posts,
            key=lambda post: post["engagement_rate"]
        )

        print()
        print("=" * 75)
        print("BEST PERFORMING POST")
        print("=" * 75)

        print(f"Post: {best_post['title']}")
        print(
            f"Engagement Rate: "
            f"{best_post['engagement_rate']:.2f}%"
        )

        print()
        print(
            "[+] Study this post's topic, format, "
            "hook, and audience response."
        )

    print("=" * 75)


# ============================================================
# GROWTH TRACKING
# ============================================================

def track_growth():
    print()
    print("Account Growth Tracking")
    print("-" * 30)

    account_name = get_account_name()

    print()
    print("CURRENT ACCOUNT")
    print("-" * 30)

    current_followers = get_non_negative_integer(
        "Current followers: "
    )

    current_following = get_non_negative_integer(
        "Current following: "
    )

    current_posts = get_non_negative_integer(
        "Current posts: "
    )

    print()
    print("PREVIOUS ACCOUNT")
    print("-" * 30)

    previous_followers = get_non_negative_integer(
        "Previous followers: "
    )

    previous_following = get_non_negative_integer(
        "Previous following: "
    )

    previous_posts = get_non_negative_integer(
        "Previous posts: "
    )

    follower_change = (
        current_followers - previous_followers
    )

    following_change = (
        current_following - previous_following
    )

    post_change = (
        current_posts - previous_posts
    )

    if previous_followers > 0:
        follower_growth_rate = (
            follower_change /
            previous_followers
        ) * 100
    else:
        follower_growth_rate = 0.0

    if previous_posts > 0:
        post_growth_rate = (
            post_change /
            previous_posts
        ) * 100
    else:
        post_growth_rate = 0.0

    print()
    print("=" * 60)
    print("ACCOUNT GROWTH REPORT")
    print("=" * 60)

    print(f"Account:              {account_name}")

    print()
    print("FOLLOWERS")
    print("-" * 30)
    print(f"Previous:             {previous_followers}")
    print(f"Current:              {current_followers}")
    print(f"Change:               {follower_change:+d}")
    print(
        f"Growth Rate:          "
        f"{follower_growth_rate:+.2f}%"
    )

    print()
    print("FOLLOWING")
    print("-" * 30)
    print(f"Previous:             {previous_following}")
    print(f"Current:              {current_following}")
    print(f"Change:               {following_change:+d}")

    print()
    print("POSTS")
    print("-" * 30)
    print(f"Previous:             {previous_posts}")
    print(f"Current:              {current_posts}")
    print(f"Change:               {post_change:+d}")
    print(
        f"Post Growth Rate:     "
        f"{post_growth_rate:+.2f}%"
    )

    print()
    print("=" * 60)
    print("GROWTH RECOMMENDATION")
    print("=" * 60)

    if follower_change > 0:
        print(
            "[+] Your follower count increased."
        )
        print(
            "Continue identifying the content "
            "responsible for that growth."
        )

    elif follower_change == 0:
        print(
            "[!] Follower count remained unchanged."
        )
        print(
            "Test new topics, hooks, formats, "
            "and discoverability techniques."
        )

    else:
        print(
            "[-] Follower count decreased."
        )
        print(
            "Review recent content performance "
            "and audience response."
        )

    print()
    print(
        "[+] Focus on genuine audience growth "
        "rather than artificial followers."
    )

    print("=" * 60)


# ============================================================
# GROWTH STRATEGY
# ============================================================

def growth_strategy():
    print()
    print("Growth Strategy")
    print("-" * 30)

    account_name = get_account_name()

    followers = get_non_negative_integer("Followers: ")
    following = get_non_negative_integer("Following: ")
    posts = get_non_negative_integer("Posts: ")
    average_likes = get_non_negative_integer(
        "Average likes per post: "
    )
    average_comments = get_non_negative_integer(
        "Average comments per post: "
    )

    if followers > 0:
        estimated_engagement = (
            (average_likes + average_comments)
            / followers
        ) * 100
    else:
        estimated_engagement = 0.0

    print()
    print("=" * 60)
    print("INSTAGRAM GROWTH STRATEGY")
    print("=" * 60)

    print(f"Account:              {account_name}")
    print(f"Followers:            {followers}")
    print(f"Following:            {following}")
    print(f"Posts:                {posts}")
    print(f"Average Likes/Post:   {average_likes}")
    print(f"Average Comments/Post: {average_comments}")

    print()
    print("=" * 60)
    print("GROWTH RECOMMENDATIONS")
    print("=" * 60)

    print()
    print("[+] CONTENT")

    if average_likes > 0:
        print(
            "Your content is generating measurable "
            "engagement."
        )
        print(
            "Study your strongest posts and create "
            "more content around similar topics."
        )
    else:
        print(
            "Start testing different content topics "
            "and formats."
        )

    print()
    print("[+] ENGAGEMENT")

    if average_comments > 0:
        print(
            "Your content is generating conversations."
        )
        print(
            "Continue using discussion-focused content."
        )
    else:
        print(
            "Use questions and discussion prompts "
            "to encourage genuine conversations."
        )

    print()
    print("[+] CONSISTENCY")

    if posts >= 20:
        print(
            "You have enough content to identify "
            "performance patterns."
        )
        print(
            "Review your strongest posts regularly."
        )
    else:
        print(
            "Build a consistent publishing habit "
            "so you can collect more performance data."
        )

    print()
    print("[+] DISCOVERY")

    print(
        "Use relevant topics, searchable keywords, "
        "appropriate hashtags, and strong opening "
        "hooks to improve discoverability."
    )

    print()
    print("[+] AUDIENCE")

    print(
        "Create content specifically for the people "
        "you want to attract."
    )

    print()
    print("[+] GROWTH")

    print(
        "Track follower growth regularly."
    )

    print(
        "Identify which posts generate the strongest "
        "engagement and create more content around "
        "those themes."
    )

    print(
        "Prioritize genuine audience growth instead "
        "of artificial followers or engagement."
    )

    print()
    print(
        f"Estimated Engagement: "
        f"{estimated_engagement:.2f}%"
    )

    print("=" * 60)


# ============================================================
# CONTENT STRATEGY GENERATOR
# ============================================================

def content_strategy():
    print()
    print("Content Strategy Generator")
    print("-" * 30)

    while True:
        niche = input("Your niche/topic: ").strip()

        if not niche:
            print("[-] Niche cannot be empty")
            continue

        break

    while True:
        audience = input("Target audience: ").strip()

        if not audience:
            print("[-] Target audience cannot be empty")
            continue

        break

    print()
    print("Growth Goal")
    print("-" * 30)

    print("1. Increase followers")
    print("2. Increase engagement")
    print("3. Build authority")
    print("4. Generate leads")

    while True:
        goal_choice = input(
            "Choose a goal (1-4): "
        ).strip()

        if goal_choice in ("1", "2", "3", "4"):
            break

        print("[-] Please choose 1, 2, 3, or 4")

    goals = {
        "1": "Increase followers",
        "2": "Increase engagement",
        "3": "Build authority",
        "4": "Generate leads"
    }

    goal = goals[goal_choice]

    posting_frequency = get_non_negative_integer(
        "Posts per week: "
    )

    print()
    print("=" * 60)
    print("CONTENT GROWTH STRATEGY")
    print("=" * 60)

    print(f"Niche:             {niche}")
    print(f"Target Audience:   {audience}")
    print(f"Primary Goal:      {goal}")
    print(f"Posts Per Week:    {posting_frequency}")

    print()
    print("=" * 60)
    print("CONTENT PILLARS")
    print("=" * 60)

    print()
    print("1. EDUCATIONAL CONTENT")
    print("-" * 30)

    print(
        f"Create useful posts that teach your audience "
        f"something related to {niche}."
    )

    print()
    print("2. PROBLEM-SOLVING CONTENT")
    print("-" * 30)

    print(
        f"Identify common problems faced by {audience} "
        f"and create practical solutions."
    )

    print()
    print("3. EXPERIENCE / STORY CONTENT")
    print("-" * 30)

    print(
        "Share lessons learned, mistakes, progress, "
        "experiences, and behind-the-scenes content."
    )

    print()
    print("4. ENGAGEMENT CONTENT")
    print("-" * 30)

    print(
        "Use questions, opinions, comparisons, and "
        "discussion topics to encourage conversations."
    )

    print()
    print("=" * 60)
    print("CONTENT FORMATS")
    print("=" * 60)

    print()
    print("- Short-form videos / Reels")
    print("- Educational carousel posts")
    print("- Tutorials and step-by-step posts")
    print("- Progress or case-study posts")
    print("- Questions and discussion posts")
    print("- Personal experience / story posts")

    print()
    print("=" * 60)
    print("HOOK IDEAS")
    print("=" * 60)

    print()
    print(
        f'1. "5 things I wish I knew about {niche}"'
    )

    print(
        f'2. "If you are interested in {niche}, '
        f'stop doing this..."'
    )

    print(
        f'3. "Here is what nobody tells you about {niche}"'
    )

    print(
        f'4. "The beginner\'s guide to {niche}"'
    )

    print(
        '5. "I tested this so you do not have to"'
    )

    print()
    print("=" * 60)
    print("CALL-TO-ACTION IDEAS")
    print("=" * 60)

    print()
    print("1. Ask your audience a question.")
    print("2. Ask people to share their experience.")
    print("3. Encourage viewers to save useful posts.")
    print("4. Encourage people to share valuable content.")
    print("5. Invite people to follow for more content.")

    print()
    print("=" * 60)
    print("WEEKLY CONTENT PLAN")
    print("=" * 60)

    if posting_frequency == 0:
        print(
            "Set a realistic posting schedule and "
            "start tracking your results."
        )

    else:
        content_types = [
            "Educational",
            "Problem-solving",
            "Story / Experience",
            "Engagement",
            "Tutorial",
            "Reel / Short-form Video",
            "Community / Discussion"
        ]

        for day in range(1, posting_frequency + 1):
            content_type = content_types[
                (day - 1) % len(content_types)
            ]

            print(
                f"Post {day}: {content_type} content"
            )

    print()
    print("=" * 60)
    print("GROWTH PRINCIPLES")
    print("=" * 60)

    print()
    print(
        "• Create content for a specific audience."
    )

    print(
        "• Focus on providing value before asking "
        "for engagement."
    )

    print(
        "• Study which posts perform best."
    )

    print(
        "• Repeat successful content themes."
    )

    print(
        "• Test different hooks and formats."
    )

    print(
        "• Respond to genuine comments and conversations."
    )

    print(
        "• Track follower growth over time."
    )

    print()
    print(
        "[+] Strategy generated successfully."
    )

    print("=" * 60)


# ============================================================
# REPORT INFORMATION
# ============================================================

def show_version():
    print(f"insta_tool.py {VERSION}")


# ============================================================
# COMMAND LINE INTERFACE
# ============================================================

def create_parser():
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
        title="Available commands"
    )

    # Account analysis
    subparsers.add_parser(
        "analyze",
        help="Analyze Instagram account performance"
    )

    # Post analysis
    subparsers.add_parser(
        "post",
        help="Analyze individual post performance"
    )

    # Post comparison
    subparsers.add_parser(
        "compare",
        help="Compare multiple posts"
    )

    # Growth tracking
    subparsers.add_parser(
        "growth",
        help="Track account growth"
    )

    # Growth strategy
    subparsers.add_parser(
        "strategy",
        help="Generate Instagram growth recommendations"
    )

    # Content strategy
    subparsers.add_parser(
        "content",
        help="Generate a content growth strategy"
    )

    return parser


# ============================================================
# MAIN
# ============================================================

def main():
    parser = create_parser()

    args = parser.parse_args()

    display_banner()

    if args.command == "analyze":
        analyze_account()

    elif args.command == "post":
        analyze_post()

    elif args.command == "compare":
        compare_posts()

    elif args.command == "growth":
        track_growth()

    elif args.command == "strategy":
        growth_strategy()

    elif args.command == "content":
        content_strategy()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
