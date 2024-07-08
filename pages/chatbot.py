import streamlit as st
import data.data as dd
import datetime
import time

user_id = st.session_state.user_id
username = st.session_state.username
st.title("AI智能助手😊")
st.subheader(f"欢迎{username}使用")
st.text("这是一个AI助手，可以回答你的任何问题，请尽情使用吧！")

list = dd.query_message_by_user_id(user_id=user_id)
if list:
    for msg in list:
        with st.chat_message(msg["role"]):
            st.write(msg["message"])
else:
    with st.chat_message("assistant"):
        st.write("我是你的智能AI助手，可以回答你的任何问题，请问你有什么问题？")


# 创建一个聊天输入框 接受用户输入的问题
problem = st.chat_input("请输入你的问题")
is_flag = True

ai_message = "ai说：你好，我是你的私人助手"
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


