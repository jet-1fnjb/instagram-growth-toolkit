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
    print("Version:", VERSION)
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


# ============================================================
# ACCOUNT CALCULATIONS
# ============================================================

def calculate_engagement_rate(followers, likes, comments):
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


def calculate_average_interactions(likes, comments, posts):
    if posts == 0:
        return 0.0

    interactions = likes + comments

    return interactions / posts


# ============================================================
# POST CALCULATIONS
# ============================================================

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


def calculate_interaction_rate(interactions, reach):
    if reach == 0:
        return 0.0

    return (interactions / reach) * 100


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


def identify_strongest_interaction(
    likes,
    comments,
    shares,
    saves
):
    interactions = {
        "Likes": likes,
        "Comments": comments,
        "Shares": shares,
        "Saves": saves
    }

    strongest = max(
        interactions,
        key=interactions.get
    )

    return strongest, interactions[strongest]


def generate_content_insight(
    likes,
    comments,
    shares,
    saves
):
    strongest, value = identify_strongest_interaction(
        likes,
        comments,
        shares,
        saves
    )

    if value == 0:
        return (
            "No significant interactions were recorded. "
            "Consider improving the content topic, hook, "
            "caption, and call to action."
        )

    if strongest == "Saves":
        return (
            "Saves are the strongest interaction. Consider "
            "creating more educational, useful, or "
            "reference-style content."
        )

    if strongest == "Shares":
        return (
            "Shares are the strongest interaction. Consider "
            "creating more relatable, entertaining, or "
            "highly shareable content."
        )

    if strongest == "Comments":
        return (
            "Comments are the strongest interaction. Consider "
            "using questions and discussion-focused captions."
        )

    return (
        "Likes are the strongest interaction. Continue testing "
        "strong visual content and engaging topics."
    )


# ============================================================
# REPORT FUNCTIONS
# ============================================================

def save_report(filename, content):
    REPORTS_DIR.mkdir(exist_ok=True)

    report_path = REPORTS_DIR / filename

    report_path.write_text(
        content,
        encoding="utf-8"
    )

    return report_path


def build_post_report(
    post_title,
    likes,
    comments,
    shares,
    saves,
    reach,
    engagement_rate,
    performance
):
    total_interactions = (
        likes
        + comments
        + shares
        + saves
    )

    like_rate = calculate_interaction_rate(
        likes,
        reach
    )

    comment_rate = calculate_interaction_rate(
        comments,
        reach
    )

    share_rate = calculate_interaction_rate(
        shares,
        reach
    )

    save_rate = calculate_interaction_rate(
        saves,
        reach
    )

    recommendation = get_post_recommendation(
        performance
    )

    insight = generate_content_insight(
        likes,
        comments,
        shares,
        saves
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    report = f"""
==================================================
INSTAGRAM POST PERFORMANCE REPORT
==================================================

Generated: {timestamp}

Post:               {post_title}

--------------------------------------------------
POST METRICS
--------------------------------------------------

Likes:              {likes}
Comments:           {comments}
Shares:             {shares}
Saves:              {saves}
Reach:              {reach}
Total Interactions: {total_interactions}

--------------------------------------------------
ENGAGEMENT ANALYSIS
--------------------------------------------------

Engagement Rate:    {engagement_rate:.2f}%
Performance:        {performance}

--------------------------------------------------
INTERACTION RATES
--------------------------------------------------

Like Rate:          {like_rate:.2f}%
Comment Rate:       {comment_rate:.2f}%
Share Rate:         {share_rate:.2f}%
Save Rate:          {save_rate:.2f}%

--------------------------------------------------
RECOMMENDATION
--------------------------------------------------

{recommendation}

--------------------------------------------------
CONTENT INSIGHT
--------------------------------------------------

{insight}

==================================================
END OF REPORT
==================================================
"""

    return report


def build_growth_report(
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
    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    if follower_change > 0:
        follower_summary = "Follower count increased."

    elif follower_change < 0:
        follower_summary = "Follower count decreased."

    else:
        follower_summary = "Follower count remained unchanged."

    report = f"""
==================================================
INSTAGRAM ACCOUNT GROWTH REPORT
==================================================

Generated: {timestamp}

--------------------------------------------------
STARTING METRICS
--------------------------------------------------

Followers:           {starting_followers}
Following:           {starting_following}
Posts:               {starting_posts}

--------------------------------------------------
CURRENT METRICS
--------------------------------------------------

Followers:           {current_followers}
Following:           {current_following}
Posts:               {current_posts}

--------------------------------------------------
GROWTH ANALYSIS
--------------------------------------------------

Follower Change:     {follower_change:+d}
Follower Growth:     {follower_growth_rate:+.2f}%

Following Change:    {following_change:+d}

Post Change:         {post_change:+d}
Post Growth:         {post_growth_rate:+.2f}%

--------------------------------------------------
SUMMARY
--------------------------------------------------

{follower_summary}

==================================================
END OF REPORT
==================================================
"""

    return report


# ============================================================
# ACCOUNT ANALYSIS
# ============================================================

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
    total_interactions = (
        likes
        + comments
        + shares
        + saves
    )

    like_rate = calculate_interaction_rate(
        likes,
        reach
    )

    comment_rate = calculate_interaction_rate(
        comments,
        reach
    )

    share_rate = calculate_interaction_rate(
        shares,
        reach
    )

    save_rate = calculate_interaction_rate(
        saves,
        reach
    )

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

    print(f"Like Rate:          {like_rate:.2f}%")
    print(f"Comment Rate:       {comment_rate:.2f}%")
    print(f"Share Rate:         {share_rate:.2f}%")
    print(f"Save Rate:          {save_rate:.2f}%")

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
        generate_content_insight(
            likes,
            comments,
            shares,
            saves
        )
    )

    print("=" * 50)


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

    report = build_post_report(
        post_title,
        likes,
        comments,
        shares,
        saves,
        reach,
        engagement_rate,
        performance
    )

    filename = (
        "post_"
        + datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        + ".txt"
    )

    report_path = save_report(
        filename,
        report
    )

    print()
    print(
        f"[+] Report saved to: {report_path}"
    )


# ============================================================
# POST COMPARISON
# ============================================================

def display_post_comparison(posts):
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
            f"{post['engagement_rate']:.2f}%"
            f"{'':<10}"
            f"{post['performance']:<15}"
        )

    print("=" * 80)

    best_post = max(
        posts,
        key=lambda post: post["engagement_rate"]
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
        f"'{best_post['title']}' generated the highest "
        "engagement rate among the posts analyzed."
    )

    print(
        "Consider studying its topic, format, hook, "
        "caption, and audience response."
    )

    print("=" * 80)


def build_comparison_report(posts):
    best_post = max(
        posts,
        key=lambda post: post["engagement_rate"]
    )

    average_engagement = (
        sum(
            post["engagement_rate"]
            for post in posts
        )
        / len(posts)
    )

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    lines = []

    lines.append("=" * 80)
    lines.append("INSTAGRAM POST COMPARISON REPORT")
    lines.append("=" * 80)
    lines.append("")
    lines.append(f"Generated: {timestamp}")
    lines.append("")

    lines.append("-" * 80)
    lines.append("POST COMPARISON")
    lines.append("-" * 80)

    lines.append(
        f"{'POST':<25}"
        f"{'REACH':<10}"
        f"{'INTERACTIONS':<15}"
        f"{'ENGAGEMENT':<15}"
        f"{'PERFORMANCE':<15}"
    )

    lines.append("-" * 80)

    for post in posts:
        lines.append(
            f"{post['title'][:24]:<25}"
            f"{post['reach']:<10}"
            f"{post['interactions']:<15}"
            f"{post['engagement_rate']:.2f}%"
            f"{'':<10}"
            f"{post['performance']:<15}"
        )

    lines.append("")
    lines.append("-" * 80)
    lines.append("COMPARISON SUMMARY")
    lines.append("-" * 80)

    lines.append(
        f"Posts Compared:       "
        f"{len(posts)}"
    )

    lines.append(
        f"Average Engagement:   "
        f"{average_engagement:.2f}%"
    )

    lines.append(
        f"Best Performing Post: "
        f"{best_post['title']}"
    )

    lines.append(
        f"Best Engagement Rate: "
        f"{best_post['engagement_rate']:.2f}%"
    )

    lines.append("")
    lines.append("-" * 80)
    lines.append("CONTENT INSIGHT")
    lines.append("-" * 80)

    lines.append(
        f"'{best_post['title']}' generated the highest "
        "engagement rate among the posts analyzed."
    )

    lines.append(
        "Consider studying its topic, format, hook, "
        "caption, and audience response."
    )

    lines.append("")
    lines.append("=" * 80)
    lines.append("END OF REPORT")
    lines.append("=" * 80)

    return "\n".join(lines)


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

    for index in range(
        1,
        number_of_posts + 1
    ):
        print()
        print(f"POST {index}")
        print("-" * 30)

        while True:
            title = input(
                "Post title: "
            ).strip()

            if not title:
                print(
                    "[-] Post title cannot be empty"
                )
                continue

            break

        likes = get_non_negative_integer(
            "Likes: "
        )

        comments = get_non_negative_integer(
            "Comments: "
        )

        shares = get_non_negative_integer(
            "Shares: "
        )

        saves = get_non_negative_integer(
            "Saves: "
        )

        reach = get_non_negative_integer(
            "Reach: "
        )

        engagement_rate = (
            calculate_post_engagement_rate(
                likes,
                comments,
                shares,
                saves,
                reach
            )
        )

        total_interactions = (
            likes
            + comments
            + shares
            + saves
        )

        performance = (
            determine_post_performance(
                engagement_rate
            )
        )

        posts.append({
            "title": title,
            "likes": likes,
            "comments": comments,
            "shares": shares,
            "saves": saves,
            "reach": reach,
            "interactions": total_interactions,
            "engagement_rate": engagement_rate,
            "performance": performance
        })

    display_post_comparison(posts)

    report = build_comparison_report(
        posts
    )

    filename = (
        "comparison_"
        + datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        + ".txt"
    )

    report_path = save_report(
        filename,
        report
    )

    print()
    print(
        f"[+] Report saved to: {report_path}"
    )


# ============================================================
# MILESTONE 9 — ACCOUNT GROWTH TRACKING
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

    # Calculate changes

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

    # Calculate growth percentages

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

    # Display results

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

    # Create report

    report = build_growth_report(
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

    filename = (
        "growth_"
        + datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )
        + ".txt"
    )

    report_path = save_report(
        filename,
        report
    )

    print()
    print(
        f"[+] Report saved to: {report_path}"
    )


# ============================================================
# MAIN PROGRAM
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

    # Individual post analysis

    subparsers.add_parser(
        "post",
        help="Analyze individual post performance"
    )

    # Multiple post comparison

    subparsers.add_parser(
        "compare",
        help="Compare multiple posts"
    )

    # Account growth tracking

    subparsers.add_parser(
        "growth",
        help="Track account growth"
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

    else:
        parser.print_help()


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
