import streamlit as st

def welcome_cont(name, status=False):
    cont = st.empty()
    with cont.container():
        post_add_button, posts_view_button = cont.columns(2)
        if status is str:
            st.write(f"{status}")
        st.write(f"welcome {name} {status}")
        post_add_button = card(
            key=1,
            title="Post new job",
            text="Some description",
            image="https://images.unsplash.com/photo-1487528278747-ba99ed528ebc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80")
        print(post_add_button)
        posts_view_button = card(
            key=2,
            title="Post view",
            text="Some description",
            image="https://source.unsplash.com/random/200x200?sig=1")
    return cont, post_add_button, posts_view_button
