#!/usr/bin/env python3
"""InstantJSONify – instantly convert key/value text to JSON.

Supported value types:
- Quoted strings (single or double quotes) → str
- Numbers (int or float) → int/float
- true / false (case‑insensitive) → bool
- null (case‑insensitive) → None

Usage:
    python instant_jsonify.py [input_file]
If no file is provided, reads from stdin.
"""

import sys
import json
import re

# Regex patterns for fast parsing
_STR_RE = re.compile(r"^[\'\"](.*?)[\'\"]$")
_NUM_RE = re.compile(r"^-?\d+(?:\.\d+)?$")
_BOOL_RE = re.compile(r"^(true|false)$", re.IGNORECASE)
_NULL_RE = re.compile(r"^null$", re.IGNORECASE)

def parse_value(val: str):
    val = val.strip()
    # String
    m = _STR_RE.match(val)
    if m:
        return m.group(1)
    # Number
    if _NUM_RE.match(val):
        return int(val) if val.isdigit() or (val[0] == '-' and val[1:].isdigit()) else float(val)
    # Boolean
    if _BOOL_RE.match(val):
        return val.lower() == 'true'
    # Null
    if _NULL_RE.match(val):
        return None
    # Fallback: treat as raw string
    return val

def parse_lines(lines):
    obj = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue  # Skip empty/comments
        if ':' not in line:
            raise ValueError(f"Invalid line (missing ':'): {line}")
        key, raw_val = line.split(':', 1)
        key = key.strip()
        obj[key] = parse_value(raw_val)
    return obj

def main():
    # Read source – file or stdin – instantly
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.read().splitlines()
    try:
        data = parse_lines(lines)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)
    # Output compact JSON with no delay
    json.dump(data, sys.stdout, separators=(',', ':'))
    sys.stdout.write('\n')

if __name__ == '__main__':
    main()
