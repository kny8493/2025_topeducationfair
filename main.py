import streamlit as st
from router import route_page

# 메뉴만 여기서 설정
st.sidebar.title("📚 목차")
selected = st.sidebar.radio("페이지 이동", ["데이터 과학", "프로그래밍", "인공지능과 미래사회"])

# 라우팅 실행
route_page(selected)
