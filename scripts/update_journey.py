import os
import re
import html
import requests
from bs4 import BeautifulSoup

CF_HANDLE = "_vishalgupta_"

# Standard headers to prevent Codeforces from blocking request calls
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_accepted_submissions():
    url = f"https://codeforces.com/api/user.status?handle={CF_HANDLE}&from=1&count=1000"
    try:
        response = requests.get(url, headers=HEADERS).json()
        if response.get("status") != "OK":
            return []
    except Exception:
        return []

    accepted = []
    for sub in response.get("result", []):
        if sub.get("verdict") == "OK" and "Java" in sub.get("programmingLanguage", ""):
            accepted.append(sub)

    return list(reversed(accepted))

def fetch_solution_code(contest_id, submission_id):
    """Scrapes the actual submitted Java source code from Codeforces submission page."""
    url = f"https://codeforces.com/contest/{contest_id}/submission/{submission_id}"
    try:
        res = requests.get(url, headers=HEADERS)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")
            code_element = soup.find("pre", id="program-source-text")
            if code_element:
                return html.unescape(code_element.text)
    except Exception as e:
        print(f"Failed to fetch code for submission {submission_id}: {e}")
    return None

def get_rating_folder(rating):
    if rating is None or not isinstance(rating, int):
        return "solutions/rating-unrated"
    lower = (rating // 200) * 200
    upper = lower + 200
    return f"solutions/rating-{lower:04d}-{upper:04d}"

def update_readme_and_files():
    submissions = fetch_accepted_submissions()
    if not submissions:
        print("No Java accepted submissions found.")
        return

    readme_path = "README.md"
    
    # Initialize README.md with standard centered table header if missing/empty
    if not os.path.exists(readme_path) or os.stat(readme_path).st_size == 0:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write("# Codeforces Journey\n\n| # | Problem Name | Rating | Solution Link |\n|:---:|:---|:---:|:---:|\n")

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    existing_ids = set(re.findall(r"problem/(\d+/[A-Z\d]+)", content))
    serial_matches = re.findall(r"\|\s*(\d{3})\s*\|", content)
    serial_counter = int(serial_matches[-1]) if serial_matches else 0

    new_rows = []

    for sub in submissions:
        sub_id = sub.get("id")
        problem = sub["problem"]
        contest_id = problem.get("contestId")
        index = problem.get("index")
        name = problem.get("name")
        rating = problem.get("rating", "Unrated")

        if not contest_id or not index:
            continue

        problem_key = f"{contest_id}/{index}"
        if problem_key in existing_ids:
            continue

        existing_ids.add(problem_key)
        serial_counter += 1
        serial_str = f"{serial_counter:03d}"

        folder = get_rating_folder(rating)
        os.makedirs(folder, exist_ok=True)

        clean_name = re.sub(r"[^a-zA-Z0-9]", "", name)
        class_name = f"Problem{contest_id}{index}_{clean_name}"
        file_path = os.path.join(folder, f"{class_name}.java")

        # Scrape source code from Codeforces
        code = fetch_solution_code(contest_id, sub_id)
        
        # Write code to Java file
        with open(file_path, "w", encoding="utf-8") as jf:
            comment_header = f"/*\n * Serial: #{serial_str}\n * Problem: {name} ({contest_id}{index})\n * Rating: {rating}\n * Link: https://codeforces.com/problemset/problem/{contest_id}/{index}\n */\n\n"
            if code:
                jf.write(comment_header + code)
            else:
                jf.write(f"{comment_header}public class {class_name} {{\n    public static void main(String[] args) {{\n        // Solution code could not be retrieved\n    }}\n}}\n")

        # Format markdown links (convert Windows backslashes to forward slashes for URLs)
        web_file_path = file_path.replace("\\", "/")
        problem_link = f"[{contest_id}{index} - {name}](https://codeforces.com/problemset/problem/{contest_id}/{index})"
        solution_link = f"[Java Solution]({web_file_path})"
        
        # Append formatted markdown table row
        new_rows.append(f"| {serial_str} | {problem_link} | {rating} | {solution_link} |")

    if new_rows:
        with open(readme_path, "a", encoding="utf-8") as f:
            for row in new_rows:
                f.write(row + "\n")
        print(f"Successfully updated {len(new_rows)} solutions with source code and formatted table rows.")

if __name__ == "__main__":
    update_readme_and_files()
