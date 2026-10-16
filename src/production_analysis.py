import csv
from collections import defaultdict

# Load the manufacturing dataset
file_path = "data/production_data.csv"

total_produced = 0
total_defective = 0
total_downtime = 0
total_energy = 0

machine_downtime = defaultdict(int)

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        produced = int(row["Produced"])
        defective = int(row["Defective"])
        downtime = int(row["Downtime_min"])
        energy = float(row["Energy_kWh"])

        total_produced += produced
        total_defective += defective
        total_downtime += downtime
        total_energy += energy

        machine_downtime[row["Machine"]] += downtime

# Calculate manufacturing KPIs
defect_rate = (total_defective / total_produced) * 100

print("SMART MANUFACTURING REPORT")
print("-" * 30)

print(f"Total produced: {total_produced} units")
print(f"Total defective: {total_defective} units")
print(f"Defect rate: {defect_rate:.2f}%")
print(f"Total downtime: {total_downtime} minutes")
print(f"Total energy consumption: {total_energy:.0f} kWh")

print("\nDOWNTIME BY MACHINE")

for machine, downtime in machine_downtime.items():
    print(f"{machine}: {downtime} minutes")

worst_machine = max(machine_downtime, key=machine_downtime.get)

print(f"\nHighest downtime: {worst_machine}")
# SUSTAINABLE MANUFACTURING KPI
# -----------------------------

total_produced = 0
total_energy = 0

with open("data/production_data.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_produced += int(row["Produced"])
        total_energy += float(row["Energy_kWh"])

energy_per_unit = total_energy / total_produced if total_produced else 0

print("\nSUSTAINABILITY REPORT")
print("---------------------")
print(f"Total energy consumption: {total_energy:.0f} kWh")
print(f"Energy consumption per unit: {energy_per_unit:.3f} kWh/unit")
