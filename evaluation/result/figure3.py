import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv("benchmark_results.csv")

# 모델별 pass@1 성공/실패 개수
pass_counts = df.groupby('model')['pass@1'].value_counts().unstack(fill_value=0)

# 각 모델별 파이 차트
fig, axes = plt.subplots(1, len(pass_counts.index), figsize=(15, 5))
for i, model in enumerate(pass_counts.index):
    axes[i].pie(pass_counts.loc[model], labels=['Fail', 'Pass'], autopct='%1.1f%%', colors=['salmon', 'lightgreen'])
    axes[i].set_title(f'{model} Pass@1')

plt.suptitle('Pass@1 Success Rate by Model')
plt.tight_layout()

# 저장 및 표시
plt.savefig('pass_at_1_pie_chart.png', dpi=150)
plt.show()