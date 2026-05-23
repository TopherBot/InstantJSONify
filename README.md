# InstantJSONify

**InstantJSONify** is a minimal Python tool that transforms plain‑text key/value pairs into a clean JSON object in a single step.

### Features
- Instant execution (no startup overhead).
- Error‑free parsing of quoted strings, numbers, booleans and `null`.
- Reads from **stdin** or a file path argument.
- Outputs compact JSON to **stdout**.
- Zero third‑party dependencies – just Python 3.8+.

### Usage
```bash
# From a file
python instant_jsonify.py data.txt > data.json

# Piped input
cat data.txt | python instant_jsonify.py > data.json
```

### Input format
Each line should contain a single key/value pair separated by `:`.
```
name: "Alice"
age: 30
active: true
notes: null
```

### License
MIT (see LICENSE file).

---
*InstantJSONify – because parsing should be instant and flawless.*