from xlwt import Workbook
from youtube_transcript_api import YouTubeTranscriptApi

# Create a new Excel workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')



def get_transcript(videoid):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(videoid, languages=['ko'])
        text = ""
        for transcript in transcript_list:
            text += transcript['text'] + ' '
        return text
    except Exception as e:
        return videoid, f"Error: {str(e)}"


# Initialize a row counter for writing to the Excel sheet
row = 0

# Read video IDs from a file
with open("video_list.txt", 'r') as file:
    video_list = file.readlines()

for i, video in enumerate(video_list[:1]):
    result = get_transcript(video.strip())
    print(f"{i} out of {len(video_list)} is done")
    results = [get_transcript(video.strip()) for video in video_list]

print(results)        
# Save the Excel workbook to a file
wb.save('transcripts.xls')
