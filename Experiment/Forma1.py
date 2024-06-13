import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos de experimentación
data = {
    'gamma': [0.1, 0.1, 0.1, 0.5, 0.5, 0.5, 0.8, 0.8, 0.8, 0.9, 0.9, 0.9, 0.99, 0.99, 0.01, 0.01],
    'threshold': [0.1, 0.01, 0.001, 0.1, 0.01, 0.001, 0.1, 0.01, 0.001, 0.1, 0.01, 0.001, 0.001, 0.0001, 0.001, 0.0001],
    'Iterations': [3, 4, 5, 5, 8, 11, 12, 22, 32, 23, 45, 67, 689, 918, 3, 3],
    'Memory Used (MB)': [1.14, 1.14, 1.21, 1.24, 1.19, 1.14, 1.18, 1.24, 1.15, 1.19, 1.14, 1.16, 1.14, 1.16, 1.15, 1.16],
    'Time execution (ms)': [17.34, 19.74, 16.77, 18.96, 21.88, 18.74, 18.20, 19.23, 19.88, 20.73, 22.85, 28.38, 95.16, 120.35, 19.32, 16.92]
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Establecer el estilo de seaborn
sns.set(style="whitegrid")

# Función para graficar
def plot_experimentation(df):
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))

    # Iterations vs Gamma y Threshold
    ax = axes[0]
    sns.lineplot(data=df, x='gamma', y='Iterations', hue='threshold', marker='o', ax=ax, palette="tab10")
    ax.set_title('Iterations vs Gamma and Threshold', fontsize=16)
    ax.set_xlabel('Gamma', fontsize=14)
    ax.set_ylabel('Iterations', fontsize=14)
    ax.legend(title='Threshold', fontsize=12, title_fontsize='13')

    # Memory Used vs Gamma y Threshold
    ax = axes[1]
    sns.lineplot(data=df, x='gamma', y='Memory Used (MB)', hue='threshold', marker='o', ax=ax, palette="tab10")
    ax.set_title('Memory Used vs Gamma and Threshold', fontsize=16)
    ax.set_xlabel('Gamma', fontsize=14)
    ax.set_ylabel('Memory Used (MB)', fontsize=14)
    ax.legend(title='Threshold', fontsize=12, title_fontsize='13')

    # Time Execution vs Gamma y Threshold
    ax = axes[2]
    sns.lineplot(data=df, x='gamma', y='Time execution (ms)', hue='threshold', marker='o', ax=ax, palette="tab10")
    ax.set_title('Time Execution vs Gamma and Threshold', fontsize=16)
    ax.set_xlabel('Gamma', fontsize=14)
    ax.set_ylabel('Time Execution (ms)', fontsize=14)
    ax.legend(title='Threshold', fontsize=12, title_fontsize='13')

    plt.tight_layout()
    plt.show()

# Llamar a la función para graficar
plot_experimentation(df)
