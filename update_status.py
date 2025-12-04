import random
from pathlib import Path
import re

STATUSES = [
    "Local causality secured. No Reading Steiner anomalies detected."
    "Stable. Observing anomalies. Logging results.",
    "Pilot link established. Neural signals nominal."
    "Parameter shift detected. Worldline classification pending."
    "Core harmony detected. No pattern-blue signatures."
]

readme_path = Path("README.md")
text = readme_path.read_text()

new_status = random.choice(STATUSES)

pattern = r"<!--STATUS_START-->(.|\n)*?<!--STATUS_END-->"
replacement = f"<!--STATUS_START-->\n{new_status}\n<!--STATUS_END-->"
new_text = re.sub(pattern, replacement, text)

readme_path.write_text(new_text)
