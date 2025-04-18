# 🔐 OpenAI API Key Validator (with Credit Checker)

This Python script checks a list of OpenAI API keys to see:
- Whether each key is **valid**
- Whether it has **remaining credits**

It uses multithreading for faster performance, supports verbose output, and handles `Ctrl+C` interrupts gracefully.

---

## 🚀 Features

- ✅ Validates OpenAI API keys
- 💰 Checks for remaining credit balance
- ⚡ Fast execution with threading
- ⏳ Verbose status for each key
- 🛑 Graceful shutdown on `Ctrl+C`
- 🧠 Memory-efficient and safe to run on large files

---

## 📁 File Structure

```
📜 check_openai_keys.py       # Main script
📄 openai api keys.txt        # Input file with API keys (one per line)
📄 valid_keys.txt             # Output file containing only valid keys with credit
```

---

## 📦 Requirements

- Python 3.6+
- `requests` module

Install dependencies:

```bash
pip install requests
```

---

## 🧪 Usage

1. Add your OpenAI keys (one per line) to a file named:

```
openai api keys.txt
```

2. Run the script:

```bash
python keys.py
```

3. All valid keys with positive credit will be saved to:

```
valid_keys.txt
```

---

## ⚠️ Disclaimer

> This tool is created for **testing and educational purposes only**.  
> Use it at your **own risk**. The creator is **not responsible** for any misuse, damage, or violation of terms associated with OpenAI or any third-party service.  
> Do **not** include real API keys in public repositories.

---

## 📄 License

Apache-2.0 License. See [LICENSE](./LICENSE) for details.

---

## ✨ Contributions

Pull requests and issues are welcome!

---

## ❤️ Author

Created by [Madan kumar](https://github.com/winklemad)  
Inspired by real-world API key testing scenarios.
