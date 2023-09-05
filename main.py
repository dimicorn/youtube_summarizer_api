from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeSummarizerAPI(object):
    def get_script(link2video: str)->str:
        video_id = link2video.split("v=")[1].split("&")[0]
        script_json = YouTubeTranscriptApi.get_transcript(video_id)
        script_text = ""
        for i in script_json:
            script_text += i["text"] + " "
        return script_text