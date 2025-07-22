import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="부동산 투자 추천 시스템", layout="wide")

st.title("🏘️ 부동산 투자 추천 시스템")
st.markdown("적합한 투자처를 데이터 기반으로 추천합니다.")

# 절대 경로 확인용 디버그 출력
st.write("현재 위치:", os.getcwd())
st.write("폴더 내 파일들:", os.listdir())

@st.cache_data
def load_data():
    path = "data/sample_properties.csv"
    return pd.read_csv(path)

try:
    df = load_data()
except FileNotFoundError:
    st.error("❌ sample_properties.csv 파일을 찾을 수 없습니다. GitHub에 제대로 업로드되었는지 확인하세요.")
    st.stop()

budget = st.slider("최대 투자 예산 (만원)", min_value=1000, max_value=50000, step=500, value=30000)
filtered_df = df[df["매매가"] <= budget]
sorted_df = filtered_df.sort_values("추천점수", ascending=False)

st.subheader("🔍 추천 투자 대상 (예산 이하)")
st.dataframe(sorted_df.reset_index(drop=True), use_container_width=True)
