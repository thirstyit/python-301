from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

id = 'b_AZri7Zi6U'

transcript = YouTubeTranscriptApi.get_transcript(id)

formatter = JSONFormatter()
json_formatted = formatter.format_transcript(transcript)

result = {'data': json_formatted}

print(result)