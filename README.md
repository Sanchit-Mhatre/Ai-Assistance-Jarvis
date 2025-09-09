# Ai-Assistance-Jarvis

A voice-activated AI assistant that responds to voice commands to perform various tasks such as opening websites, playing music, and fetching news.

Features
Voice Activation: Responds to the wake phrase "wake up"

Web Navigation: Opens Google, YouTube, Facebook, and LinkedIn

Music Playback: Plays specific songs from YouTube based on voice commands

News Updates: Fetches and reads the latest news headlines

Extensible Architecture: Easy to add new commands and functionality

Project Structure
text
├── chat_gptCode.py      # Basic version with limited commands
├── client.py            # OpenAI API client setup (requires configuration)
├── main.py              # Main application with extended functionality
├── musicLibrary.py      # Music database with YouTube links
├── Son_bot.py           # Enhanced version with YouTube search capability
└── README.md            # This file
Installation
Clone this repository:

bash
git clone <your-repo-url>
cd jarvis-ai-assistant
Install required dependencies:

bash
pip install speechrecognition webbrowser pyttsx3 requests
For enhanced speech recognition (optional):

bash
pip install pocketsphinx
Configuration
News API (optional):

Get a free API key from NewsAPI.org

Replace the newsapi variable in main.py with your key

OpenAI Integration (optional):

Set up your API key in client.py

Uncomment and configure the OpenAI client for advanced AI responses

Usage
Run the main application:

bash
python main.py
Wait for the "Initializing Jarvis..." message

Say the wake phrase: "wake up"

After the confirmation, give one of these commands:

"Open Google"

"Open YouTube"

"Open Facebook"

"Open LinkedIn"

"Play [song name]" (e.g., "Play lemonade")

"News" (to get the latest headlines)

Customization
Adding New Music
Edit musicLibrary.py to add new songs:

python
music = {
    "song_name": "youtube_url",
    # ... more songs
}
Adding New Commands
Extend the processCommand() function in main.py:

python
elif "your command" in c.lower():
    # Your action here
Troubleshooting
Ensure your microphone is properly connected and configured

Check internet connection for web features and speech recognition

Adjust microphone sensitivity if having trouble with voice detection

Dependencies
speechrecognition

pyttsx3

webbrowser

requests

pocketsphinx (optional, for offline speech recognition)
