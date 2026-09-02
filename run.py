#!/usr/bin/env python3
"""
BhashaSetu Launcher Script
Starts the FastAPI web server on http://localhost:8000
"""

import sys
import os
import uvicorn

# Ensure project root is in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def main():
    print("=" * 60)
    print(">> BhashaSetu - Hindi to Tribal & Regional Languages")
    print("=" * 60)
    print("[+] Serving web app at: http://127.0.0.1:8000")
    print("[+] API documentation: http://127.0.0.1:8000/docs")
    print("[+] Press Ctrl+C to stop the server.")
    print("=" * 60)

    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
