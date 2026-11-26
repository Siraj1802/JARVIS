
import subprocess


class VoiceOutput:

    def __init__(self, voice="Daniel", rate=190):
        if not isinstance(rate, (int, float)) or rate <= 0:
            raise ValueError("Speaking rate must be a positive number.")

        self.voice = voice
        self.rate = rate

    def speak(self, text):

        if not text or not text.strip():
            return

        try:
            subprocess.run(
                [
                    "say",
                    "-v", self.voice,
                    "-r", str(self.rate),
                    text
                ],
                check=True
            )

        except FileNotFoundError:
            print("Error: macOS speech engine not found.")

        except subprocess.CalledProcessError:
            print("Error: Unable to generate speech.")
