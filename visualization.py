import matplotlib.pyplot as plt

def plot_predicted_vs_experimental(y_test, y_pred, r2, rmse, mae, output_path):
    plt.figure(figsize=(8, 8))

    plt.scatter(y_test, y_pred, alpha=0.7, edgecolors="k")

    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())

    plt.plot(
        [min_val, max_val],
        [min_val, max_val],
        linestyle="--",
        linewidth=2,
        label="Ideal Prediction (y = x)"
    )

    plt.xlabel("Experimental Compressive Strength (MPa)", fontsize=12)
    plt.ylabel("Predicted Compressive Strength (MPa)", fontsize=12)

    plt.text(
        0.05, 0.95,
        f"$R^2$ = {r2:.3f}\nRMSE = {rmse:.2f} MPa\nMAE = {mae:.2f} MPa",
        transform=plt.gca().transAxes,
        fontsize=11,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.9)
    )

    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()