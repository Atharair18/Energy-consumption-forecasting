[README.md](https://github.com/user-attachments/files/32491496/README.md)
# WattWise — Predicting Household Energy Consumption

Forecasting a household's daily electricity usage using historical consumption patterns, and identifying which factors drive that usage the most.

## Problem Statement

Utility companies and households alike benefit from being able to anticipate electricity demand ahead of time — for grid load planning, cost management, or simply understanding one's own usage habits. This project explores whether a household's near-future daily power consumption can be predicted from its own recent usage history and calendar patterns.

## Dataset

- **Source:** [UCI Individual Household Electric Power Consumption Dataset](https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set) (via Kaggle)
- **Description:** Minute-level electricity readings from a single household in France, collected over ~4 years (2006–2010), including global active power, voltage, current intensity, and sub-metered usage for the kitchen, laundry room, and water heater/AC.
- **Size:** ~2 million minute-level readings, resampled to ~1,440 daily records for this project.

## Approach

1. **Data Cleaning** — Handled missing values (`?` markers) and dropped incomplete rows.
2. **Resampling** — Aggregated minute-level readings into daily averages to reduce noise and make the problem more tractable.
3. **Exploratory Data Analysis** — Identified a clear seasonal pattern: consumption rises in winter (likely heating) and dips in summer.
4. **Feature Engineering** — Initially included same-day electrical measurements (voltage, sub-metering) as features, but this caused severe data leakage (unrealistic R² of 0.998), since those values are mathematically tied to the target. Corrected this by switching to genuine forecasting features:
   - Lag features: usage 1, 2, 3, and 7 days prior
   - A 7-day rolling average of past usage
   - Calendar features: month, day of week, weekend flag, year
5. **Modeling** — Trained a Random Forest Regressor, using a chronological (non-shuffled) train/test split to avoid leaking future information into training, as is standard for time-series problems.
6. **Evaluation** — Assessed with MAE, RMSE, and R² on held-out future data.

## Results

| Metric | Value |
|---|---|
| MAE | 0.176 kW |
| RMSE | 0.242 kW |
| R² | 0.393 |

The model captures broad trends and seasonality well (see the actual-vs-predicted chart below) but smooths over sudden day-to-day spikes, which likely stem from one-off household events not present in the data (e.g., unusual cooking, guests, appliance use).

**Feature importance** showed that the 7-day rolling average (44.8%) and yesterday's usage (18.7%) were by far the strongest predictors — far outweighing calendar features like month or day of week. This suggests that once recent usage history is known, the exact calendar date adds relatively little further predictive value.

## Limitations & Future Improvements

- No external weather data — temperature is likely a major unexplained driver of heating/cooling usage and would probably improve accuracy significantly.
- Single household only — patterns may not generalize to other households or regions.
- Could explore dedicated time-series models (SARIMA, Prophet) or deep learning approaches (LSTM) for comparison.

## Tech Stack

Python, pandas, scikit-learn, matplotlib

## How to Run

1. Open the notebook in Google Colab.
2. Add your Kaggle API credentials (`kaggle.json`) to download the dataset.
3. Run all cells in order.
