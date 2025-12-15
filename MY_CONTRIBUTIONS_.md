# My Contributions

**Role:** ML Engineering Lead  
**Project:** Logan River Discharge Prediction using LSTM  
**Team:** Kishore Ragul Alagarsamy, Jacob Haight, Ehsan Kahrizi

---

## Summary

As the ML engineering lead, I was responsible for all machine learning development:
-  **100%** of LSTM model architecture design
-  **100%** of training pipeline implementation  
-  **100%** of hyperparameter optimization experiments
-  **85%** of total code implementation
-  **Achieved RMSE: 0.5959** for 7-day discharge prediction

---
Technical Contributions
1. Model Architecture (100%)
Designed 2-layer LSTM in PyTorch with 45 hidden units, dropout regularization, and configurable hyperparameters.
2. Training Pipeline (100%)
Built training loop with early stopping, learning rate scheduling, and checkpointing. Converges in 50 epochs (~25 min).
3. Hyperparameter Optimization (100%)
Tested 10+ configurations varying layer sizes (20, 45), lag windows (31-71 days), and prediction horizons (7-19 days).
Best Result: Multivariate, 45 units, 31-day lag → RMSE: 0.5959 (15% improvement over baseline)
4. Data Preprocessing (70%)
Implemented sequence generation, sliding windows, z-score normalization, and PyTorch DataLoader.
Ehsan: Initial exploration (30%)
5. Evaluation (100%)
Implemented RMSE, MAE, R² metrics and prediction visualizations.
**Results Achieved:**
- Test RMSE: 0.5959 (discharge), 0.4541 (stage)
- R² Score: 0.8342 (discharge), 0.8756 (stage)

---
**Technical:**
- Deep Learning (LSTM architecture)
- PyTorch (model building, training)
- Time Series Analysis (sequence modeling)
- Hyperparameter Optimization
- Python (NumPy, Pandas, Matplotlib)

---

## Team Collaboration

**My Role:** ML Engineering  
- Designed and implemented all ML components
- Conducted all training and optimization
- Generated final results

**Jacob Haight's Role:** LSTM Setup
- Environment configuration
- Some visualization scripts

**Ehsan Kahrizi's Role:** Data Analysis
- Initial data exploration
- Feature selection support

---

**Results:**
- Best RMSE: 0.5959 (my optimization)
- 10+ experiments conducted (my work)
- All evaluation metrics (my implementation)

---
*For detailed technical implementation, see the Jupyter notebook: `Final_Project.ipynb`*
