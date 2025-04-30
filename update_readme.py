import random
from datetime import datetime

# Load quotes
with open("quotes.txt", "r") as f:
    quotes = [line.strip() for line in f if line.strip()]

# Select one at random
quote = random.choice(quotes)
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# Update README
with open("README.md", "w") as f:
    f.write(f"> _\"{quote}\"_\n> _Updated: {timestamp}_\n")
