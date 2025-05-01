import streamlit as st

st.title("💡 고등학교 선택과목 소개")
st.write("""
이 앱은 고등학교 2~3학년의 선택 과목에 대한 정보를 제공합니다.
왼쪽 사이드바에서 과목을 선택해 주세요.
""")


import streamlit as st

st.set_page_config(page_title="선택과목 메인", layout="wide")

st.sidebar.title("📚 목차")
choice = st.sidebar.radio("과목을 선택하세요", ["홈", "데이터 과학", "프로그래밍", "인공지능과 미래사회"])

# 해시를 활용한 페이지 이동
if choice == "데이터 과학":
    st.experimental_set_query_params(page="data_science")
    st.experimental_rerun()
elif choice == "프로그래밍":
    st.experimental_set_query_params(page="programming")
    st.experimental_rerun()
elif choice == "인공지능과 미래사회":
    st.experimental_set_query_params(page="ai")
    st.experimental_rerun()

st.title("🏫 고등학교 선택과목 소개")
st.write("왼쪽 목차에서 과목을 선택하세요.")
