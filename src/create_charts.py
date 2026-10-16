import csv
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

DATA_FILE = Path("data/production_data.csv")
OUTPUT_DIR = Path("charts")
OUTPUT_FILE = OUTPUT_DIR / "machine_downtime.svg"

downtime_by_machine = defaultdict(int)

with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        machine = row["Machine"]
        downtime = int(row["Downtime_min"])
        downtime_by_machine[machine] += downtime

OUTPUT_DIR.mkdir(exist_ok=True)

chart_width = 800
chart_height = 450
left_margin = 160
right_margin = 60
top_margin = 80
bar_height = 55
bar_gap = 55

max_downtime = max(downtime_by_machine.values(), default=1)
available_width = chart_width - left_margin - right_margin

svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'width="{chart_width}" height="{chart_height}" '
    f'viewBox="0 0 {chart_width} {chart_height}">',
    '<rect width="100%" height="100%" fill="white"/>',
    '<text x="400" y="40" text-anchor="middle" '
    'font-size="24" font-family="Arial" font-weight="bold">'
    'Machine Downtime Analysis</text>',
    '<text x="400" y="65" text-anchor="middle" '
    'font-size="14" font-family="Arial" fill="#555">'
    'Simulated manufacturing data</text>',
]

for index, (machine, downtime) in enumerate(
    sorted(downtime_by_machine.items())
):
    y = top_margin + index * (bar_height + bar_gap)
    bar_width = available_width * downtime / max_downtime

    svg_parts.extend([
        f'<text x="{left_margin - 20}" y="{y + 35}" '
        f'text-anchor="end" font-size="18" font-family="Arial">'
        f'{escape(machine)}</text>',
        f'<rect x="{left_margin}" y="{y}" width="{bar_width:.1f}" '
        f'height="{bar_height}" fill="#2878B5" rx="5"/>',
        f'<text x="{left_margin + bar_width + 10:.1f}" '
        f'y="{y + 35}" font-size="17" font-family="Arial">'
        f'{downtime} min</text>',
    ])

svg_parts.extend([
    '<text x="400" y="420" text-anchor="middle" '
    'font-size="14" font-family="Arial" fill="#555">'
    'Total downtime measured in minutes</text>',
    '</svg>',
])

OUTPUT_FILE.write_text("\n".join(svg_parts), encoding="utf-8")

print("MACHINE DOWNTIME CHART")
print("----------------------")

for machine, downtime in sorted(downtime_by_machine.items()):
    print(f"{machine}: {downtime} minutes")

print(f"\nChart saved to: {OUTPUT_FILE}")
