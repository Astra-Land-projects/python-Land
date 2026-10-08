from gtts import gTTS
from moviepy.editor import VideoFileClip

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='fa')
    tts.save(filename)
    print(f"فایل صوتی '{filename}' ایجاد شد.")

def video_to_audio(video_filename, audio_filename):
    video = VideoFileClip(video_filename)
    audio = video.audio
    audio.write_audiofile(audio_filename)
    print(f"فایل صوتی '{audio_filename}' از ویدیو استخراج شد.")

def main():
    while True:
        choice = input("لطفاً انتخاب کنید:")
                       
        if choice == '1':
            text = input("متن مورد نظر خود را وارد کنید: ")
            filename = input("نام فایل خروجی (با پسوند .mp3): ")
            text_to_speech(text, filename)

        elif choice == '2':
            video_filename = input("نام فایل ویدیویی (با پسوند .mp4): ")
            audio_filename = input("نام فایل خروجی صوتی (با پسوند .mp3): ")
            video_to_audio(video_filename, audio_filename)

        elif choice == '3':
            print("خروج...")
            break
       
        else:
            print("گزینه نامعتبر است، لطفاً دوباره تلاش کنید.")

Main()
#خراب و کتابخانه نصب نشده است نت می خواهد