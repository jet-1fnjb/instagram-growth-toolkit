#!/usr/bin/env python3

"""
Instagram Growth & Analytics Toolkit

Purpose:
    A learning-focused toolkit for Instagram analytics
    and ethical audience-growth planning.

Features:
    - Account analysis
    - Post analysis
    - Post comparison
    - Account growth tracking
    - Growth strategy recommendations
    - Text report generation

Version: 0.1
"""

import argparse
from datetime import datetime
from pathlib import Path


TOOL_NAME = "Instagram Growth & Analytics Toolkit"
VERSION = "0.1"

REPORTS_DIR = Path("reports")


# ============================================================
# DISPLAY
# ============================================================

def display_banner():
    print("=" * 50)
    print(TOOL_NAME)
    print(f"Version: {VERSION}")
    print("=" * 50)


# ============================================================
# INPUT VALIDATION
# ============================================================

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


def get_account_name():
    while True:
        account_name = input("Account name: ").strip()

        if not account_name:
            print("[-] Account name cannot be empty")
            continue

        return account_name


def get_account_information():
    print()
    print("Account Information")
    print("-" * 30)

    account_name = get_account_name()

    followers = get_non_negative_integer("Followers: ")
    following = get_non_negative_integer("Following: ")
    posts = get_non_negative_integer("Posts: ")
    likes = get_non_negative_integer("Likes: ")
    comments = get_non_negative_integer("Comments: ")

    return {
        "account_name": account_name,
        "followers": followers,
        "following": following,
        "posts": posts,
        "likes": likes,
        "comments": comments
    }


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

    return {
        "title": post_title,
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "saves": saves,
        "reach": reach
    }


# ============================================================
# ACCOUNT ANALYSIS
# ============================================================

def calculate_account_engagement_rate(
    followers,
    likes,
    comments
):
    if followers == 0:
        return 0.0

    interactions = likes + comments

    return (interactions / followers) * 100


def calculate_average_likes(likes, posts):
    if posts == 0:
        return 0.0

    return likes / posts


def calculate_average_comments(comments, posts):
    if posts == 0:
        return 0.0

    return comments / posts


def calculate_average_interactions(
    likes,
    comments,
    posts
):
    if posts == 0:
        return 0.0

    return (likes + comments) / posts


def analyze_account():
    account = get_account_information()

    engagement_rate = calculate_account_engagement_rate(
        account["followers"],
        account["likes"],
        account["comments"]
    )

    average_likes = calculate_average_likes(
        account["likes"],
        account["posts"]
    )

    average_comments = calculate_average_comments(
        account["comments"],
        account["posts"]
    )

    average_interactions = calculate_average_interactions(
        account["likes"],
        account["comments"],
        account["posts"]
    )

    print()
    print("=" * 50)
    print("ACCOUNT INFORMATION")
    print("=" * 50)

    print(
        f"Account:              "
        f"{account['account_name']}"
    )

    print(
        f"Followers:            "
        f"{account['followers']}"
    )

    print(
        f"Following:            "
        f"{account['following']}"
    )

    print(
        f"Posts:                "
        f"{account['posts']}"
    )

    print(
        f"Likes:                "
        f"{account['likes']}"
    )

    print(
        f"Comments:             "
        f"{account['comments']}"
    )

    print()
    print("=" * 50)
    print("ACCOUNT ANALYSIS")
    print("=" * 50)

    print(
        f"Engagement Rate:      "
        f"{engagement_rate:.2f}%"
    )

    print(
        f"Average Likes/Post:   "
        f"{average_likes:.2f}"
    )

    print(
        f"Average Comments/Post:"
        f" {average_comments:.2f}"
    )

    print(
        f"Average Interactions: "
        f"{average_interactions:.2f}"
    )

    print("=" * 50)


# ============================================================
# POST ANALYSIS
# ============================================================

def calculate_post_engagement_rate(post):
    if post["reach"] == 0:
        return 0.0

    interactions = (
        post["likes"]
        + post["comments"]
        + post["shares"]
        + post["saves"]
    )

    return (
        interactions
        / post["reach"]
    ) * 100


def calculate_interaction_rate(
    interaction,
    reach
):
    if reach == 0:
        return 0.0

    return (interaction / reach) * 100


def determine_post_performance(
    engagement_rate
):
    if engagement_rate >= 10:
        return "Excellent"

    if engagement_rate >= 5:
        return "Moderate"

    return "Needs Improvement"


def get_post_recommendation(
    performance
):
    if performance == "Excellent":
        return (
            "Excellent engagement. Keep creating "
            "content similar to this post."
        )

    if performance == "Moderate":
        return (
            "Moderate engagement. Experiment with "
            "stronger hooks, captions, and calls to action."
        )

    return (
        "Engagement is low. Consider improving the "
        "content hook, topic, caption, and call to action."
    )


def identify_strongest_interaction(post):
    interactions = {
        "Likes": post["likes"],
        "Comments": post["comments"],
        "Shares": post["shares"],
        "Saves": post["saves"]
    }

    strongest = max(
        interactions,
        key=interactions.get
    )

    return strongest, interactions[strongest]


def generate_content_insight(post):
    strongest, value = identify_strongest_interaction(
        post
    )

    if value == 0:
        return (
            "No significant interactions were recorded. "
            "Consider improving the content topic, hook, "
            "caption, and call to action."
        )

    if strongest == "Saves":
        return (
            "Saves are the strongest interaction. "
            "Consider creating more educational, useful, "
            "or reference-style content."
        )

    if strongest == "Shares":
        return (
            "Shares are the strongest interaction. "
            "Consider creating more relatable, entertaining, "
            "or highly shareable content."
        )

    if strongest == "Comments":
        return (
            "Comments are the strongest interaction. "
            "Consider using questions and discussion-focused "
            "captions."
        )

    return (
        "Likes are the strongest interaction. "
        "Continue testing strong visual content and "
        "engaging topics."
    )


def analyze_post():
    post = get_post_information()

    engagement_rate = (
        calculate_post_engagement_rate(post)
    )

    performance = determine_post_performance(
        engagement_rate
    )

    total_interactions = (
        post["likes"]
        + post["comments"]
        + post["shares"]
        + post["saves"]
    )

    print()
    print("=" * 50)
    print("POST PERFORMANCE")
    print("=" * 50)

    print(
        f"Post:               "
        f"{post['title']}"
    )

    print(
        f"Likes:              "
        f"{post['likes']}"
    )

    print(
        f"Comments:           "
        f"{post['comments']}"
    )

    print(
        f"Shares:             "
        f"{post['shares']}"
    )

    print(
        f"Saves:              "
        f"{post['saves']}"
    )

    print(
        f"Reach:              "
        f"{post['reach']}"
    )

    print(
        f"Total Interactions: "
        f"{total_interactions}"
    )

    print()
    print("=" * 50)
    print("POST ANALYSIS")
    print("=" * 50)

    print(
        f"Engagement Rate:    "
        f"{engagement_rate:.2f}%"
    )

    print(
        f"Performance:        "
        f"{performance}"
    )

    print()
    print("INTERACTION RATES")
    print("-" * 30)

    print(
        f"Like Rate:          "
        f"{calculate_interaction_rate(post['likes'], post['reach']):.2f}%"
    )

    print(
        f"Comment Rate:       "
        f"{calculate_interaction_rate(post['comments'], post['reach']):.2f}%"
    )

    print(
        f"Share Rate:         "
        f"{calculate_interaction_rate(post['shares'], post['reach']):.2f}%"
    )

    print(
        f"Save Rate:          "
        f"{calculate_interaction_rate(post['saves'], post['reach']):.2f}%"
    )

    print()
    print("RECOMMENDATION")
    print("-" * 30)

    print(
        get_post_recommendation(
            performance
        )
    )

    print()
    print("CONTENT INSIGHT")
    print("-" * 30)

    print(
        generate_content_insight(post)
    )

    print("=" * 50)


# ============================================================
# POST COMPARISON
# ============================================================

def collect_comparison_post(number):
    print()
    print(f"POST {number}")
    print("-" * 30)

    post = get_post_information()

    post["engagement_rate"] = (
        calculate_post_engagement_rate(post)
    )

    post["interactions"] = (
        post["likes"]
        + post["comments"]
        + post["shares"]
        + post["saves"]
    )

    post["performance"] = (
        determine_post_performance(
            post["engagement_rate"]
        )
    )

    return post


def compare_posts():
    print()
    print("Multiple Post Comparison")
    print("-" * 30)

    number_of_posts = get_non_negative_integer(
        "Number of posts to compare: "
    )

    if number_of_posts == 0:
        print("[-] At least one post is required")
        return

    posts = []

    for number in range(
        1,
        number_of_posts + 1
    ):
        posts.append(
            collect_comparison_post(number)
        )

    print()
    print("=" * 80)
    print("POST COMPARISON")
    print("=" * 80)

    print(
        f"{'POST':<25}"
        f"{'REACH':<10}"
        f"{'INTERACTIONS':<15}"
        f"{'ENGAGEMENT':<15}"
        f"{'PERFORMANCE':<15}"
    )

    print("-" * 80)

    for post in posts:
        print(
            f"{post['title'][:24]:<25}"
            f"{post['reach']:<10}"
            f"{post['interactions']:<15}"
            f"{post['engagement_rate']:<15.2f}"
            f"{post['performance']:<15}"
        )

    print("=" * 80)

    best_post = max(
        posts,
        key=lambda item: item["engagement_rate"]
    )

    average_engagement = (
        sum(
            post["engagement_rate"]
            for post in posts
        )
        / len(posts)
    )

    print()
    print("COMPARISON SUMMARY")
    print("-" * 30)

    print(
        f"Posts Compared:       "
        f"{len(posts)}"
    )

    print(
        f"Average Engagement:   "
        f"{average_engagement:.2f}%"
    )

    print(
        f"Best Performing Post: "
        f"{best_post['title']}"
    )

    print(
        f"Best Engagement Rate: "
        f"{best_post['engagement_rate']:.2f}%"
    )

    print()
    print("CONTENT INSIGHT")
    print("-" * 30)

    print(
        f"'{best_post['title']}' generated the "
        "highest engagement rate."
    )

    print(
        "Consider studying its topic, format, "
        "hook, caption, and audience response."
    )

    print("=" * 80)


# ============================================================
# ACCOUNT GROWTH TRACKING
# ============================================================

def track_growth():
    print()
    print("Account Growth Tracking")
    print("-" * 30)

    print()
    print("Starting Metrics")
    print("-" * 30)

    starting_followers = get_non_negative_integer(
        "Starting followers: "
    )

    starting_following = get_non_negative_integer(
        "Starting following: "
    )

    starting_posts = get_non_negative_integer(
        "Starting posts: "
    )

    print()
    print("Current Metrics")
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

    follower_change = (
        current_followers
        - starting_followers
    )

    following_change = (
        current_following
        - starting_following
    )

    post_change = (
        current_posts
        - starting_posts
    )

    if starting_followers == 0:
        follower_growth_rate = 0.0
    else:
        follower_growth_rate = (
            follower_change
            / starting_followers
        ) * 100

    if starting_posts == 0:
        post_growth_rate = 0.0
    else:
        post_growth_rate = (
            post_change
            / starting_posts
        ) * 100

    print()
    print("=" * 50)
    print("ACCOUNT GROWTH ANALYSIS")
    print("=" * 50)

    print(
        f"Follower Change:     "
        f"{follower_change:+d}"
    )

    print(
        f"Follower Growth:     "
        f"{follower_growth_rate:+.2f}%"
    )

    print(
        f"Following Change:    "
        f"{following_change:+d}"
    )

    print(
        f"Post Change:         "
        f"{post_change:+d}"
    )

    print(
        f"Post Growth:         "
        f"{post_growth_rate:+.2f}%"
    )

    print("=" * 50)

    save_growth_report(
        starting_followers,
        starting_following,
        starting_posts,
        current_followers,
        current_following,
        current_posts,
        follower_change,
        follower_growth_rate,
        following_change,
        post_change,
        post_growth_rate
    )


def save_growth_report(
    starting_followers,
    starting_following,
    starting_posts,
    current_followers,
    current_following,
    current_posts,
    follower_change,
    follower_growth_rate,
    following_change,
    post_change,
    post_growth_rate
):
    REPORTS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    report = f"""
==================================================
INSTAGRAM ACCOUNT GROWTH REPORT
==================================================

Generated: {timestamp}

STARTING METRICS
------------------------------
Followers: {starting_followers}
Following: {starting_following}
Posts:     {starting_posts}

CURRENT METRICS
------------------------------
Followers: {current_followers}
Following: {current_following}
Posts:     {current_posts}

GROWTH ANALYSIS
------------------------------
Follower Change:  {follower_change:+d}
Follower Growth:  {follower_growth_rate:+.2f}%

Following Change: {following_change:+d}

Post Change:      {post_change:+d}
Post Growth:      {post_growth_rate:+.2f}%

==================================================
END OF REPORT
==================================================
"""

    filename = (
        "growth_"
        + datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        + ".txt"
    )

    report_path = REPORTS_DIR / filename

    report_path.write_text(
        report,
        encoding="utf-8"
    )

    print()
    print(
        f"[+] Report saved to: {report_path}"
    )


# ============================================================
# GROWTH STRATEGY ENGINE
# ============================================================

def growth_strategy():
    print()
    print("Growth Strategy")
    print("-" * 30)

    account_name = get_account_name()

    followers = get_non_negative_integer(
        "Followers: "
    )

    following = get_non_negative_integer(
        "Following: "
    )

    posts = get_non_negative_integer(
        "Posts: "
    )

    average_likes = get_non_negative_integer(
        "Average likes per post: "
    )

    average_comments = get_non_negative_integer(
        "Average comments per post: "
    )

    print()
    print("=" * 50)
    print("INSTAGRAM GROWTH STRATEGY")
    print("=" * 50)

    print(
        f"Account:              {account_name}"
    )

    print(
        f"Followers:            {followers}"
    )

    print(
        f"Following:            {following}"
    )

    print(
        f"Posts:                {posts}"
    )

    print(
        f"Average Likes/Post:   {average_likes}"
    )

    print(
        f"Average Comments/Post:"
        f" {average_comments}"
    )

    print()
    print("=" * 50)
    print("GROWTH RECOMMENDATIONS")
    print("=" * 50)

    # --------------------------------------------------------
    # CONTENT
    # --------------------------------------------------------

    print()
    print("[+] CONTENT")

    if average_likes == 0:
        print(
            "Focus on creating useful and relevant content "
            "that gives people a reason to engage."
        )

    elif followers > 0 and average_likes < (
        followers * 0.05
    ):
        print(
            "Average likes are relatively low compared "
            "with your follower count."
        )

        print(
            "Test stronger hooks, visuals, topics, "
            "captions, and content formats."
        )

    else:
        print(
            "Your content is generating reasonable "
            "engagement."
        )

        print(
            "Study your strongest posts and create "
            "more content around similar topics."
        )

    # --------------------------------------------------------
    # ENGAGEMENT
    # --------------------------------------------------------

    print()
    print("[+] ENGAGEMENT")

    if average_comments < 5:
        print(
            "Encourage meaningful conversations by "
            "asking questions in your captions."
        )

    else:
        print(
            "Your content is generating conversations."
        )

        print(
            "Continue using discussion-focused content."
        )

    # --------------------------------------------------------
    # CONSISTENCY
    # --------------------------------------------------------

    print()
    print("[+] CONSISTENCY")

    if posts < 10:
        print(
            "Build a consistent content library before "
            "judging long-term growth."
        )

    elif posts < 30:
        print(
            "You are building a content history."
        )

        print(
            "Continue posting consistently and track "
            "which topics perform best."
        )

    else:
        print(
            "You have enough content to identify "
            "performance patterns."
        )

        print(
            "Review your strongest posts regularly."
        )

    # --------------------------------------------------------
    # AUDIENCE
    # --------------------------------------------------------

    print()
    print("[+] AUDIENCE")

    if followers == 0:
        print(
            "Define a specific target audience and "
            "create content that solves their problems "
            "or provides useful information."
        )

    elif following > followers:
        print(
            "Your following count is higher than your "
            "follower count."
        )

        print(
            "Focus more on discoverable, valuable content "
            "rather than simply following more accounts."
        )

    else:
        print(
            "Continue creating content that provides "
            "clear value to your target audience."
        )

    # --------------------------------------------------------
    # DISCOVERY
    # --------------------------------------------------------

    print()
    print("[+] DISCOVERY")

    print(
        "Use relevant topics, searchable keywords, "
        "appropriate hashtags, and strong opening hooks "
        "to improve content discoverability."
    )

    # --------------------------------------------------------
    # GROWTH
    # --------------------------------------------------------

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
    print("=" * 50)


# ============================================================
# COMMAND-LINE INTERFACE
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description=TOOL_NAME
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

    # Account growth

    subparsers.add_parser(
        "growth",
        help="Track account growth"
    )

    # Growth strategy

    subparsers.add_parser(
        "strategy",
        help="Generate Instagram growth recommendations"
    )

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

    else:
        parser.print_help()


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
