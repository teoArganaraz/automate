import streamlit as st
from agent.serp_integration import search
from agent.agent import find_relevant_articles_urls, get_content_from_urls, generate_summary, generate_post


def main():
    st.set_page_config(page_title = "Autonomus Researcher - Social Media Post", page_icon=":writing_hand:")
    query = st.text_input("Topic of Twitter Thread")

    if query:
        print(query)
        st.write("Generating Social Media post for: ", query)

        search_results = search(query)
        urls = find_relevant_articles_urls(search_results,query)
        data = get_content_from_urls(urls)
        summaries = generate_summary(data,query)
        post = generate_post(summaries,query)

        with st.expander("Search results:"):
            st.info(search_results)
        with st.expander("Best urls:"):
            st.info(urls)
        with st.expander("Data:"):
            st.info(data)
        with st.expander("Summaries:"):
            st.info(summaries)
        with st.expander("Generated Post:"):
            st.info(post)


if __name__ == "__main__":
    main()
