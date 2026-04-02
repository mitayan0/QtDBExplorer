# QtDBExplorer

Modular database exploration tool built with PySide6.

## 🚀 Quick Start

```powershell
# Activate venv and run
.\.venv\Scripts\activate
python main.py
```

## 🛠 Features

- **Security:** AES-256 (Fernet) encryption for credentials, anchored in Windows Credential Manager via `keyring`.
- **Dynamic UI:** Loads `.ui` files at runtime; no compilation needed.
- **Architected:** Separated DAOs, Workers, and Adapters for high scalability.
- **Auto-Bootstrap:** Generates local database and executes migrations on first launch.

## 📂 Project Structure

```text
QtDBExplorer/
├── main.py                   # Entry point
├── requirements.txt          # Dependencies
├── app/
│   ├── appdb/                # App's internal SQLite (Connection/History storage)
│   │   ├── dao/              # Data Access Objects
│   │   ├── migrations/       # SQL schema scripts
│   │   └── setup.py          # DB initialization logic
│   ├── core/                 # App state & signals
│   ├── database/             # Target DB logic
│   │   ├── adapters/         # DB-specific drivers (Postgres, Oracle, etc.)
│   │   └── models/           # Data classes reflecting schemas
│   ├── dialogs/              # UI Window logic
│   ├── ui/                   # Raw Qt Designer .ui files
│   ├── utils/                # Crypto, UI Loaders, Validators
│   ├── widgets/              # Component-level widget logic
│   ├── windows/              # Main Window logic
│   └── workers/              # Async ThreadPool workers
├── data/                     # Local app persistence (Git ignored)
└── resources/                # Icons and Stylesheets
```

## 🛡 Security
Passwords in `appdata.db` are encrypted. To decrypt, the app requires the unique key stored in the machine's OS Keystore. Database files are not portable across users without re-entering credentials.
