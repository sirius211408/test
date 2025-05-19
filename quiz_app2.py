import streamlit as st

# 初始化 session_state 以追蹤使用者進度
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.answers = []
    st.session_state.traits = {
        "introvert": 0,  # 內向
        "extrovert": 0,  # 外向
        "proactive": 0,  # 積極
        "cautious": 0,   # 謹慎
        "collaborative": 0,  # 合作
        "independent": 0     # 獨立
    }

# 心理測驗題目資料（無標準答案）
quiz_data = [
    {
        "question": "你更喜歡哪種休閒方式？",
        "options": [
            {"text": "獨自閱讀或看電影", "traits": {"introvert": 1}},
            {"text": "參加朋友聚會或派對", "traits": {"extrovert": 1}},
            {"text": "探索新地方旅行", "traits": {"proactive": 1}},
            {"text": "在家整理或學習新技能", "traits": {"cautious": 1}}
        ]
    },
    {
        "question": "面對職場壓力時，你通常會？",
        "options": [
            {"text": "主動與同事討論解決方案", "traits": {"proactive": 1, "collaborative": 1}},
            {"text": "獨自分析並制定計劃", "traits": {"cautious": 1, "independent": 1}},
            {"text": "參加社交活動放鬆", "traits": {"extrovert": 1}},
            {"text": "尋求主管或專業建議", "traits": {"collaborative": 1}}
        ]
    },
    {
        "question": "你如何開始新項目？",
        "options": [
            {"text": "立即行動，邊做邊學", "traits": {"proactive": 1}},
            {"text": "詳細研究後再開始", "traits": {"cautious": 1}},
            {"text": "與團隊腦力激盪", "traits": {"collaborative": 1}},
            {"text": "獨自規劃所有細節", "traits": {"independent": 1}}
        ]
    },
    {
        "question": "與陌生人初次見面時，你會？",
        "options": [
            {"text": "主動開啟話題", "traits": {"extrovert": 1}},
            {"text": "保持沉默，觀察對方", "traits": {"introvert": 1}},
            {"text": "適度回應，保持禮貌", "traits": {"cautious": 1}},
            {"text": "尋找共同興趣點", "traits": {"collaborative": 1}}
        ]
    },
    {
        "question": "你對失敗的看法是？",
        "options": [
            {"text": "學習的機會", "traits": {"proactive": 1}},
            {"text": "需要謹慎避免", "traits": {"cautious": 1}},
            {"text": "與他人討論改進", "traits": {"collaborative": 1}},
            {"text": "獨自反思原因", "traits": {"independent": 1}}
        ]
    },
    {
        "question": "你偏好的工作環境是？",
        "options": [
            {"text": "充滿挑戰與變化的", "traits": {"proactive": 1}},
            {"text": "穩定且有結構的", "traits": {"cautious": 1}},
            {"text": "團隊合作導向的", "traits": {"collaborative": 1}},
            {"text": "獨立完成任務的", "traits": {"independent": 1}}
        ]
    },
    {
        "question": "如何管理你的時間？",
        "options": [
            {"text": "嚴格遵循日程表", "traits": {"cautious": 1}},
            {"text": "靈活調整優先事項", "traits": {"proactive": 1}},
            {"text": "與同事協調安排", "traits": {"collaborative": 1}},
            {"text": "依個人節奏行事", "traits": {"independent": 1}}
        ]
    },
    {
        "question": "參加團體活動時，你通常？",
        "options": [
            {"text": "積極帶領討論", "traits": {"extrovert": 1, "proactive": 1}},
            {"text": "安靜聆聽意見", "traits": {"introvert": 1}},
            {"text": "提出實用建議", "traits": {"collaborative": 1}},
            {"text": "獨自完成分配任務", "traits": {"independent": 1}}
        ]
    },
    {
        "question": "你對未來的計畫傾向？",
        "options": [
            {"text": "設定長期目標並追求", "traits": {"proactive": 1}},
            {"text": "謹慎評估風險再行動", "traits": {"cautious": 1}},
            {"text": "與他人合作制定計畫", "traits": {"collaborative": 1}},
            {"text": "隨遇而安，保持彈性", "traits": {"independent": 1}}
        ]
    },
    {
        "question": "你如何處理與同事的衝突？",
        "options": [
            {"text": "直接溝通解決", "traits": {"proactive": 1}},
            {"text": "冷靜分析後回應", "traits": {"cautious": 1}},
            {"text": "尋求團隊共識", "traits": {"collaborative": 1}},
            {"text": "獨自調整以避免衝突", "traits": {"independent": 1}}
        ]
    }
]

# 心理分析函數
def analyze_personality(answers, traits):
    # 計算每種特質的分數
    for answer, question in zip(answers, quiz_data):
        for option in question["options"]:
            if option["text"] == answer:
                for trait, value in option["traits"].items():
                    traits[trait] += value
    
    # 確定主導特質
    intro_extro = "外向" if traits["extrovert"] > traits["introvert"] else "內向" if traits["introvert"] > traits["extrovert"] else "內外平衡"
    action_style = "積極" if traits["proactive"] > traits["cautious"] else "謹慎" if traits["cautious"] > traits["proactive"] else "動靜平衡"
    work_style = "合作" if traits["collaborative"] > traits["independent"] else "獨立" if traits["independent"] > traits["collaborative"] else "合作與獨立平衡"
    
    # 生成分析報告
    analysis = f"""

    **社交風格：{intro_extro}**  
    - 您在社交場合中傾向於 {intro_extro.lower()}。  
    - {'外向者擅長建立關係，喜歡與人互動；' if traits["extrovert"] > traits["introvert"] else '內向者享受獨處，擅長深度思考；' if traits["introvert"] > traits["extrovert"] else '您在社交與獨處間保持平衡，適應力強；'}職場中，您{'能快速融入團隊' if traits["extrovert"] > traits["introvert"] else '專注於個人貢獻' if traits["introvert"] > traits["extrovert"] else '能根據情境調整'}。  

    **行動風格：{action_style}**  
    - 您在面對挑戰時傾向於 {action_style.lower()}行事。  
    - {'積極者勇於嘗試新事物，快速行動；' if traits["proactive"] > traits["cautious"] else '謹慎者重視計劃，穩健推進；' if traits["cautious"] > traits["proactive"] else '您在積極與謹慎間找到平衡，靈活應對；'}職場中，您{'擅長抓住機會' if traits["proactive"] > traits["cautious"] else '能有效降低風險' if traits["cautious"] > traits["proactive"] else '能根據需求調整策略'}。  

    **工作風格：{work_style}**  
    - 您在工作中傾向於 {work_style.lower()}模式。  
    - {'合作者重視團隊協作，擅長溝通；' if traits["collaborative"] > traits["independent"] else '獨立者專注個人任務，效率高；' if traits["independent"] > traits["collaborative"] else '您在合作與獨立間靈活切換，適應力強；'}職場中，您{'能促進團隊效率' if traits["collaborative"] > traits["independent"] else '能獨立完成高質量工作' if traits["independent"] > traits["collaborative"] else '能勝任多種角色'}。  

    **建議**  
    - **社交**：{'多參加團體活動，提升影響力' if traits["introvert"] > traits["extrovert"] else '適時享受獨處，平衡精力' if traits["extrovert"] > traits["introvert"] else '繼續保持靈活的社交方式'}。  
    - **行動**：{'偶爾放慢腳步，評估風險' if traits["proactive"] > traits["cautious"] else '適時抓住機會，主動行動' if traits["cautious"] > traits["proactive"] else '保持當前的靈活策略'}。  
    - **工作**：{'嘗試獨立完成任務，提升自信' if traits["collaborative"] > traits["independent"] else '多參與團隊項目，增強協作' if traits["independent"] > traits["collaborative"] else '繼續發揮多面手優勢'}。  
    """
    
    # 答案回顧
    review = "**您的答案回顧：**\n"
    for i, (q, a) in enumerate(zip(quiz_data, answers)):
        review += f"問題 {i+1}: {q['question']} - 您的選擇: {a}\n"
    
    return analysis

# Streamlit 應用程式
st.title("🧠 心理測驗應用程式")
st.write("透過以下測驗，探索您的性格特質與職場風格！")

# 顯示進度
if st.session_state.current_index < len(quiz_data):
    st.progress(st.session_state.current_index / len(quiz_data))
    st.write(f"進度：{st.session_state.current_index + 1} / {len(quiz_data)}")

# 顯示問題
if st.session_state.current_index < len(quiz_data):
    current_question = quiz_data[st.session_state.current_index]
    st.subheader(f"問題 {st.session_state.current_index + 1}: {current_question['question']}")
    options = [opt["text"] for opt in current_question["options"]]
    selected_option = st.radio("請選擇一個選項：", options, key=f"q{st.session_state.current_index}")

    if st.button("提交答案"):
        st.session_state.answers.append(selected_option)
        st.session_state.current_index += 1
        st.rerun()
else:
    st.subheader("🎉 測驗完成！")
    
    # 顯示心理分析
    st.markdown("### 您的心理分析結果")
    analysis = analyze_personality(st.session_state.answers, st.session_state.traits)
    st.markdown(analysis)
    
    # 重新開始按鈕
    if st.button("重新開始測驗"):
        st.session_state.current_index = 0
        st.session_state.answers = []
        st.session_state.traits = {
            "introvert": 0, "extrovert": 0, "proactive": 0,
            "cautious": 0, "collaborative": 0, "independent": 0
        }
        st.rerun()

