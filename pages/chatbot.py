import streamlit as st
import data.data as dd
import datetime

import time
st.set_page_config(
    page_title="Register",
    page_icon="😊"
)


user_id = st.session_state.user_id
username = st.session_state.username
st.title('AI问答小助手👏👏👏')
st.subheader(f"欢迎{username}使用")
st.text("这是一个聊天小助手")

problem = st.chat_input("请输入你的问题")

is_flag = True

ai_message = f"ai说：{problem}"
if problem:
    is_flag = False
    time = datetime.datetime.now()
    dd.add_chat_message(user_id,problem,"user",time)
    dd.add_chat_message(user_id, ai_message, "message", time)
    message = dd.query_message_by_id(user_id)
    if message:
        for i in message:
            with st.chat_message(i["role"]):
                st.write(i["message"])
    else:
        with st.chat_message("assistant"):
            st.write("我是你的智能AI助手，可以回答你的任何问题")

result = dd.query_message_by_id(user_id)
if is_flag:
    if result:
        for i in result:
            with st.chat_message(i["role"]):
                st.write(i["message"])
    else:
        with st.chat_message("assistant"):
            st.write("我是你的智能AI助手，可以回答你的任何问题")


