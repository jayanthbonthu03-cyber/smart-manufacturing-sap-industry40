# Initial Manufacturing Analysis Report

## 1. Project Overview

This project explores how Industry 4.0 concepts and data analytics can improve manufacturing performance.

The project uses simulated production data from an electric vehicle component factory to analyse production output, product quality, machine downtime, and energy consumption.

The objective is to develop a simple Smart Manufacturing Monitoring System that converts production data into meaningful performance indicators.

## 2. Project Objectives

The main objectives of this project are:

- Monitor manufacturing production output.
- Analyse defective products and product quality.
- Compare machine downtime.
- Track manufacturing energy consumption.
- Identify potential production inefficiencies.
- Explore data-driven decision-making in manufacturing.
- Investigate future integration with SAP technologies.

## 3. Dataset Description

The project uses a CSV dataset containing 10 simulated manufacturing records collected over five days.

The dataset represents the production of two electric vehicle components:

- EV-Motor
- EV-Battery

### Dataset Fields

| Field | Description |
|---|---|
| Date | Production date |
| Machine | Machine identifier |
| Product | Manufactured product |
| Produced | Total units produced |
| Defective | Number of defective units |
| Downtime_min | Machine downtime in minutes |
| Energy_kWh | Energy consumption in kilowatt-hours |

### Data Limitations

The dataset is simulated for educational purposes. It does not represent actual factory operations.

The dataset is relatively small and covers only five days. Therefore, the findings demonstrate the analysis process rather than establishing long-term manufacturing trends.

## 4. Key Performance Indicators

The Python script calculates several manufacturing Key Performance Indicators (KPIs).

### 4.1 Total Production

Total production represents the number of units manufactured during the observation period.

Formula:

Total Production = Sum of all Produced values

### 4.2 Total Defective Products

This KPI measures the total number of units identified as defective.

Formula:

Total Defective Products = Sum of all Defective values

### 4.3 Defect Rate

The defect rate measures the proportion of manufactured units that are defective.

Formula:

Defect Rate (%) = (Total Defective Products / Total Production) * 100

### 4.4 Total Machine Downtime

Machine downtime represents the total time during which machines were unavailable for production.

Formula:

Total Downtime = Sum of all Downtime_min values

### 4.5 Total Energy Consumption

This KPI measures the total energy consumed during the observation period.

Formula:

Total Energy Consumption = Sum of all Energy_kWh values

### 4.6 Downtime by Machine

Machine-level downtime analysis helps identify which machines account for the most downtime during the observation period.

## 5. Initial Findings

The Python analysis was executed successfully through GitHub Actions.

The script reads the manufacturing CSV dataset and calculates the selected KPIs automatically.

### 5.1 Manufacturing Performance Results

| KPI | Result |
|---|---:|
| Total production | 4,680 units |
| Total defective products | 100 units |
| Defect rate | 2.14% |
| Total machine downtime | 225 minutes |
| Total energy consumption | 2,006 kWh |

### 5.2 Downtime by Machine

| Machine | Total downtime |
|---|---:|
| M01 | 140 minutes |
| M02 | 85 minutes |
| **Total** | **225 minutes** |

### 5.3 Key Observations

**Production output**

The factory produced 4,680 units across the five-day observation period.

**Product quality**

The dataset contains 100 defective units. The overall defect rate is approximately 2.14%.

**Machine performance**

Machine M01 recorded 140 minutes of downtime, compared with 85 minutes for machine M02.

Machine M01 therefore accounted for approximately 62.2% of the recorded downtime.

**Energy consumption**

The recorded energy consumption was 2,006 kWh across the 10 production records.

Further analysis would be required to compare energy consumption per unit across different products and machines.

## 6. Initial Recommendations

Based on the preliminary findings, the following improvements could be investigated.

### 6.1 Reduce Machine Downtime

Investigate the reasons for machine M01's higher recorded downtime.

Potential approaches include preventive maintenance, monitoring machine conditions, and analysing recurring equipment problems.

The dataset alone does not establish the cause of the downtime.

### 6.2 Improve Product Quality

Monitor defective products regularly and investigate possible causes of manufacturing defects.

Additional information, such as defect categories, production batches, and machine settings, would help identify quality problems more accurately.

### 6.3 Monitor Energy Consumption

Analyse energy consumption alongside production output.

A useful future KPI would be:

Energy Intensity = Total Energy Consumption / Total Production

This indicator could help compare energy use over time, provided the production data and measurement boundaries are consistent.

### 6.4 Introduce Automated Monitoring

A future version of the system could automatically process new production records and flag unusual downtime, high defect rates, or increased energy consumption.

These alerts would require clearly defined thresholds and additional testing.

## 7. Technology Stack

### Currently Implemented

- **Python:** Calculates manufacturing performance indicators.
- **CSV:** Stores the simulated manufacturing dataset.
- **GitHub:** Hosts the project source code and documentation.
- **GitHub Actions:** Automatically executes the Python analysis workflow.

### Planned Future Technologies

- **Pandas:** For more advanced data processing.
- **Matplotlib:** For manufacturing performance charts.
- **SAP S/4HANA:** To investigate manufacturing and production-planning processes.
- **SAP Business Technology Platform (BTP):** To explore application development and integration concepts.
- **SAP Integration Suite:** To investigate integration between manufacturing data sources and business systems.
- **AI-assisted analytics:** To explore anomaly detection and predictive maintenance concepts.

The planned technologies have not yet been integrated into the current implementation.

## 8. Future Development Roadmap

The project will be developed incrementally.

### Phase 1: Data Analysis

- Maintain the manufacturing dataset.
- Calculate production and quality KPIs.
- Verify the calculations against the source data.

### Phase 2: Data Visualization

- Create charts for machine downtime.
- Visualize production output and defective products.
- Compare energy consumption across production records.

### Phase 3: Automated Monitoring

- Improve the GitHub Actions workflow.
- Add automated checks for data quality.
- Explore configurable warnings for unusual manufacturing results.

### Phase 4: Advanced Analytics

- Investigate relationships between downtime, defects, and energy consumption.
- Explore predictive maintenance using a suitable dataset.
- Evaluate the limitations of small datasets and simulated results.

### Phase 5: SAP and Industry 4.0 Concepts

- Study SAP manufacturing and production-planning processes.
- Investigate how manufacturing data could be exchanged with business systems.
- Develop a prototype integration using suitable interfaces or simulated data.
- Document the architecture and limitations of the prototype.

## 9. Conclusion

This project establishes a foundation for a Smart Manufacturing Monitoring System using Python and Industry 4.0 concepts.

The current implementation processes simulated production data, calculates manufacturing KPIs, and executes automatically through GitHub Actions.

The initial analysis identified a defect rate of 2.14% and showed that machine M01 accounted for the larger share of recorded downtime.

Future development will focus on data visualization, automated monitoring, advanced analytics, and exploring potential integration with SAP technologies.

The project demonstrates an initial application of programming and data analysis to manufacturing performance monitoring.

## 10. Project Scope and Disclaimer

This is an independent educational project.

All manufacturing records are simulated and do not represent actual factory operations.

SAP products and integration technologies are included as areas for future exploration only. The current project does not implement a live SAP connection.

This project is not affiliated with, endorsed by, or sponsored by SAP or any manufacturing company.
