from pytube import YouTube

def download_video(url, path='.'):
    try:
       yt = YouTube(url)
       stream = yt.streams.get_highest_resolution()
       stream.download(path)
       print(f"ویدیو '{yt.title}' با موفقیت دانلود شد.")
      
    except Exception as e:
       print(f"خطا در دانلود: {e}")

if __name__ == "__main__":
   video_url = input("لطفاً لینک ویدیوی یوتیوب را وارد کنید: ")
   download_video(video_url)
   #خراب کتابخانه نصب نشده نیاز به نت