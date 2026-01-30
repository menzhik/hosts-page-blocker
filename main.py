#!/usr/bin/env python3
"""
Block URLs by rerouting them to localhost through
the addition of rules in the system's hosts file.
"""

import platform
import re


def get_os_name():
    """Get the current OS name."""
    return platform.system()


def get_hosts_path():
    """Determine the path to the hosts file based on the current OS."""
    system_name = get_os_name()
    if system_name == "Windows":
        return "C:\\Windows\\System32\\drivers\\etc\\hosts"
    if system_name in ("Linux", "Darwin"):  # Darwin = macOS
        return "/etc/hosts"
    raise OSError(f"Unsupported OS: {system_name}")


def prompt_for_number_of_pages():
    """Prompt for an integer"""
    while True:
        try:
            return int(input("Number of pages: "))
        except ValueError:
            print("Incorrect input. Enter an integer!")


def prompt_for_url():
    """Prompt for a link and ensure it doesn't contain unnecessary prefix"""
    url = input("Enter URL: ").strip()
    return re.sub(r"^(?:https?://)?(?:www\.)?", "", url)


def get_all_hostnames(urls):
    """
    Generate hostnames for /etc/hosts (NO http:// or https://).
    
    For each URL, generate:
    - example.com
    - www.example.com (if not already www)
    
    Deduplicate to avoid redundant entries.
    """
    hostnames = set()
    for url in urls:
        hostnames.add(url)
        if not url.startswith("www."):
            hostnames.add(f"www.{url}")
    return sorted(hostnames)


def ipv4_block_entry(hostname):
    """Generate an IPv4 block entry for a given hostname."""
    return "0.0.0.0" + "\t\t" + hostname + "\n"


def ipv6_block_entry(hostname):
    """Generate an IPv6 block entry for a given hostname."""
    return "::1" + "\t\t" + hostname + "\n"


def append_to_hosts(urls, hosts_path):
    """Append URLs to the hosts file to block them."""
    with open(hosts_path, "a", encoding="utf-8") as hosts_file:
        hosts_file.write("\n")
        for url in urls:
            hosts_file.write(ipv4_block_entry(url))
            hosts_file.write(ipv6_block_entry(url))
    print("URLs have been successfully blocked!")


def check_is_sudo(system_name):
    """Check if the script is running with admin/root privileges."""
    if system_name in ("Linux", "Darwin"):
        import os
        return os.geteuid() == 0

    if system_name == "Windows":
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

    return False


def main():
    """Prompt for URLs and append them to the hosts file to block them."""
    system_name = get_os_name()
    
    if not check_is_sudo(system_name):
        exit("Error: This script requires admin/root privileges.\n"
             "  Linux/macOS: Run with 'sudo python3 main.py'\n"
             "  Windows: Run terminal as Administrator")

    hosts_path = get_hosts_path()
    n = prompt_for_number_of_pages()
    urls = []
    for _ in range(n):
        urls.append(prompt_for_url())
    append_to_hosts(get_all_hostnames(urls), hosts_path)


if __name__ == "__main__":
    main()
