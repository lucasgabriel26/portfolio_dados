import streamlit as st

def run():
    st.subheader('Contato')

    st.write("Vamos nos conectar?")

    # LinkedIn
    linkedin_url = "https://www.linkedin.com/in/lucasgpin/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24"/> LinkedIn: @Lucas Gabriel</a>', unsafe_allow_html=True)

    # Instagram
    instagram_url = "https://www.instagram.com/lucasgabr.el/"
    st.markdown(f'<a href="{instagram_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174855.png" width="24"/> Instagram: @lucasgabr.el</a>', unsafe_allow_html=True)

    # GitHub
    github_url = "https://github.com/lucasgabriel26"
    st.markdown(f'<a href="{github_url}" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733609.png" width="24"/> GitHub: @lucasgabriel26</a>', unsafe_allow_html=True)
