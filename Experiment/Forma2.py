import pandas as pd
import matplotlib.pyplot as plt

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

# Función para graficar gráficos de pastel
def plot_pie_charts(df):
    fig, axes = plt.subplots(3, 1, figsize=(12, 18))

    # Iterations vs Gamma
    ax = axes[0]
    iterations_data = df.groupby('gamma')['Iterations'].mean()
    ax.pie(iterations_data, labels=iterations_data.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Iterations Distribution by Gamma', fontsize=16)

    # Memory Used vs Gamma
    ax = axes[1]
    memory_data = df.groupby('gamma')['Memory Used (MB)'].mean()
    ax.pie(memory_data, labels=memory_data.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Memory Used Distribution by Gamma', fontsize=16)

    # Time Execution vs Gamma
    ax = axes[2]
    time_data = df.groupby('gamma')['Time execution (ms)'].mean()
    ax.pie(time_data, labels=time_data.index, autopct='%1.1f%%', startangle=140)
    ax.set_title('Time Execution Distribution by Gamma', fontsize=16)

    plt.tight_layout()
    plt.show()

# Llamar a la función para graficar
plot_pie_charts(df)
