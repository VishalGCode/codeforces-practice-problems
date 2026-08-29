import os
import re
import requests

# -------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------
CF_HANDLE = "_vishalgupta_"  # Updated Codeforces Handle


def fetch_accepted_submissions():
    """Fetches user submissions from Codeforces API and filters for Java OK verdicts."""
    url = f"https://codeforces.com/api/user.status?handle={CF_HANDLE}&from=1&count=1000"
    try:
        response = requests.get(url).json()
        if response.get("status") != "OK":
            print(f"Error fetching data from API: {response.get('comment')}")
            return []
    except Exception as e:
        print(f"Request failed: {e}")
        return []

    accepted = []
    for sub in response.get("result", []):
        # Check for Accepted verdict and Java programming language
        if sub.get("verdict") == "OK" and "Java" in sub.get(
            "programmingLanguage", ""
        ):
            accepted.append(sub)

    # Reverse to process oldest submissions first to maintain sequential order
    return list(reversed(accepted))


def get_rating_folder(rating):
    """Determines the rating directory based on problem rating."""
    if rating is None or not isinstance(rating, int):
        return "solutions/rating-unrated"
    lower = (rating // 200) * 200
    upper = lower + 200
    return f"solutions/rating-{lower:04d}-{upper:04d}"


def update_readme_and_files():
    """Reads submissions, creates Java solution files, and updates README.md."""
    submissions = fetch_accepted_submissions()
    if not submissions:
        print("No new Java accepted submissions found.")
        return

    readme_path = "README.md"

    # Initialize README.md with header if missing or empty
    if not os.path.exists(readme_path) or os.stat(readme_path).st_size == 0:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(
                "# Codeforces Journey\n\n| # | Problem Name | Rating | Solution Link |\n|---|---|---|---|\n"
            )

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Track logged problems to prevent duplicates
    existing_ids = set(re.findall(r"problem/(\d+/[A-Z\d]+)", content))

    # Find the current highest serial number
    serial_matches = re.findall(r"\|\s*(\d{3})\s*\|", content)
    serial_counter = int(serial_matches[-1]) if serial_matches else 0

    new_rows = []

    for sub in submissions:
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

        # Get target directory based on rating
        folder = get_rating_folder(rating)
        os.makedirs(folder, exist_ok=True)

        # Sanitize class name for Java compliance
        clean_name = re.sub(r"[^a-zA-Z0-9]", "", name)
        class_name = f"Problem{contest_id}{index}_{clean_name}"
        file_name = f"{class_name}.java"
        file_path = os.path.join(folder, file_name)

        # Create boilerplate Java file if missing
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as jf:
                jf.write(
                    f"/*\n"
                    f" * Serial: #{serial_str}\n"
                    f" * Problem: {name} ({contest_id}{index})\n"
                    f" * Rating: {rating}\n"
                    f" * Link: https://codeforces.com/problemset/problem/{contest_id}/{index}\n"
                    f" */\n\n"
                    f"public class {class_name} {{\n"
                    f"    public static void main(String[] args) {{\n"
                    f"        // Solution for {name}\n"
                    f"    }}\n"
                    f"}}\n"
                )

        # Prepare entry for README table
        problem_link = f"[{contest_id}{index} - {name}](https://codeforces.com/problemset/problem/{contest_id}/{index})"
        solution_link = f"[Java Solution]({file_path})"
        row = f"| {serial_str} | {problem_link} | {rating} | {solution_link} |"
        new_rows.append(row)

    # Append new rows to README.md
    if new_rows:
        with open(readme_path, "a", encoding="utf-8") as f:
            for row in new_rows:
                f.write(row + "\n")
        print(f"Successfully added {len(new_rows)} new solutions.")
    else:
        print("All Java submissions are already logged.")


if __name__ == "__main__":
    update_readme_and_files()