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

    return account_name, followers, following, posts


def display_account_information(
    account_name,
    followers,
    following,
    posts
):
    print()
    print("=" * 50)
    print("ACCOUNT INFORMATION")
    print("=" * 50)

    print(f"Account:   {account_name}")
    print(f"Followers: {followers}")
    print(f"Following: {following}")
    print(f"Posts:     {posts}")

    print("=" * 50)


def analyze_account():
    account_name, followers, following, posts = get_account_information()

    display_account_information(
        account_name,
        followers,
        following,
        posts
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

    args = parser.parse_args()

    display_banner()

    if args.command == "analyze":
        analyze_account()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
