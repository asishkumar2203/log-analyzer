import re
import json
from collections import defaultdict, Counter
from datetime import datetime
from typing import List, Optional, Dict


LOG_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - ([^-]+) - ([^-]+) - (.+)')

def parse_log_line(line: str) -> Optional[Dict]:
    match = LOG_PATTERN.match(line.strip())
    if match:
        try:
            timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return None
        return {
            'timestamp': timestamp,
            'service_name': match.group(2).strip(),
            'log_level': match.group(3).strip(),
            'message': match.group(4).strip()
        }
    return None


def read_log_file(filename: str) -> List[Dict]:
    entries = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            entry = parse_log_line(line)
            if entry:
                entries.append(entry)
            else:
                print(f"[Warning] Skipping line {i}: {line.strip()}")
    return entries


def analyze_logs(entries: List[Dict]) -> Dict:
    log_level_counter = Counter()
    service_counter = Counter()
    error_messages = Counter()

    for entry in entries:
        log_level_counter[entry['log_level']] += 1
        service_counter[entry['service_name']] += 1
        if entry['log_level'] == 'ERROR':
            error_messages[entry['message']] += 1

    most_common_error = error_messages.most_common(1)
    return {
        'log_levels': dict(log_level_counter),
        'services': dict(service_counter),
        'most_common_error': {
            'message': most_common_error[0][0] if most_common_error else None,
            'count': most_common_error[0][1] if most_common_error else 0
        }
    }


def filter_by_datetime(entries: List[Dict], start: datetime, end: datetime) -> List[Dict]:
    return [entry for entry in entries if start <= entry['timestamp'] <= end]


def main():
    filename = 'app.log'
    print(f"Reading from '{filename}'...\n")
    entries = read_log_file(filename)
    analysis = analyze_logs(entries)

    print(json.dumps(analysis, indent=4, default=str))


if __name__ == '__main__':
    main()
