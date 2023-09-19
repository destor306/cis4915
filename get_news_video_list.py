import time
import re
start_time = time.time()

# Read the data from the .txt file
with open('TC_VC_VIDO_INFO_20211126174408_1.txt', 'r', encoding='utf-8') as file:
    data = file.read()
lines = data.split('\n')

filtered_lines = [line for line in lines if '뉴스' in line]
filtered_lines = "".join(filtered_lines)

# Use regular expressions to extract YouTube video IDs
video_ids = re.findall(
    r'www\.youtube\.com/watch\?v=([A-Za-z0-9_-]+)', filtered_lines)

with open("video_list.txt", "w") as file:
    for i, video_id in enumerate(video_ids):
        file.write(f"{video_id}\n")

