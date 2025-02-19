import os
import json
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from urllib.parse import quote  # For URL encoding
import time  # For adding delays
import subprocess
import shutil
import requests
import aiohttp
import asyncio
import multiprocessing
import tkinter as tk
import webbrowser
from bs4 import BeautifulSoup
import threading
from user_agents import USER_AGENTS
from SOCIAL_MEDIA_OSINT_TOOLS1 import SOCIAL_MEDIA_OSINT_TOOLS
from Dorking_methodM import dorking_methods
from resultsorking_methods import resultsorking_methods
from Ascii import Ascii
from urllib.parse import quote
import aiofiles
import random
import sys





def generate_username_variations(first_name, surname, max_variations=50):
    first_name = first_name.lower()
    surname = surname.lower()
    variations = [
        # Just the first name
        first_name,
        # Just the surname
        surname,
        # firstname.surname
        f"{first_name}.{surname}",
        # surname.firstname
        f"{surname}.{first_name}",
        # firstname-surname
        f"{first_name}-{surname}",
        # surname-firstname
        f"{surname}-{first_name}",
        # firstnamesurname
        f"{first_name}{surname}",
        # surnamefirstname
        f"{surname}{first_name}",
        # firstname_surname
        f"{first_name}_{surname}",
        # surname_firstname
        f"{surname}_{first_name}",
        # F.surname
        f"{first_name[0]}.{surname}",
        # S.firstname
        f"{surname[0]}.{first_name}",
        # surname.F
        f"{surname}.{first_name[0]}",
        # firstname.S
        f"{first_name}.{surname[0]}",
        # F-surname
        f"{first_name[0]}-{surname}",
        # S-firstname
        f"{surname[0]}-{first_name}",
        # surname-F
        f"{surname}-{first_name[0]}",
        # firstname-S
        f"{first_name}-{surname[0]}",
        # Fsurname
        f"{first_name[0]}{surname}",
        # Sfirstname
        f"{surname[0]}{first_name}",
        # surnameF
        f"{surname}{first_name[0]}",
        # firstnameS
        f"{first_name}{surname[0]}",
        # F_surname
        f"{first_name[0]}_{surname}",
        # S_firstname
        f"{surname[0]}_{first_name}",
        # surname_F
        f"{surname}_{first_name[0]}",
        # firstname_S
        f"{first_name}_{surname[0]}",
        ]
    # Add uppercase variations
    variations += [v.capitalize() for v in variations]
    return variations[:max_variations]  # Return only the first `max_variations`

# Suppress all logging messages
logging.basicConfig(level=logging.CRITICAL)




# Function to validate URLs with retries and session reuse
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def send_to_log(message):
    """ Write OSINT results to a log file, which the new terminal will display in real time. """
    with open("/tmp/osint_results.log", "a") as log_file:
        log_file.write(message + "\n")




async def validate_url(url, session):
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=3), ssl=False) as response:
            if hasattr(response, 'status'):
                if response.status == 200:
                    result = f"{url} - ✅ Valid"
                elif response.status == 404:
                    result = f"{url} - ❌ Not Found"
                elif response.status == 200:
                    result = f"{url} - ✅ Valid"
                else:
                    result = f"{url} - Status {response.status}"
            else:
                result = f"{url} - 🔴 Invalid Response Object"
    except asyncio.TimeoutError:
        result = f"{url} - 🔴 Timeout Error"
    except Exception as e:
        result = f"{url} - 🔴 Error: {e}"

    send_to_log(result)  # Send output to results terminal in real time
    return url, result





async def validate_urls_in_batches(urls, batch_size=1500, max_workers=1000):
    results = []  # This will store validation results
    connector = aiohttp.TCPConnector(limit=max_workers, force_close=True)
    
    async with aiohttp.ClientSession(connector=connector) as session:
        for i in range(0, len(urls), batch_size):
            batch = urls[i:i + batch_size]
            tasks = [validate_url(url, session) for url in batch]
            batch_results = await asyncio.gather(*tasks)
            results.extend(batch_results)  # Store the results
    
    return results  # Return results correctly




async def validate_urls_concurrently(urls, max_workers=500):
    results = []
    
    # Create an aiohttp session with a high connection limit
    connector = aiohttp.TCPConnector(limit=max_workers, force_close=True)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [validate_url(url, session) for url in urls]
        
        # Use tqdm to show progress
        progress_bar = tqdm(total=len(tasks), desc="Validating URLs", unit="URL", position=0, leave=True)
        for future in asyncio.as_completed(tasks):
            result = await future
            results.append(result)
            progress_bar.update(1)  # ✅ Only update manually
        progress_bar.close()  # ✅ Close once done

    
    return results  # Return results at the end


async def google_custom_search_async(username, method, temp_file):
    """Asynchronous function to perform Google Custom Search."""
    query = method["link"].format(username=username)  # Use method parameter instead of dorking_methods
    url = f"https://www.googleapis.com/customsearch/v1?q={quote(query)}"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    results = await response.json()

                    if "items" in results:
                        for i, item in enumerate(results["items"], start=1):
                            print(f"{i}. {item['title']}\n{item['link']}\n")
                            print("Information Saved To Google Dorking File")
                    else:
                        print("No results found.")
                else:
                    print(f"Error: Received status code {response.status}")
        except aiohttp.ClientError as e:
            print(f"Error: {e}")

# Insert before or after fetch_google_results function
async def fetch_google_results(session, search_url):
    """Fetch Google search results and parse the top links asynchronously while avoiding blocks."""
    headers = {
        "User-Agent": random.choice(USER_AGENTS)  # Rotate user agents to bypass detection
    }





async def fetch_google_results(session, search_url):
    """Fetch Google search results and parse the top links asynchronously while avoiding blocks."""
    headers = {
        "User-Agent": random.choice(USER_AGENTS)  # Rotate user agents to bypass detection
    }

    try:
        async with session.get(search_url, headers=headers, timeout=10) as response:
            if response.status == 429:  # Too many requests (Google blocked us)
                return [f"(Saved to Google dorking file)"]

            if response.status != 200:
                return [f"Google returned status {response.status}"]

            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")

            results = []
            for g in soup.select("div.tF2Cxc"):  # Extract valid search results
                title = g.select_one("h3")
                link_tag = g.select_one("a")

                if title and link_tag:
                    link = link_tag["href"]
                    if link.startswith("/url?q="):
                        link = link.split("/url?q=")[1].split("&")[0]  # Extract actual URL

                    results.append(f"{title.text.strip()} - {link}")

                if len(results) >= 5:  # Limit to top 5 results
                    break

            return results if results else ["No results found."]

    except Exception as e:
        return [f"Error fetching search results: {e}"]


    

async def open_google_dork_async(username_variations):
    #print other def i tink or mi gon tek mei oewn leaf
    await google_dorking(username_variations)
    temp_file = "/tmp/google_dork_results.log"
    await write_terminal_log(temp_file, "[*] Google Dorking process started...", style='info')

    total_queries = len(username_variations) * len(dorking_methods)
    google_dorking_bar = tqdm(total=total_queries, desc="Google Dorking Progress", unit="queries", position=0, leave=True)

    async with aiohttp.ClientSession() as session:
        for username in username_variations:
            for method in dorking_methods:
                query = f'"{username}" site:{method["name"].lower()}.com'
                search_url = f"https://www.google.com/search?q={quote(query)}"

                await write_terminal_log(temp_file, f"\n[+] Checking {method['name']} for {username}", style='info')

                results = await fetch_google_results(session, search_url)

                google_dorking_bar.update(1)  # ✅ Keep progress separate

    google_dorking_bar.close()





async def extract_username_info(username_variations, first_name, surname):
    """Fetch and scrape info related to the generated usernames from multiple OSINT sources with a progress bar."""
    all_info = {}
    
    async def validate_url(url, session):
        try:
            async with session.get(url) as response:
                return url, response.status
        except Exception as e:
            return url, str(e)

    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = []
            for platform, tools in SOCIAL_MEDIA_OSINT_TOOLS.items():
                for tool in tools["Profile_search"]:
                    for username in username_variations:
                        try:
                            url = tool["link"].format(
                                username=quote(username),
                                first_name=quote(first_name),
                                surname=quote(surname)
                            )
                        except KeyError as e:
                            print(f"Error formatting URL for {tool['name']}: Missing key {e}")
                            continue  # Skip this tool
                        tasks.append(validate_url(url, session))
            results = await asyncio.gather(*tasks)
            for url, status in results:
                print(f"URL: {url}, Status: {status}")

    asyncio.run(main())





async def google_dorking(username_variations):
    """Perform Google Dorking and log results correctly in google_dork_results.log with animated word-by-word output"""
    temp_file = "/tmp/google_dork_results.log"
    open(temp_file, "w").close()  # Clear previous logs

    total_queries = len(username_variations) * len(dorking_methods)
    google_bar = tqdm(total=total_queries, desc="Google Dorking Progress", unit="queries", position=0, leave=True)

    async with aiohttp.ClientSession() as session:
        for username in username_variations:
            for method in dorking_methods:
                query = method["link"].format(username=username)
                search_url = f"https://www.google.com/search?q={quote(query)}"

                # Rotate user agent to avoid detection
                headers = {"User-Agent": random.choice(USER_AGENTS)}

                try:
                    async with session.get(search_url, headers=headers, timeout=10) as response:
                        status_code = response.status  # Get HTTP response status

                        # ✅ Print each part word by word for animated effect
                        await write_terminal_log(temp_file, "----------------", style="info")
                        await write_terminal_log(temp_file, f"🔍 **Google Dorking:** `{username}`", style="success")
                        await write_terminal_log(temp_file, f"📡 **Google Status Code:** `{status_code}`", style="warning")
                        await write_terminal_log(temp_file, f"🔗 **Dorking Link:** [Google Search]({search_url})", style="info")
                        await write_terminal_log(temp_file, f"💾 **Saved to:** `/tmp/google_dork_results.log`", style="success")
                        await write_terminal_log(temp_file, "----------------", style="info")

                        # ✅ Add a delay to prevent detection
                        await asyncio.sleep(random.uniform(3, 7))

                except Exception as e:
                    pass  # Ignore errors and continue

                google_bar.update(1)  # ✅ Update progress bar

    google_bar.close()
    await write_terminal_log(temp_file, "\n✅ **Google Dorking Complete!**", style="success")




    


def social_media_investigation(username_variations):
    for username in username_variations:
        print(f"Checking username: {username}")
        time.sleep(1)


def check_requirements():
    if os.system("which wmctrl") != 0:
        print("Installing wmctrl...")
        os.system("sudo apt-get install -y wmctrl")


def get_terminal_emulator():
    terminals = ["x-terminal-emulator", "gnome-terminal", "xfce4-terminal", "qterminal"]
    for term in terminals:
        if os.system(f"which {term} > /dev/null 2>&1") == 0:
            return term
    return None




# Function to generate URLs for a given username across all tools
def generate_username_urls(first_name, surname, tools_dict):
    username_urls = []
    unique_urls = set()
    username_variations = generate_username_variations(first_name, surname)

    for platform, categories in tools_dict.items():
        if isinstance(categories, list):
            categories = {"default": categories}  # Convert list to dictionary

        for category, tools in categories.items():
            for tool in tqdm(tools, desc=f"Generating URLs for {platform} - {category}", unit="tool"):
                for username in username_variations:
                    try:
                       
                        tool_link = tool["link"].replace("{first_name}", "{surname}")

                        tool_url = tool_link.format(
                            username=quote(username),
                            first_name=quote(first_name),
                            surname=quote(surname)
                        )

                    except KeyError as e:
                        print(f"Skipping {tool['name']} due to missing key: {e}")
                        continue  # Skip URLs with incorrect placeholders
                    
                    if tool_url not in unique_urls:
                        unique_urls.add(tool_url)
                        username_urls.append({
                            "platform": platform,
                            "category": category,
                            "tool_name": tool["name"],
                            "url": tool_url,
                            "tool_link": tool["link"],
                            "requires_api": tool.get("requires_api", False)
                        })

    return username_urls




# Function to save results to a JSON file
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)



# Function to create a structured directory for username results
def save_results(username, validated_links):
    # Replace spaces in the username with underscores for the directory name
    formatted_username = username.replace(" ", "_")
    base_dir = os.path.abspath(formatted_username)
    os.makedirs(base_dir, exist_ok=True)

    platform_data = {}
    for link in validated_links:
        platform = link["platform"]
        category = link["category"]

        if platform not in platform_data:
            platform_data[platform] = {}


        if category not in platform_data[platform]:
            platform_data[platform][category] = []

        platform_data[platform][category].append(link)

    # Create organized folders and save JSON files
    for platform, categories in platform_data.items():
        platform_dir = os.path.join(base_dir, platform)
        os.makedirs(platform_dir, exist_ok=True)

        for category, links in categories.items():
            category_file = os.path.join(platform_dir, f"{category}.json")
            save_to_json(links, category_file)

    # Print all files and directories
    print(f"\nDirectory structure for {formatted_username}:")
    for root, dirs, files in os.walk(base_dir):
        level = root.replace(base_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")



async def write_terminal_log(file_path, text, delay=0.1, style=None):
    """Writes log entries word by word to a unified log file for both OSINT processes."""
    styles = {
        'info': '\033[94m',  # Blue
        'success': '\033[92m',  # Green
        'warning': '\033[93m',  # Yellow
        'error': '\033[91m',  # Red
        'reset': '\033[0m'  # Reset
    }

    prefix = styles.get(style, '') if style else ''
    suffix = styles['reset'] if style else ''

    words = text.split()

    async with aiofiles.open(file_path, "a") as f:
        for word in words:
            await f.write(f"{prefix}{word}{suffix} ")
            await f.flush()
            await asyncio.sleep(delay)
        await f.write("\n")
        await f.flush()


async def open_results_terminal_async(username_variations, first_name, surname):
    temp_file = "/tmp/osint_results.log"
    
    total_queries = sum(len(tools["Profile_search"]) for tools in SOCIAL_MEDIA_OSINT_TOOLS.values()) * len(username_variations)
    social_media_bar = tqdm(total=total_queries, desc="Social Media OSINT Progress", unit="queries", position=1, leave=True)

    async with aiohttp.ClientSession() as session:
        for platform, tools in SOCIAL_MEDIA_OSINT_TOOLS.items():
            for tool in tools["Profile_search"]:
                tool_name = tool["name"]
                
                await write_terminal_log(temp_file, f"\n🔍 Tool: {tool_name}", style="info")
                await write_terminal_log(temp_file, "---------------------------------------", style="info")
                
                for username in username_variations:
                    try:
                        # Replace 'sirname' with 'surname' in URL template
                        tool_link = tool["link"].replace("{sirname}", "{surname}")
                        
                        url = tool_link.format(
                            username=quote(username),
                            first_name=quote(first_name),
                            surname=quote(surname)
                        )   

                        await write_terminal_log(temp_file, f"👤 Username: {username}", style="success")
                        await write_terminal_log(temp_file, f"🔗 URL: {url}", style="warning")
                        await write_terminal_log(temp_file, "---------------------------------------", style="info")

                        async with session.get(url, timeout=10) as response:
                            status = response.status
                            log_message = f"[{platform}] {tool_name} | Username: {username} | Status: {status}"
                            await write_terminal_log(temp_file, log_message)
                    
                    except KeyError as ke:
                        error_message = f"❌ URL Format Error: {tool_name}: Invalid template variable"
                        await write_terminal_log(temp_file, error_message, style="error")
                    except Exception as e:
                        error_message = f"❌ Website/Tool Error: {tool_name}: {str(e)}"
                        await write_terminal_log(temp_file, error_message, style="error")

                    social_media_bar.update(1)  

    social_media_bar.close()
    await write_terminal_log(temp_file, "\n✅ Social Media OSINT Complete!", style="success")


    

def set_window_title(window_id, label):
    """Rename terminal window using wmctrl."""
    try:
        subprocess.run(["wmctrl", "-i", "-r", window_id, "-T", label])
    except Exception as e:
        print(f"Error setting window title: {e}")


def set_window_position(window_title, position):
    """Position terminal window to the left or right side of the screen."""
    try:
        # Get the window ID based on title
        window_id = subprocess.check_output(f"wmctrl -l | grep '{window_title}' | awk '{{print $1}}'", shell=True).decode().strip()

        if not window_id:
            print(f"Window '{window_title}' not found.")
            return

        # Define positions: left (0,0) and right (half screen width, 0)
        screen_width = 1920  # Adjust based on your screen resolution
        screen_height = 540
        terminal_width = screen_width // 2
        terminal_height = screen_height - 100

        middle_width = terminal_width // 3  # Make it skinnier (1/3 of the full width)
        middle_x = (terminal_width - middle_width) // 2  # Center it horizontally

        middle_height = terminal_height // 3  # Make it shorter (1/3 of the full height)
        middle_y = (terminal_height - middle_height) // 2  # Center it vertically

        positions = {
            "left": f"0,0,0,{terminal_width},{terminal_height}",  # Top-left
            "right": f"0,{terminal_width},0,{terminal_width},{terminal_height}",  # Top-right
            "middle": f"{middle_y},{middle_x},{middle_y + middle_height},{middle_x + middle_width}"  # Fully centered skinny box
        }



        # Move window to the correct position
        subprocess.run(["wmctrl", "-i", "-r", window_id, "-e", positions[position]])
    except Exception as e:
        print(f"Error positioning window: {e}")


def get_terminal_app():
    """Get the correct terminal application."""
    # Check for GNOME Terminal first (most common)
    if os.system("which gnome-terminal > /dev/null 2>&1") == 0:
        return "gnome-terminal"
    # Fallback to x-terminal-emulator
    return "x-terminal-emulator"


async def open_terminal(cmd, title, position):
    """Open a new terminal and move it to the correct position."""
    term = get_terminal_app()

    # Open the terminal
    process = await asyncio.create_subprocess_exec(
        term, "--title", title, "--", "bash", "-c",
        f'{cmd}; read -p "Press Enter to close..."'
    )

    # Wait briefly for the terminal to appear
    time.sleep(1)

    # Move the terminal to the correct position
    set_window_position(title, position)

    return process


async def animated_print(text, delay=0.000005):
    """Print text character by character with animation."""
    for char in text:
        print(char, end='', flush=True)
        await asyncio.sleep(delay)
    print()


async def write_terminal_log(file_path, text, delay=0.05, style=None):
    """Write log entries word by word to a log file, ensuring animation appears only in the OSINT terminals."""
    styles = {
        'info': '\033[94m',  # Blue
        'success': '\033[92m',  # Green
        'warning': '\033[93m',  # Yellow
        'error': '\033[91m',  # Red
        'reset': '\033[0m'  # Reset
    }

    prefix = styles.get(style, '') if style else ''
    suffix = styles['reset'] if style else ''

    words = text.split()

    # Write word by word to the log file so the terminal running `tail -f` prints animated output
    async with aiofiles.open(file_path, "a") as f:
        for word in words:
            await f.write(f"{prefix}{word}{suffix} ")
            await f.flush()
            await asyncio.sleep(delay)
        await f.write("\n")  # Newline after sentence completion
        await f.flush()




async def print_usernames_animated(username_variations, temp_file):
    """Print username variations with letter-by-letter animation."""
    async with aiofiles.open(temp_file, "w") as f:
        # Header
        await write_terminal_log(temp_file, "\n🎯 Generated Username Variations", style="info")
        await write_terminal_log(temp_file, "=" * 50, style="info")
        
        # Print each username letter by letter
        for username in username_variations:
                await write_terminal_log(temp_file, f"\r👤 {username}", style="success")
                await asyncio.sleep(0.05)  # Delay between letters
                await write_terminal_log(temp_file, "", style="reset")  # New line after username
        
        # Footer
        await write_terminal_log(temp_file, "=" * 50, style="info")
        await write_terminal_log(temp_file, f"Total Variations: {len(username_variations)}", style="success")
        time.sleep(3)
        os.system("exit")  # Closes the terminal running the script





async def main():
    try:
        # Clear log files
        open("/tmp/osint_results.log", "w").close()
        open("/tmp/google_dork_results.log", "w").close()
        open("/tmp/username_variations.log", "w").close()

        # Print ASCII art
        ascii_art = Ascii()
        await animated_print(ascii_art)

        first_name = input("Enter first name: ")
        surname = input("Enter surname: ")
        username_variations = generate_username_variations(first_name, surname)

        # Open terminals
        try:
            # Username variations terminal
            username_term = await open_terminal(
                "tail -f /tmp/username_variations.log",
                "Username Variations",
                "middle"
            )
            
            # Print usernames with animation
            await print_usernames_animated(username_variations, "/tmp/username_variations.log")
            
            # Other terminals and tasks
            google_term = await open_terminal(
                "tail -f /tmp/google_dork_results.log",
                "Google Dorking",
                "left"
            )
            
            osint_term = await open_terminal(
                "tail -f /tmp/osint_results.log",
                "Social Media OSINT",
                "right"
            )
              
            # Run tasks
            google_task = google_dorking(username_variations)
            social_task = open_results_terminal_async(username_variations, first_name, surname)
            
            await asyncio.gather(google_task, social_task)
            
        except Exception as e:
            print(f"Error opening terminals: {e}")
            return
    except Exception as e:
        print(f"Error in main: {str(e)}")
        raise
            

if __name__ == "__main__":
    check_requirements()
    asyncio.run(main())

