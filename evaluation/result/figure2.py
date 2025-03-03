import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv("benchmark_results.csv")

# 선 차트 생성
plt.figure(figsize=(12, 6))
for model in df['model'].unique():
    model_data = df[df['model'] == model]
    plt.plot(model_data['question_idx'], model_data['execution_time'], marker='o', label=model)

plt.title('Execution time by Question Index')
plt.xlabel('Question Index')
plt.ylabel('execution_times')
plt.legend(title='Model')
plt.grid(True)
plt.tight_layout()

# 저장 및 표시
plt.savefig('line_chart.png', dpi=150)
plt.show()