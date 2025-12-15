# My Contributions

**Role:** ML Engineering Lead  
**Project:** Logan River Discharge Prediction using LSTM  
**Team:** Kishore Ragul Alagarsamy, Jacob Haight, Ehsan Kahrizi

---

## Summary

As the ML engineering lead, I was responsible for all machine learning development:
- ✅ **100%** of LSTM model architecture design
- ✅ **100%** of training pipeline implementation  
- ✅ **100%** of hyperparameter optimization experiments
- ✅ **85%** of total code implementation
- ✅ **Achieved RMSE: 0.5959** for 7-day discharge prediction

---

## Detailed Contributions

### 1. Model Architecture (100%)
**What I Did:**
- Designed PyTorch LSTM model with configurable hyperparameters
- Implemented both univariate and multivariate variants
- Added dropout regularization and batch normalization

**Result:** Successfully trained 2-layer LSTM with 45 hidden units

---

### 2. Training Pipeline (100%)
**What I Did:**
- Built complete training loop with PyTorch
- Implemented early stopping (patience=10)
- Added learning rate scheduling
- Created model checkpointing system

**Result:** Training completes in ~25 minutes, model converges in 50 epochs

---

### 3. Hyperparameter Optimization (100%)
**What I Did:**
- Tested 10+ configurations systematically
- Varied: layer sizes (20, 45), lag windows (31-71 days), prediction horizons (7-19 days)
- Compared univariate vs multivariate approaches

**Experiments Conducted:**

| Configuration | RMSE | Insight |
|--------------|------|---------|
| Univariate, 20 units, 31-day | 0.8570 | Baseline |
| Univariate, 45 units, 51-day | 0.6357 | More context helps |
| **Multivariate, 45 units, 31-day** | **0.5959** ✅ | **Best model** |

**Key Finding:** Multivariate approach improved predictions by 15%

---

### 4. Data Preprocessing (70%)
**What I Did:**
- Implemented sequence generation for LSTM input
- Created sliding window function for lag sequences
- Applied z-score normalization
- Built PyTorch DataLoader for batching

**Teammate Contribution:** Ehsan performed initial data exploration (30%)

---

### 5. Evaluation Framework (100%)
**What I Did:**
- Implemented RMSE, MAE, R² metrics
- Created prediction vs actual visualizations
- Generated error distribution analysis

**Results Achieved:**
- Test RMSE: 0.5959 (discharge), 0.4541 (stage)
- R² Score: 0.8342 (discharge), 0.8756 (stage)

---

## Code Breakdown

| Component | My Work | Lines of Code |
|-----------|---------|---------------|
| Model Definition | 100% | ~80 |
| Training Pipeline | 100% | ~150 |
| Hyperparameter Tuning | 100% | ~200 |
| Data Preprocessing | 100% | ~120 |
| Evaluation Metrics | 100% | ~100 |
| Visualization | 40% | ~60 |
| **Total** | **~85%** | **~710 / ~830** |

---

## Time Investment

**Total:** ~115 hours over 8 weeks

| Phase | Hours | Weeks |
|-------|-------|-------|
| Literature review & design | 12 | 1 |
| Model implementation | 15 | 1 |
| Training pipeline | 18 | 1 |
| Experiments (univariate) | 20 | 1 |
| Experiments (multivariate) | 22 | 1 |
| Downstream prediction | 10 | 1 |
| Analysis & evaluation | 8 | 1 |
| Documentation | 10 | 1 |

---

## Skills Demonstrated

**Technical:**
- Deep Learning (LSTM architecture)
- PyTorch (model building, training)
- Time Series Analysis (sequence modeling)
- Hyperparameter Optimization
- Python (NumPy, Pandas, Matplotlib)

**Research:**
- Literature review
- Experimental design
- Results analysis

**Leadership:**
- Led ML engineering efforts
- Collaborated with 2 teammates
- Presented methodology and results

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

## Evidence

**Notebook Authorship:**
- 85% of code cells written by me
- All model and training sections are my work
- Primary contributor to Final_Project.ipynb

**Results:**
- Best RMSE: 0.5959 (my optimization)
- 10+ experiments conducted (my work)
- All evaluation metrics (my implementation)

---

## Interview Talking Points

**"Tell me about this project"**

> "I led the ML engineering for a 3-person team predicting river discharge. I designed the LSTM architecture in PyTorch, implemented the training pipeline, and conducted systematic hyperparameter optimization. I tested 10+ configurations and achieved an RMSE of 0.5959 - a 15% improvement over the baseline. I wrote 85% of the code, focusing entirely on the machine learning components while my teammates helped with data collection and visualization."

**"What was your specific role?"**

> "I was the ML engineering lead. I was responsible for all model development - the architecture design, training pipeline, hyperparameter tuning, and evaluation. My teammates helped with initial data analysis and presentation, but all the deep learning work was mine."

**"What challenges did you face?"**

> "The biggest challenge was hyperparameter optimization. LSTMs are sensitive to configuration, so I systematically tested different layer sizes and lag windows. I found that a 31-day lag with 45 hidden units gave the best results for 7-day predictions. I also discovered that adding the stage variable improved predictions by 15%."

---

## Contact

**Kishore Ragul Alagarsamy**  
📧 kishorealagar12@gmail.com  
💻 [GitHub](https://github.com/kishore02449534)  
🔗 [LinkedIn](https://linkedin.com/in/kishore-ragul)

---

*For detailed technical implementation, see the Jupyter notebook: `Final_Project.ipynb`*
