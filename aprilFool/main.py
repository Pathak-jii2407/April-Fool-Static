import streamlit as st
import time


def main():
    st.set_page_config(page_title="GATE CSE Telegram Group", page_icon="🔗")

    if "prank" not in st.session_state:
        st.session_state.prank = False

    st.title("🚀 Join our GATE CSE Telegram Group!")
    st.write("Click the button below to join the exclusive group for GATE CSE preparation.")

    if not st.session_state.prank:
        if st.button("📲 Join Telegram Group"):
            with st.spinner("Redirecting to Telegram..."):
                time.sleep(2)
            st.session_state.prank = True
            st.rerun()
    else:
        st.error("🎉 April Fool Banaya, To Unko Gussa Aya! 😂")
        st.write("Meri Charno Me Aapka Koti Koti Pranam.      ~ Ved")
        st.balloons()



if __name__ == "__main__":
    main()
