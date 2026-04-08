import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 데이터 불러오기
df = pd.read_csv('train.csv')

# 2. 기초 통계량 확인 (엑셀보다 훨씬 상세함)
print("--- 기초 통계량 ---")
print(df.describe())

# 3. 결측치 재확인 (엑셀 필터로 놓친 공백 문자 찾기)
# 'TotalCharges'에 공백이 있으면 수치형 변환 시 에러가 나므로 미리 체크
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
print("\n--- 변환 후 결측치 개수 ---")
print(df.isnull().sum())

# 4. 이탈 여부(Churn) 시각화
plt.figure(figsize=(8, 5))
sns.countplot(x='Churn', data=df, hue='Churn', palette='viridis', legend=False)
plt.title('Churn Distribution')
plt.show()

# 5. 월 요금(MonthlyCharges)과 이탈의 관계 (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df, hue='Churn', palette='viridis', legend=False)
plt.title('Monthly Charges vs Churn')
plt.show()

df_sample = df.sample(n=1000, random_state=42)

# 전체 산점도 행렬 그리기
sns.pairplot(df_sample, hue='Churn', palette='husl')
plt.show()

