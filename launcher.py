import os
import sys
import threading
import time
import webbrowser
from pathlib import Path

import streamlit.web.cli as stcli


def get_app_path():
    """Find app.py in development or in the PyInstaller bundle."""
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS) / "app.py"

    return Path(__file__).resolve().parent / "app.py"


def open_browser():
    """Open the local application after startup."""
    time.sleep(5)
    webbrowser.open("http://localhost:8501")


def main():
    app_path = get_app_path()

    if not app_path.is_file():
        print(f"ERROR: app.py not found: {app_path}")
        input("Press Enter to exit...")
        return

    # Configure Streamlit for a packaged local application.
    os.environ["STREAMLIT_GLOBAL_DEVELOPMENT_MODE"] = "false"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    os.environ["STREAMLIT_SERVER_PORT"] = "8501"
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"

    threading.Thread(target=open_browser, daemon=True).start()

    sys.argv = [
        "streamlit",
        "run",
        str(app_path),
        "--global.developmentMode=false",
        "--server.headless=true",
        "--server.port=8501",
        "--browser.gatherUsageStats=false",
    ]

    sys.exit(stcli.main())


if __name__ == "__main__":
    main()