# Smart Manufacturing Monitoring System — Industry 4.0

## Project Overview

This independent project explores manufacturing performance monitoring using Python, simulated production data, and GitHub Actions.

The project focuses on production output, product quality, machine downtime, and energy consumption in a simulated electric vehicle component factory.

## Technologies

- Python
- CSV data processing
- GitHub
- GitHub Actions
- SVG data visualization
- Industry 4.0 concepts

## Manufacturing KPIs

| KPI | Result |
|---|---:|
| Total production | 4,680 units |
| Defective products | 100 units |
| Defect rate | 2.14% |
| Total downtime | 225 minutes |
| Energy consumption | 2,006 kWh |

## Machine Downtime

| Machine | Downtime |
|---|---:|
| M01 | 140 minutes |
| M02 | 85 minutes |

Machine M01 recorded the highest downtime in the simulated dataset.

## Project Structure

- `data/production_data.csv` — simulated manufacturing dataset
- `src/production_analysis.py` — manufacturing KPI calculations
- `src/create_charts.py` — chart-generation script
- `charts/` — manufacturing chart documentation
- `docs/initial_findings.md` — detailed analysis report
- `.github/workflows/manufacturing-analysis.yml` — automated workflow

## Automation

GitHub Actions executes the Python analysis and generates a machine downtime chart. The chart is uploaded as a workflow artifact.

## Future Improvements

- Display generated charts directly in the repository
- Analyse energy consumption per unit
- Add more manufacturing data
- Explore predictive maintenance
- Investigate SAP manufacturing and integration concepts

## Disclaimer

All data is simulated for educational purposes. This independent project is not affiliated with or endorsed by SAP or any manufacturing company.
