import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import koreanize_matplotlib

# Streamlit 애플리케이션 제목
st.title('인구 구조 시각화 대시보드')

# 데이터 불러오기
@st.cache_data
def load_data():
    file_path = 'age2411.csv'  # 스트림릿 클라우드에 업로드된 파일 경로
    data = pd.read_csv(file_path)
    return data

data = load_data()

# 행정구역 선택 드롭다운
region = st.selectbox(
    '행정구역을 선택하세요:',
    data['행정구역'].unique()
)

# 선택한 행정구역 데이터 필터링
region_data = data[data['행정구역'] == region]

# 연령별 데이터 추출
age_columns = [col for col in data.columns if '계_' in col and '총인구수' not in col]
age_values = region_data[age_columns].iloc[0].values

# 연령대 추출 (예: 0세, 1세, ..., 100세 이상)
age_labels = [col.split('_')[2] for col in age_columns]

# 인구 구조 시각화
fig, ax = plt.subplots()
ax.bar(age_labels, age_values)
plt.xticks(rotation=90)
plt.title(f'{region} 인구 구조')
plt.xlabel('연령대')
plt.ylabel('인구수')

# 그래프 출력
st.pyplot(fig)
