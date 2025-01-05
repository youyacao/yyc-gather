import yt_dlp

# 下载视频的函数
def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': output_path
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# 示例用法
video_url = 'https://www.youtube.com/watch?v=WBZVM_YGbLU'
output_file = 'gtagame.mp4'
download_video(video_url, output_file)
