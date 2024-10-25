# Voice-assistant
A voice assistant python AI which recognizes voice and does various commands like search on Wikipedia and reminders.

## Features

- Voice recognition
- Wikipedia search
- Open websites (YouTube, Google, Stack Overflow)
- Play music
- Tell the current time
- Open VS Code
- Send emails
- Set reminders

## Installation

To make this work, first run this command through your terminal (commands also mentioned in the py file):

1. `pip install pyttsx3 pyaudio datetime wikipedia os plyer smtplib speechRecognition`
2. `python .\assist.py`

## Configuration

Create a `config.py` file in the same directory as `assist.py` with the following content:

```python
# Configuration file for managing constants and settings

# Email credentials
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"

# File paths
MUSIC_DIR = "path_to_music_directory"
CODE_PATH = "path_to_code_editor"

# Other settings
REMINDER_INTERVAL = 10  # Default reminder interval in minutes
```

## Running Unit Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover -s tests
```

## Usage

1. Run the `assist.py` script.
2. The assistant will greet you based on the time of the day.
3. You can give voice commands to the assistant. Some examples of commands are:
   - "search Wikipedia for Python programming"
   - "open YouTube"
   - "open Google"
   - "open Stack Overflow"
   - "play music"
   - "what is the time"
   - "open code"
   - "send email"
   - "set a reminder"

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
