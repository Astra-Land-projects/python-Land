import sounddevice as sd
from scipy.io.wavfile import write


class VoiceRecorder:

    def record(self, seconds):
        fs = 44100

        print("Recording...")

        audio = sd.rec(
            int(seconds * fs),
            samplerate=fs,
            channels=2
        )

        sd.wait()

        write("record.wav", fs, audio)

        print("Saved.")