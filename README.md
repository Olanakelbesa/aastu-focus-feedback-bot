# AASTU FOCUS Feedback Bot

A Telegram bot for collecting anonymous feedback.

## Deployment Instructions

### Using PythonAnywhere (Free Tier)

1. Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com/)
2. Go to the Dashboard and open a Bash console
3. Clone this repository or upload the files:
   ```bash
   git clone <your-repo-url>
   # OR upload the files manually through the Files tab
   ```
4. Create a virtual environment and install dependencies:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 aastu-bot
   pip install -r requirements.txt
   ```
5. Go to the "Tasks" tab and set up a new scheduled task:
   - Command: `cd ~/aastufocusfeedbackbot && python aastufocusfeedbackbot.py`
   - Time: Set it to run every day at a specific time

### Alternative: Using a VPS (DigitalOcean, AWS, etc.)

1. Set up a VPS with Ubuntu
2. Install Python and required packages:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv
   ```
3. Clone the repository and set up the environment:
   ```bash
   git clone <your-repo-url>
   cd aastufocusfeedbackbot
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Use systemd to run the bot as a service:

   ```bash
   sudo nano /etc/systemd/system/aastu-bot.service
   ```

   Add the following content:

   ```
   [Unit]
   Description=AASTU FOCUS Feedback Bot
   After=network.target

   [Service]
   User=<your-username>
   WorkingDirectory=/path/to/aastufocusfeedbackbot
   Environment="PATH=/path/to/aastufocusfeedbackbot/venv/bin"
   ExecStart=/path/to/aastufocusfeedbackbot/venv/bin/python aastufocusfeedbackbot.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

5. Enable and start the service:
   ```bash
   sudo systemctl enable aastu-bot
   sudo systemctl start aastu-bot
   ```

## Security Notes

1. Never commit your BOT_TOKEN to version control
2. Consider using environment variables for sensitive data
3. Regularly update your dependencies

## Monitoring

- Check the bot's status using:
  ```bash
  sudo systemctl status aastu-bot  # For VPS deployment
  ```
- View logs:
  ```bash
  sudo journalctl -u aastu-bot -f  # For VPS deployment
  ```
# AASTU_FOCUS_feedback_bot
# aastu-focus-feedback
# aastu-focus-feedback-bot
# aastu-focus-feedback-bot
