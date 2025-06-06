import streamlit as st
from footer import footer

st.set_page_config(page_title="프로그래밍 (Python)", layout="wide")

st.title("💻 프로그래밍 (Python)")

# ▒▒ 소개 ▒▒
st.markdown("### 👋 이 과목은 어떤 과목일까?")
st.markdown("""
“**파이썬으로 직접 프로그램을 만들 수 있다면?**”  
이 수업은 그런 꿈을 이뤄주는 과목이야!

- 우리가 자주 듣는 **웹, 인공지능, 앱 개발**에 꼭 쓰이는 언어인 **Python**을 다뤄!
- 기초 문법부터 직접 만드는 프로젝트까지 차근차근 배울 수 있어!
""")

# ▒▒ 이런 친구에게 추천해! ▒▒
st.markdown("### 🙋 이런 친구에게 추천해!")
st.markdown("""
- **코딩 처음이지만** 흥미 있는 친구  
- **앱/게임 만들기**에 관심 있는 친구  
- **나중에 컴퓨터 관련 진로** 생각 중인 친구  
- 혼자서도 **작은 프로그램 만들어보고 싶은 친구**
""")

# ▒▒ 배울 내용 한눈에 보기 ▒▒
st.markdown("### 🧠 배울 내용 한눈에 보기")

st.markdown("""
| 주제 | 예시 설명 |
|------|-----------|
| **파이썬 시작하기** | 'Hello Python!' 출력하기, 개발 도구 설치하기 |
| **변수 & 자료형** | 숫자 저장, 이름 저장, 리스트로 여러 값 관리 |
| **조건문 & 반복문** | “만약 ~라면”, “~하는 동안 반복하기” |
| **함수 만들기** | 계산기처럼 자주 쓰는 기능을 함수로 묶기 |
| **모듈과 패키지** | 남이 만든 도구 불러와서 내 프로그램에 쓰기 |
| **클래스와 객체** | 진짜 앱 개발할 때 필요한 개념도 가볍게 맛보기 |
| **파일 저장/불러오기** | 텍스트 파일 만들고, 내용 저장하기 |
| **미니 프로젝트** | 나만의 퀴즈 앱, 계산기, 가계부, 랜덤 뽑기 만들기 등 |
""", unsafe_allow_html=True)

# ▒▒ 내가 직접 만들어봤어요! ▒▒
st.markdown("### 🧪 우리가 직접 해본 프로젝트 예시")
st.markdown("""
- 📱 나만의 **BMI 계산기** 만들기  
- 🎲 **랜덤 점심 메뉴 추천기**  
- ✍️ 실생활 문제 해결 프로그램 개발
- 📈 친구들 이름 입력하고 **성적 통계 그래프** 그리기
""")

# ▒▒ 이 과목 들으면 뭐가 좋을까? ▒▒
st.markdown("### ✅ 이 과목, 왜 들어야 할까?")
st.markdown("""
- **프로그래밍이 뭔지 감 잡을 수 있어요**  
- 나중에 **전공 안 해도 코딩을 읽고 쓰는 힘**을 기를 수 있어요  
- 실생활에서 '이거 내가 만들 수 있어?' 싶던 걸 **직접 만들 수 있어요**
""")

# ▒▒ 진로 연결 ▒▒
st.markdown("### 🧭 관련 진로도 많아요!")
st.markdown("""
- 소프트웨어 개발자  
- 인공지능 개발자  
- 앱/웹 프로그래머  
- 데이터 분석가 등 IT 진로와도 연결돼요!
""")

st.markdown('---')
st.markdown("### 🧪 우리가 직접 만든 프로그램 예시")

st.markdown("""
수업에서는 단순히 문법만 배우지 않아요!  
배운 걸 바로 활용해서 이런 프로그램들을 직접 만들어요.  

- ➗ **배수 판별 프로그램**: 숫자를 입력하면 3의 배수인지 알려줘요  
- ✅ **짝수/홀수 판별 프로그램**: 조건문을 써서 짝수인지 판별해요  
- 🔐 **로그인 프로그램**: 아이디와 비밀번호가 맞는지 확인해주는 간단한 로그인 시스템  
- 🧮 **계산기 만들기**, 📋 **간단한 가계부**, 🎮 **랜덤 숫자 맞추기 게임** 도 만들어볼 수 있어요!
""")

st.markdown('---')
st.markdown("### 👨‍💻 수업 분위기 엿보기")

st.markdown("""
프로그래밍 수업은 단순히 교과서로 배우는 게 아니라 실제 기업에서 사용하는 온라인 플랫폼(goorm, codle)을 통해  
**학생 개개인이 실습하며 프로젝트를 완성해 나가는 수업**!
""")

# ▒▒ 실습 화면 3개 ▒▒
st.markdown("#### 💻 실습 화면 (Goorm, Codle 플랫폼)")
cols = st.columns(3)
cols[0].image("img/구름1.png", caption="구름 IDE 실습 화면 1")
cols[1].image("img/구름2.png", caption="구름 IDE 실습 화면 2")
cols[2].image("img/구름3.png", caption="구름 IDE 실습 화면 3")

# ▒▒ 수업 사진 2개 ▒▒
st.markdown("#### 🏫 실제 수업 현장 모습")
cols2 = st.columns(2)
cols2[0].image("img/수업사진1.png", caption="수업 모습 1")
cols2[1].image("img/수업사진2.png", caption="수업 모습 2")



st.markdown('---')

st.title("💻 프로그래밍 퀴즈")
st.markdown("아래 문제를 풀고, 정답과 해설은 화살표를 눌러 확인해보세요!")

# 퀴즈 1
st.subheader("1. 프로그래밍은 어떤 언어를 배우는 교과인가요?")
st.markdown("A. C언어  \nB. Python  \nC. Java  \nD. HTML")
with st.expander("📌 정답 보기"):
    st.markdown("**정답: B**  \n토평고에서는 문법이 간단하고 직관적인 파이썬(Python)을 중심으로 프로그래밍을 배웁니다.")

# 퀴즈 2
st.subheader("2. 프로그래밍에서 '반복문'은 무엇을 위해 사용될까요?")
st.markdown("A. 조건을 비교하기 위해  \nB. 같은 코드를 여러 번 실행하기 위해  \nC. 에러를 찾기 위해  \nD. 프로그램을 종료하기 위해")
with st.expander("📌 정답 보기"):
    st.markdown("**정답: B**  \n반복문은 특정 명령을 여러 번 반복 실행할 때 사용합니다. 예: `for`, `while` 문")

# 퀴즈 4
st.subheader("3. 프로그래밍 수업은 학교 교육과정에서 언제 개설되나요?")
st.markdown("A. 1학년  \nB. 2학년 1학기  \nC. 2학년 2학기  \nD. 3학년 1학기")
with st.expander("📌 정답 보기"):
    st.markdown("**정답: C**  \n2022 개정 교육과정 기준으로 토평고등학교에서는 **2학년 2학기**에 프로그래밍 중심 정보 수업이 개설됩니다.")


footer()