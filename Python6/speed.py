import speedtest


class SpeedTest:

    def run(self):
        st = speedtest.Speedtest()

        print("Download:", round(st.download() / 1_000_000, 2), "Mbps")
        print("Upload:", round(st.upload() / 1_000_000, 2), "Mbps")