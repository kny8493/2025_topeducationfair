# footer.py
import streamlit as st
import os
import datetime

def footer(author="김나영"):
    # 현재 실행 중인 파일 경로
    current_file = os.path.abspath(__file__)

    try:
        # 파일 마지막 수정 시간
        last_modified = os.path.getmtime(current_file)
        last_modified_str = datetime.datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d %H:%M')
    except:
        last_modified_str = "알 수 없음"

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown(f"""
    <p style='text-align: center; font-size: 14px; color: gray;'>
        Made by <b>{author}</b> | ⓒ 2025 토평고등학교 교육과정 박람회<br>
        Last Modified: {last_modified_str}<br>
        Contact: 2학년부 김나영(담당교과: 프로그래밍, 인공지능과 미래사회)
    </p>
    """, unsafe_allow_html=True)
