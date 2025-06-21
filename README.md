# 🧠 Mental Health Check-In Agent

An intelligent Telegram bot that detects your mood from your message, stores it, and replies with empathetic responses. It uses a custom Flask API integrated via n8n workflows.

---

## 🔧 Features

- Mood detection using custom keywords via Flask API
- Telegram bot interaction via n8n
- Stores mood logs in JSON
- Fully automated response system
- Localtunnel support for public API access

---

## 📁 Project Structure

```
mental-health-agent/
├── mood_api.py                 # Flask API for mood detection
├── mood_utils.py              # Mood detection logic
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview
├── logs/
│   └── mood_logs.json         # Mood log storage
└── workflows/
    └── n8n_mood_workflow.json # n8n workflow export
```

---

## 🚀 Getting Started

### 1. Clone and Setup
```bash
git clone https://github.com/your-username/mental-health-agent.git
cd mental-health-agent
python -m venv telegram-env
telegram-env\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 2. Run Flask API
```bash
python mood_api.py
```

### 3. Expose API via LocalTunnel
```bash
npm install -g localtunnel
lt --port 5000
```
Update the HTTP Request node in n8n with your public URL like `https://your-url.loca.lt/detect`

---

## 🤖 n8n Workflow Setup

1. Import `workflows/n8n_mood_workflow.json` in n8n
2. Connect Telegram Trigger to HTTP Request → Telegram Send
3. Ensure correct credentials and test with Telegram bot

---

## 📊 Logs
- All mood responses are saved in `logs/mood_logs.json`

---

## 💡 Use Cases
- Self-awareness and reflection
- Daily emotional journaling
- AI-based personal well-being assistant

---

## 🌟 Advantages
- Personalized responses
- Data privacy (local logging)
- Easy to modify or expand

---

## 🔮 Future Scope
- Mood trend charts and analytics
- Sentiment-based suggestions
- Voice input support
- Integration with daily planners or Google Calendar

---

## 📜 License
MIT License