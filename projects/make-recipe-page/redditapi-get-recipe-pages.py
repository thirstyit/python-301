# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

from pathlib import Path
import praw
from slugify import slugify
from secrets import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)

recipes = [post for post in reddit.subreddit("recipes").top(limit=100)]

rloc = Path().cwd().joinpath("recipage/recipes")
rloc.mkdir(exist_ok=True)

recipe_titles = list()

for i, r in enumerate(recipes):
    filename = f"{i}-{slugify(r.title)[:20].strip('-')}.html"
    recipe_titles.append((r.title, Path("recipes").joinpath(filename)))
    #print(r.selftext)
    c = r.comments[0]
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../style.css">
    <title>Recipe #{i}</title>
</head>
<body> 
    <section class="section">
        <div class="container">
        <div class="content is-normal">
            <h1 class="title is-2">{r.title}</h1>
            <p class="subtitle is-3 author">by {r.author}</p>
            {c.body_html}
        </div>
        </div>
    </section>
</body>
</html>"""
    with open(rloc.joinpath(filename), "w") as fout:
        fout.write(html)


with open(Path().cwd().joinpath("recipage").joinpath("index.html"), "w") as fout:
    links_html = "\n".join([f'<li><a href="{link[1]}">{link[0]}</a></li>' for link in recipe_titles])
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>🍜 Recipes</title>
</head>
<body>
  <section class="hero is-info">
    <div class="hero-body">
        <h1 class="title is-1">
        Recipe Collection
        </h1>
        <p class="subtitle is-2">
        This page contains some recipes gathered from Reddit posts
        </p>
    </div>
  </section>
  <section class="section">
    <div class="container">
    <div class="content is-normal">
    <ul>
    {links_html}
    </ul>
    </div>
    </div>
    </section>
</body>
</html>"""
    fout.write(html)
