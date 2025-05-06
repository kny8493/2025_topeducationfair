import streamlit as st
from footer import footer

st.set_page_config(page_title="인공지능과 미래사회", layout="wide")

st.title("🤖 인공지능과 미래사회")

# ▒▒ 과목 소개 ▒▒
st.markdown("### 👋 이 과목은 어떤 과목인가요?")
st.markdown("""
**인공지능(AI)**, 말로만 들어봤지 어떻게 돌아가는지는 잘 모르겠다고요?  
이 수업에서는 AI가 **어떻게 문제를 해결하는지**, **데이터는 어떻게 쓰는지**,  
그리고 우리 사회에서 **AI가 어떤 역할을 하는지** 함께 배워요.

**AI 윤리부터 데이터 분석, 실제 프로젝트까지!**  
이 과목을 들으면 인공지능이 **막연한 기술이 아니라**,  
우리가 함께 만들어가는 기술이라는 걸 느낄 수 있어요.
""")

# ▒▒ 이런 친구에게 추천해요! ▒▒
st.markdown("### 🙋 이런 친구에게 추천해요!")
st.markdown("""
- 인공지능에 대해 **기초부터 배우고 싶은 친구**  
- AI를 **직접 실습하고 프로젝트까지 해보고 싶은 친구**  
- 사회 문제 해결, 데이터 분석, 코딩에 흥미가 있는 친구  
- 미래에 AI, 컴퓨터 관련 진로를 생각하는 친구
""")

# ▒▒ 배울 내용 한눈에 보기 ▒▒
st.markdown("### 🧠 배울 내용 한눈에 보기")

st.markdown("""
| 단원 | 배우는 내용 |
|------|--------------|
| **1. 인공지능과 함께** | 인공지능이란 무엇인지, 왜 필요한지, 사회에서 어떤 역할을 하는지 배워요 |
| **2. 인공지능과 데이터** | 데이터를 어떻게 수집하고, 정리하고, AI가 어떻게 활용하는지 알아봐요 |
| **3. 인공지능의 구현** | 기계학습(머신러닝), 딥러닝, 컴퓨터비전, 자연어처리 등 AI가 문제를 어떻게 해결하는지 체험해요 |
| **4. 미래를 위한 인공지능** | 다양한 분야의 사회 문제를 AI로 해결하는 프로젝트를 기획하고 발표해요 |
""", unsafe_allow_html=True)

# ▒▒ 우리가 해본 활동 예시 ▒▒
st.markdown("### 🧪 우리가 직접 해본 활동")
st.markdown("""
- 🎯 인공지능 윤리 실생활 사례 조사  
- 📊 뉴스 기사 분석해서 감정 분류하기
- 🎨 코딩 없는 머신러닝 체험  
- 💡 우리 학교에 필요한 AI 시스템 아이디어 제안  
- 🎓 올바른 chatgpt 활용 방법과 응용
""")

# ▒▒ 이 과목, 왜 들어야 할까? ▒▒
st.markdown("### ✅ 이 과목, 왜 꼭 들어야 할까요?")
st.markdown("""
- **AI는 모든 분야에서 필수 기술!**  
- 코딩을 몰라도 **이해하고 참여할 수 있는 활동 중심 수업**  
- 윤리, 사회, 기술을 아우르는 **융합적 사고력** 키움  
- 실제 사회 문제를 AI로 해결하는 **창의적 프로젝트 수행 경험**
""")

# ▒▒ 진로 연결 ▒▒
st.markdown("### 🧭 어떤 진로랑 연결될까요?")
st.markdown("""
- 인공지능 개발자  
- 데이터 분석가, AI 교육자  
- UX디자이너, AI 윤리 연구자  
- 빅데이터 전문가, 미래기술 정책가
""")

st.markdown("---")

st.markdown("### 🧪 우리가 직접 해본 AI 윤리 & ChatGPT 활동")

# 인공지능 윤리 활동 예시
st.markdown("#### 🔍 인공지능 윤리 문제 조사 프로젝트")

st.markdown("""
- [AI 윤리 발표 자료 1](https://www.canva.com/design/DAGhl6bjJbU/mWEMC66kkNXeMfp8nMCPzQ/view?utm_content=DAGhl6bjJbU&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=ha12bb8bb47)  
- [AI 윤리 발표 자료 2](https://www.canva.com/design/DAGhV36GuXY/n6Z-53O2YJVqd4U4nLUi0w/view?utm_content=DAGhV36GuXY&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hb800819ee4)
""")

# ChatGPT 활동 예시
st.markdown("#### 🤖 ChatGPT 이해와 올바른 사용")

chatgpt_links = {
    "김동형": "https://www.canva.com/design/DAGmE5f51Es/jp-JuZqCutH_R6em9Xb7eA/view?utm_content=DAGmE5f51Es&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h0fc991f868",
    "김민준": "https://www.canva.com/design/DAGmE6GZVdQ/noQcNRYwIIK-qNe9FpSOJQ/view?utm_content=DAGmE6GZVdQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h8a3e2f5b39",
    "이가영": "https://www.canva.com/design/DAGmE6IfrAg/sVO8IvoGYLBk2gqh62IuXQ/view?utm_content=DAGmE6IfrAg&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hb7cb647703",
    "정태희": "https://www.canva.com/design/DAGmKc_dvow/cijV7qBrhO_7Gr8bx0u9XQ/view?utm_content=DAGmKc_dvow&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hc129e44d6b"
}

for name, link in chatgpt_links.items():
    st.markdown(f"- [{name} - ChatGPT 발표자료]({link})")


st.markdown('---')
st.title("🤖 인공지능과 미래사회 퀴즈")

st.markdown("아래 문제를 풀고, 화살표를 눌러 정답과 설명을 확인해보세요!")

# 퀴즈 1
st.subheader("1. 인공지능은 사람처럼 생각하고 학습하는 기술이다. (O/X)")
with st.expander("📌 정답 보기"):
    st.markdown("**정답: O**  \nAI는 데이터를 기반으로 학습하고, 판단과 예측을 수행할 수 있는 기술입니다.")

# 퀴즈 2
st.subheader("2. 인공지능과 미래사회는 토평고등학교에서 언제 생긴 과목일까요?")
with st.expander("📌 정답 보기"):
    st.markdown("**정답: 2023**  \n2023년도부터 입학생부터 있었습니다.")

# 퀴즈 3
st.subheader("3. 다음 중 인공지능이 활용되는 분야가 아닌 것은?")
st.markdown("A. 자율주행 자동차  \nB. 음악 작곡  \nC. 음식 조리 기계  \nD. 연필 생산")
with st.expander("📌 정답 보기"):
    st.markdown("**정답: D**  \n연필 생산은 단순한 기계 자동화이며, 인공지능 기술이 특별히 활용되지는 않습니다.")

st.markdown("---")

footer()