#!/usr/bin/env python3
"""
Resume Bullet Rewriter (offline)
Usage:
  python main.py --input "Managed a small team of 5 people"
"""
import argparse, requests, os, sys

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = "llama3.2:4b"
TIMEOUT = 60

def run_llama(prompt):
    r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json().get("response","").strip()

def build_prompt(bullet):
    return (
        "Rewrite this resume bullet into 3 concise, quantified, impact-focused variants. "
        "Keep each variant short (one line).\n\n"
        f"Original: {bullet}"
    )

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True)
    args = p.parse_args()
    print(run_llama(build_prompt(args.input)))

if __name__ == "__main__":
    main()
