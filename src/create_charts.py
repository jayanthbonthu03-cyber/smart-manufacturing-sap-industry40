import csv
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

DATA_FILE = Path("data/production_data.csv")
OUTPUT_DIR = Path("charts")
OUTPUT_FILE = OUTPUT_DIR / "machine_downtime.svg"
# --------------------------------------------------
# PRODUCT QUALITY ANALYSIS
# --------------------------------------------------

defective_by_machine = defaultdict(int)
produced_by_machine = defaultdict(int)

with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        machine = row["Machine"]
        produced = int(row["Produced"])
        defective = int(row["Defective"])

        produced_by_machine[machine] += produced
        defective_by_machine[machine] += defective

quality_chart = OUTPUT_DIR / "product_quality.svg"

chart_width = 800
chart_height = 450
left_margin = 160
right_margin = 100
top_margin = 100
bar_height = 55
bar_gap = 55

max_defects = max(defective_by_machine.values(), default=1)
available_width = chart_width - left_margin - right_margin

svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" '
    f'width="{chart_width}" height="{chart_height}" '
    f'viewBox="0 0 {chart_width} {chart_height}">',
    '<rect width="100%" height="100%" fill="white"/>',
    '<text x="400" y="40" text-anchor="middle" '
    'font-size="24" font-family="Arial" font-weight="bold">'
    'Product Quality Analysis</text>',
    '<text x="400" y="65" text-anchor="middle" '
    'font-size="14" font-family="Arial" fill="#555">'
    'Defective products by machine</text>',
]

for index, machine in enumerate(sorted(defective_by_machine)):
    defects = defective_by_machine[machine]
    y = top_margin + index * (bar_height + bar_gap)
    bar_width = available_width * defects / max_defects

    svg_parts.extend([
        f'<text x="{left_margin - 20}" y="{y + 35}" '
        f'text-anchor="end" font-size="18" font-family="Arial">'
        f'{escape(machine)}</text>',
        f'<rect x="{left_margin}" y="{y}" width="{bar_width:.1f}" '
        f'height="{bar_height}" fill="#2878B5" rx="5"/>',
        f'<text x="{left_margin + bar_width + 10:.1f}" '
        f'y="{y + 35}" font-size="17" font-family="Arial">'
        f'{defects} defects</text>',
    ])

svg_parts.extend([
    '<text x="400" y="420" text-anchor="middle" '
    'font-size="14" font-family="Arial" fill="#555">'
    'Number of defective products</text>',
    '</svg>',
])

quality_chart.write_text("\n".join(svg_parts), encoding="utf-8")

print("\nPRODUCT QUALITY REPORT")
print("----------------------")

for machine in sorted(defective_by_machine):
    produced = produced_by_machine[machine]
    defects = defective_by_machine[machine]
    defect_rate = defects / produced * 100 if produced else 0

    print(f"{machine}: {defects} defective out of {produced} produced")
    print(f"  Defect rate: {defect_rate:.2f}%")

print(f"\nQuality chart saved to: {quality_chart}")
