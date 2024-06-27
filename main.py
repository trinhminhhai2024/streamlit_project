import streamlit as st
st.title("How are you")
st.header("Hello Kitty")
st.subheader("Hello Puppy")
st.text("Hello Pony")
st.divider()
st.markdown("heading 1")
st.markdown("Can you tell me more?")
st.markdown("# Heading 1")
st.markdown("[AI VIETNAM](https://aivietnam.edu.vn/)")
st.markdown("""
         1. Machine Learning
         2. Deep Learning
         """)
st.markdown("$\sqrt{2x+2}$")
st.divider()
st.latex("\sqrt{4x+5}")
st.markdown("$\sqrt{3x+2}$")
st.latex("\sqrt{2x+2}")
st.divider()
st.write("I don't like you")
st.write('## Heading 1')
st.write('$ \sqrt{2x+1} $')
st.write('1+1 =', 2)
st.logo('sources/Vinatek Logo.png')
st.divider()
st.code("""
        def hello():
            print("Hello World")
        """, language='python'
        )
st.image('sources/DSCF0920.JPG')
st.audio('sources/02 第2套.mp3')
st.video('sources/Sylomer demo 1.mp4')
st.divider()
st.write("Hello Bear")
st.write("Hello Princess")
st.write("Hello vietnam")
st.write("Hello World")