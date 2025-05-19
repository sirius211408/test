import streamlit as st

# 啟用 session_state 以追蹤使用者進度
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.answers = []

# 測驗資料
quiz_data = [
    {
        "question": "你更喜歡哪種活動？",
        "options": ["閱讀書籍", "參加派對", "獨自旅行", "團體運動"],
        "answer": "閱讀書籍"
    },
    {
        "question": "遇到壓力時，你通常會？",
        "options": ["尋求朋友支持", "自己解決", "逃避問題", "尋求專業幫助"],
        "answer": "尋求朋友支持"
    },
    {
        "question": "你認為成功的關鍵是？",
        "options": ["努力工作", "良好人脈", "運氣", "持續學習"],
        "answer": "持續學習"
    }
]

st.title("🧠 心理測驗應用程式")

# 顯示問題
if st.session_state.current_index < len(quiz_data):
    current_question = quiz_data[st.session_state.current_index]
    st.subheader(f"問題 {st.session_state.current_index + 1}: {current_question['question']}")
    selected_option = st.radio("請選擇一個選項：", current_question['options'])

    if st.button("提交答案"):
        st.session_state.answers.append(selected_option)
        if selected_option == current_question['answer']:
            st.session_state.score += 1
        st.session_state.current_index += 1
        st.rerun()
else:
    st.subheader("🎉 測驗完成！")
    st.write(f"您的總分為：{st.session_state.score} / {len(quiz_data)}")
    if st.button("重新開始測驗"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.answers = []
        st.rerun()()