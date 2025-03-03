import pandas as pd
from prettytable import PrettyTable

# CSV 파일 읽기
RESULTS_FILE = "benchmark_results.csv"
df = pd.read_csv(RESULTS_FILE)

# 모델별 평균 계산 (composite_score 제외)
metrics = ['pass@1', 'execution_time', 'memory_usage']
avg_scores = df.groupby('model')[metrics].mean()

# Evaluation Table 생성
table = PrettyTable()
table.field_names = ['Model'] + metrics  # 헤더 설정

# 데이터 추가
for model, row in avg_scores.iterrows():
    table.add_row([model, 
                   f"{row['pass@1']:.2f}", 
                   f"{row['execution_time']:.2f}", 
                   f"{row['memory_usage']:.2f}"])

# 표 출력
print("Evaluation Table (Averages by Model):")
print(table)

# CSV로 저장 (선택 사항)
avg_scores.to_csv('evaluation_table.csv')
print("\nEvaluation table saved to 'evaluation_table.csv'")