def process_command(text):
    text=text.lower()
    if text=="exit":
        return "exit"
    elif "hello" in text or "hi" in text:
        return "greeting"
    elif "good morning" in text:
        return "morning"
    elif "good afternoon" in text:
        return "afternoon"
    elif "good evening" in text:
        return "evening"
    elif "youtube search" in text:
        return "youtube_search"
    elif "play music" in text or text.startswith("play"):
        return "play_music"
    elif "volume up" in text:
        return "volume_up"
    elif "volume down" in text:
        return "volume_down"
    elif "unmute" in text:
        return "unmute"
    elif "mute" in text:
        return "mute"
    elif "who is" in text:
        return "wikipedia"
    elif "what is" in text:
        return "wikipedia"
    elif "vs code" in text or "visual studio code" in text:
        return "vs_code"
    elif "chrome" in text:
        return "chrome"
    elif "file explorer" in text:
        return "explorer"
    elif "search" in text:
        return "google_search"

    elif "youtube" in text:
        return "youtube"
    elif "google" in text:
        return "google"
    elif "gmail" in text:
        return "gmail"
    elif "notepad" in text:
        return "notepad"
    elif "calculator" in text:
        return "calculator"
    elif "time" in text:
        return "time"
    elif "date" in text:
        return "date"
    else:
        return "Unknown"
#print(process_command("Please open youtube"))
#print(process_command("please open google"))
#print(process_command("can you open calculator"))
#print(process_command("what is time "))
#print(process_command("what is  todays date"))
#print(process_command("hello"))