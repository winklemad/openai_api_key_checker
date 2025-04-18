import requests
import threading
import signal
import sys
from queue import Queue

INPUT_FILE = "openai api keys.txt"
OUTPUT_FILE = "valid_keys.txt"
NUM_THREADS = 20

lock = threading.Lock()
queue = Queue()
stop_event = threading.Event()

def check_key(api_key):
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        # Verbose: Checking key...
        print(f"🔍 Checking key: {api_key[:10]}...")

        # Step 1: Check model access (validity)
        model_resp = requests.get("https://api.openai.com/v1/models", headers=headers, timeout=10)
        if model_resp.status_code != 200:
            print(f"❌ Invalid key or no model access: {api_key[:10]}...")
            return

        # Step 2: Check credit info
        billing_url = "https://api.openai.com/dashboard/billing/credit_grants"
        billing_resp = requests.get(billing_url, headers=headers, timeout=10)
        if billing_resp.status_code != 200:
            print(f"⚠️  Could not fetch billing info: {api_key[:10]}...")
            return

        data = billing_resp.json()
        available = data.get("total_available", 0)

        if available > 0:
            with lock:
                with open(OUTPUT_FILE, "a") as f:
                    f.write(f"{api_key}\n")
            print(f"✅ Valid key with credit (${available:.2f}): {api_key[:10]}...")
        else:
            print(f"🚫 Valid but no credit: {api_key[:10]}...")

    except Exception as e:
        print(f"⚠️ Error for {api_key[:10]}...: {e}")

def worker():
    while not queue.empty() and not stop_event.is_set():
        api_key = queue.get()
        check_key(api_key)
        queue.task_done()
        remaining = queue.qsize()
        print(f"⏳ Remaining: {remaining} keys")

def signal_handler(sig, frame):
    print("\n🛑 Received Ctrl+C! Stopping...")
    stop_event.set()
    while not queue.empty():
        queue.get_nowait()
        queue.task_done()

signal.signal(signal.SIGINT, signal_handler)

def main():
    print("📥 Reading API keys...")
    with open(INPUT_FILE, "r") as f:
        keys = [line.strip() for line in f if line.strip()]

    print(f"🔢 Loaded {len(keys)} keys.")
    
    for key in keys:
        queue.put(key)

    threads = []
    for _ in range(min(NUM_THREADS, len(keys))):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    try:
        queue.join()
    except KeyboardInterrupt:
        print("🛑 Interrupted! Cleaning up...")

    for t in threads:
        t.join()

    print("\n✅ Finished checking all keys.")

if __name__ == "__main__":
    main()
