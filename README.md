# Kaggle Projects

This repository contains my experiments and learning journey through hands-on Machine Learning (ML) projects, exploring different algorithms and techniques to solve real-world prediction problems.

## Projects

### Melbourne Housing Price Prediction
Predicting house prices in Melbourne, Australia using regression models. This project explores:
- **Decision Tree Regressor**: Initial model with hyperparameter tuning (`max_leaf_nodes`) to optimize tree depth
- **Random Forest Regressor**: Improved model that reduces overfitting by combining multiple decision trees, achieving a 22% improvement in prediction accuracy

**Key Techniques**: Train/validation splitting, Mean Absolute Error (MAE) evaluation, hyperparameter optimization

### Iowa Housing Price Prediction
Predicting house prices in Iowa using regression models. This project explores:
- **Random Forest Regressor**: A robust model trained on features like `LotArea`, `YearBuilt`, and `GrLivArea` to predict housing prices.
- **Feature Engineering**: Experimenting with additional features to improve model accuracy.
- **Validation and Submission**: Evaluating the model locally using Mean Absolute Error (MAE) and submitting predictions to Kaggle for leaderboard scoring.

**Key Techniques**: Train/validation splitting, feature selection, and generating submission files for Kaggle competitions.



## Datasets

All datasets used in these projects can be found on [Kaggle](https://www.kaggle.com/).

### Setting Up Kaggle API (for downloading datasets)

1. **Get API credentials**: Go to [Kaggle Account Settings](https://www.kaggle.com/settings) → API section → "Create New API Token"
2. **Place credentials**: Move the downloaded `kaggle.json` to `~/.kaggle/`
   ```bash
   mkdir -p ~/.kaggle
   mv ~/Downloads/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
3. **Download datasets:** Use the Kaggle CLI
   ```bash
   kaggle competitions download -c competition-name -p datasets/folder-name
   ```

### Submitting to Kaggle Competitions

1. **Generate predictions**: Run your model to create a submission file (usually a CSV)
   ```python
   output = pd.DataFrame({'Id': test_data.Id, 'Target': predictions})
   output.to_csv('submission.csv', index=False)
   ```

2. **Submit via Kaggle website**:
   - Go to the competition page
   - Click the "Submit Predictions" button
   - Upload your `submission.csv` file
   - Add a submission description (optional but recommended)

3. **Submit via Kaggle API** (faster):
   ```bash
   kaggle competitions submit -c competition-name -f submission.csv -m "Description of submission"
   ```

4. **Check your score**: View your position on the leaderboard after submission is processed

**Note**: Most competitions limit the number of daily submissions, so iterate and test locally before submitting!