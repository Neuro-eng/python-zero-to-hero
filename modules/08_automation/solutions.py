import re

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
LOG_RE = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>[\d:]+) (?P<level>[A-Z]+) (?P<msg>.*)$")


def extract_emails(text):
    return EMAIL_RE.findall(text)


def parse_log_line(line):
    m = LOG_RE.match(line.strip())
    return m.groupdict() if m else None
