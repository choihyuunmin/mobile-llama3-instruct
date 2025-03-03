import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
RESULTS_FILE = "benchmark_results.csv"
df = pd.read_csv(RESULTS_FILE)

# 모델별 평균 계산
avg_scores = df.groupby('model')[['pass@1', 'execution_time', 'memory_usage']].mean()

# 막대 차트 생성
fig, ax = plt.subplots(figsize=(10, 6))
avg_scores.plot(kind='bar', ax=ax)
plt.title('Model Benchmark Scores Comparison')
plt.xlabel('Model')
plt.ylabel('Score / Time (s) / Memory (MB)')
plt.legend(title='Metrics')
plt.xticks(rotation=45)
plt.tight_layout()

# 저장 및 표시
plt.savefig('bar_chart.png', dpi=150)
plt.show()

