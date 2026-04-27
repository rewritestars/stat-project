import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. 데이터 로드
df = pd.read_csv('data.csv')

# 2. 전처리 (TotalCharges 수치화 및 결측치 제거)
# 공백 문자 등을 NaN으로 바꾸고 결측치 11개 날려버림
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna(subset=['TotalCharges'])

print("--- 전처리 후 결측치 상태 ---")
print(df.isnull().sum())

# 3. 이상치 탐지 함수 (IQR 방식)
def analyze_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return len(outliers), lower_bound, upper_bound

# 4. 수치형 변수 이상치 체크 및 시각화 저장
numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

plt.figure(figsize=(15, 5))
for i, col in enumerate(numeric_cols, 1):
    # 통계치 계산
    count, lb, ub = analyze_outliers(df, col)
    print(f"[{col}] 이상치 개수: {count}개 (범위: {lb:.2f} ~ {ub:.2f})")
    
    # 시각화
    plt.subplot(1, 3, i)
    sns.boxplot(y=df[col], color='lightgreen')
    plt.title(f'Boxplot of {col}')

# 5. 결과 저장 (show 대신 save 써라 제발)
plt.tight_layout()
plt.savefig('outlier_analysis.png') 
plt.close()

print("\n--- 분석 완료! 'outlier_analysis.png' 파일 확인 ---")