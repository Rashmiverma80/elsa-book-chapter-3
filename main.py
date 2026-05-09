from src.data_preprocessing import load_and_preprocess_data
from src.model_training import train_model
from src.model_evaluation import evaluate_model
from src.visualization import plot_predicted_vs_experimental

# Load and preprocess data
X, y, scaler = load_and_preprocess_data(
    "data/geopolymer_strength_dataset.csv"
)

# Train model
model, X_train, X_test, y_train, y_test = train_model(X, y)

# Evaluate model
y_pred, r2, rmse, mae = evaluate_model(model, X_test, y_test)

# Save metrics
with open("results/performance_metrics.txt", "w") as f:
    f.write(f"R2 Score : {r2:.3f}\n")
    f.write(f"RMSE     : {rmse:.3f} MPa\n")
    f.write(f"MAE      : {mae:.3f} MPa\n")

# Generate Figure 3
plot_predicted_vs_experimental(
    y_test,
    y_pred,
    r2,
    rmse,
    mae,
    "results/figure_3_predicted_vs_experimental.png"
)

print("Model training, evaluation, and visualization completed successfully.")