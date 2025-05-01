import pages.data_science as data_science
import pages.programming as programming
import pages.ai_future as ai_future

def route_page(selected):
    if selected == "데이터 과학":
        data_science.app()
    elif selected == "프로그래밍":
        programming.app()
    elif selected == "인공지능과 미래사회":
        ai_future.app()
