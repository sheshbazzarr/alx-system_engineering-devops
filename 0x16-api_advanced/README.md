# API Advanced Project

## Overview

This project focuses on enhancing your skills in working with APIs, particularly the Reddit API. The tasks in this project will help you get comfortable with making API calls, handling JSON data, and using recursion in Python. Understanding these concepts is valuable for technical interviews and can be applied to real-world scenarios.

## Learning Objectives

By the end of this project, you will be able to:

- Read API documentation to identify relevant endpoints.
- Use an API with pagination.
- Parse JSON results from an API.
- Make recursive API calls.
- Sort a dictionary by value.

## Requirements

- **Python Version:** Python 3.4.3 or higher.
- **Operating System:** Ubuntu 20.04 LTS.
- **Editor:** vi, vim, emacs.
- **Code Style:** PEP 8.
- **Modules:** Use the `Requests` module for HTTP requests.
- **File Requirements:**
  - All Python files must end with a new line.
  - The first line of each Python file should be `#!/usr/bin/python3`.
  - Libraries in Python files should be imported in alphabetical order.
  - All files must be executable.
  - Documentation must be provided for each module.

## Tasks

### 0. How many subs?

**Description:**  
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If the subreddit is invalid, the function should return 0.

- **Prototype:** `def number_of_subscribers(subreddit)`
- **Note:** Avoid following redirects for invalid subreddits.

**Example Usage:**

```python
number_of_subscribers('programming')  # Expected output: 756024
number_of_subscribers('this_is_a_fake_subreddit')  # Expected output: 0

1. Top Ten
Description:
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit. If the subreddit is invalid, print None.

Prototype: def top_ten(subreddit)
Note: Avoid following redirects for invalid subreddits.

Example Usage:
```top_ten('programming')
# Expected output:
# Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
# How a 64k intro is made
# HTTPS on Stack Overflow: The End of a Long Road
# ...

top_ten('this_is_a_fake_subreddit')  # Expected output: None
2. Recurse it!
Description:
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found, return None.

Prototype: def recurse(subreddit, hot_list=[])
Note: Avoid using loops; the function must be recursive.  ```

```recurse('programming')  # Expected output: A list of titles
recurse('this_is_a_fake_subreddit')  # Expected output: None```

### Usage Instructions
1.clone the repository
2.navigatie to the project directory
3.run the scripts with python 
License
This project is licensed under the MIT License - see the LICENSE file for details
``` 
---

This `README.md` file is now well-structured and includes all necessary sections like an introduction, learning objectives, requirements, tasks, usage instructions, and licensing information. The example usage for each task is also provided to guide users in running the scripts. Replace placeholders like `your-username` with your actual GitHub username before using the README.

