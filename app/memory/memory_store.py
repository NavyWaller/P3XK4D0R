import json
import os
from datetime import datetime

MEMORY_FILE = "memory.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(data):

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_memory(topic, summary, sources):

    memory = load_memory()

    memory.append({
        "timestamp": datetime.utcnow().isoformat(),
        "topic": topic,
        "summary": summary,
        "sources": sources
    })

    save_memory(memory)


def search_memory(keyword):

    memory = load_memory()

    results = []

    for item in memory:

        if keyword.lower() in item["topic"].lower():
            results.append(item)

    return results