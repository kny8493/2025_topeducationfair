# footer.py
import streamlit as st

def footer(author="김나영"):

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown(f"""
    <p style='text-align: center; font-size: 14px; color: gray;'>
        Made by <b>{author}</b> | ⓒ 2025 토평고등학교 교육과정 박람회<br>
        Contact: 2학년부 김나영(담당교과: 프로그래밍, 인공지능과 미래사회)
    </p>
    """, unsafe_allow_html=True)
