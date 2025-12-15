# Logan River Discharge Prediction using LSTM

<div align="center">




**Time-series forecasting of river discharge and water stage using LSTM neural networks**

*Team Project - Utah State University | Fall 2024*

</div>

---

## Overview

Predicting Logan River discharge and stage levels using Long Short-Term Memory (LSTM) networks for water resource management and agricultural planning.

**Best Model Performance:**
- Discharge RMSE: **0.5959**
- Stage RMSE: **0.4541**
- R² Score: **0.83+**

---

## Team

**Kishore Ragul Alagarsamy** - ML Engineering Lead
- Designed LSTM architecture and training pipeline
- Conducted all model experiments (10+ configurations)
- Implemented evaluation framework
- Contribution: 85% of code, 100% of ML development

**Jacob Haight** - LSTM Implementation  
**Ehsan Kahrizi** - Feature Selection & Data Analysis

*See [MY_CONTRIBUTIONS.md](MY_CONTRIBUTIONS_.md) for detailed breakdown*

---

## Problem Statement

Logan River provides water for agriculture, municipal use, and ecosystems. Accurate discharge prediction helps:
- Farmers plan irrigation schedules
- City manage water allocation
- Government agencies set water policies

Traditional methods fail to capture complex temporal patterns. This project uses deep learning for improved 7-day forecasts.

---

## Dataset

**Source:** Logan River Observatory, Utah State University  
**Timespan:** 2014-2024 (10 years)  
**Resolution:** 15-minute intervals → Daily averages  
**Stations:** WaterLab (upstream), Main Street (downstream)

| Variable | Description | Range |
|----------|-------------|-------|
| Discharge | Water flow volume (m³/s) | 0.5 - 52.0 |
| Stage | Water level (cm) | 20 - 160 |

---

## Methodology

### LSTM Architecture
```
Input (31-day lag) → LSTM(45 units, 2 layers) → Output (7-day forecast)
```

**Hyperparameters:**
- Hidden Units: 45
- Layers: 2
- Dropout: 0.2
- Optimizer: Adam (lr=0.001)
- Loss: MSE

### Experiments Conducted
1. **Univariate:** Discharge only → RMSE: 0.64
2. **Multivariate:** Discharge + Stage → **RMSE: 0.5959** 
3. **Downstream:** Predict Main Street from WaterLab → RMSE: 0.44

---

## Results

### Model Comparison

| Model | Configuration | Discharge RMSE | Stage RMSE |
|-------|--------------|----------------|------------|
| Univariate | 45 units, 51-day lag | 0.6357 | - |
| **Multivariate** | **45 units, 31-day lag** | **0.5959**  | **0.4541**  |
| Downstream | 45 units, 61-day lag | 0.4419 | 0.4648 |

### Key Findings
-  Multivariate models outperform univariate by 15%
-  31-day lag window optimal for 7-day predictions
-  Model captures seasonal patterns (spring snowmelt peaks)
-  Struggles with extreme events (>40 m³/s discharge)
-  Accuracy decreases beyond 7-day forecast horizon

---
Results and Outputs
Note: Due to GitHub's file size limitations, detailed experiment results and output files (211.7 MB) are not included in this repository.
What's excluded:

Complete experiment results (10000+ runs)
Trained model weights (.h5, .pkl, .pth files)
Generated visualizations and plots
Intermediate output files

Access Results:

📈 Key findings and metrics are summarized above in the Results section
Full results archive available upon request
Contact: a02449534@usu.edu or kishorealagar12@gmail.com
To reproduce results, follow the Quick Start guide below

## Quick Start

```bash
# Clone repository
git clone https://github.com/kishore02449534/river-discharge-prediction.git
cd river-discharge-prediction

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook Final_Project.ipynb
```

**Requirements:** Python 3.8+, PyTorch, NumPy, Pandas, Matplotlib



---

## Project Structure

```
river-discharge-prediction/
├── Final_Project.ipynb          # Main analysis
├── MainStreet_Discharge.csv     # Downstream data
├── MainStreet_Stage.csv         # Downstream data
├── WaterLab_Discharge.csv       # Upstream data
├── WaterLab_Stage.csv           # Upstream data
├── parse.py                     # Visualization script
├── requirements.txt             # Dependencies
├── presentations/               # Slides and proposal
└── README.md                    # This file
```

---

## Future Improvements

- Add weather data (precipitation, temperature, snowpack)
- Extend prediction horizon to 30-60 days
- Try alternative architectures (GRU, Transformer)
- Build web application (Flask + React)
- Deploy as real-time prediction API

---

## References

1. Mehedi et al. (2022). *Exploring Temporal Dynamics of River Discharge Using Univariate LSTM*. Hydrology, 9(11), 202.
2. Zhang et al. (2022). *Discharge Forecasting Using Hybrid LSTM Models*. Water, 14(11), 1794.

---

<div align="center">


*Developed as part of Data Science in Practice course at Utah State University*

</div>
