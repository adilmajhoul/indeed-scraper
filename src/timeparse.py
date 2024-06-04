import dateparser
from datetime import datetime

# List of relative time strings
time_strings = [
    "just now",
    "12 seconds ago",
    "3 minutes ago",
    "2 hours ago",
    "24 days ago",
    "6 months ago",
    "2 years ago",
    "in 12 seconds",
    "in 3 minutes",
    "in 2 hours",
    "in 24 days",
    "in 6 months",
    "in 2 years"
]

# Current time
current_time = datetime.now()

# Parse the relative time strings
parsed_times = [dateparser.parse(time_str, settings={'RELATIVE_BASE': current_time}) for time_str in time_strings]

# Display the results
for original, parsed in zip(time_strings, parsed_times):
    print(f"{original} -> {parsed}")
