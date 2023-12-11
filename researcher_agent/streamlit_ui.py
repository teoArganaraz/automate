import streamlit as st
from agent.agent import researcher


def main():
    st.set_page_config(page_title="AI research agent", page_icon=":bird:")
    st.header("AI research agent :bird:")
    
    query = st.text_input("Research goal")
    
    if query:
        st.write("Doing research for ", query)
        result = researcher({"input": query})
        st.info(result['output'])

if __name__ == '__main__':
     main()
