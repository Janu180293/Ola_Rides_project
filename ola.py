import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from ola_queries import queries

palette = sns.color_palette("rocket")
# Page configuration
st.set_page_config(
    page_title="OLA Ride Analytics",
    page_icon="🚕",
    layout="wide"
)
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
    }
    h1 {
        font-size: 35px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_resource
def get_connection():
    engine = create_engine(
        "mysql+mysqlconnector://root:7708275323@localhost:3306/ola_project"
    )
    return engine

engine = get_connection()

st.title("🚕 OLA Ride Analytics Dashboard")


# -----------------------------
# LEFT SIDE MENU
# -----------------------------

st.sidebar.title("Menu")

selected_question = st.sidebar.selectbox(
    "Select Question",
    list(queries.keys())
)

option = st.sidebar.radio(
    "Select View",
    [
        "Table",
        "Visualization"
    ]
)


# Get query details

sql_query = queries[selected_question]["sql"]

insight = queries[selected_question]["insight"]

chart_type = queries[selected_question]["chart"]



# Execute SQL

df = pd.read_sql(
    sql_query,
    engine
)



# -----------------------------
# RIGHT SIDE DISPLAY
# -----------------------------


st.subheader(selected_question)

# -----------------------------
# TABLE VIEW
# -----------------------------

if option == "Table":
    try:

        st.subheader("Query Result")
        st.dataframe(
            df.style.set_properties(
                **{
                    "text-align": "left"
                }
            ),
            hide_index=True,
            use_container_width=True
        )
        st.subheader("Insight")
        st.info(insight)
    except Exception as e:
        st.error(str(e))


    # -----------------------------
    # VISUALIZATION VIEW
    # -----------------------------


elif option == "Visualization":
    try:

        st.subheader("Visualization")


        if chart_type == "bar":

            fig, ax = plt.subplots(
                figsize=(8,5)
            )


            sns.barplot(
                data=df,
                x=df.columns[0],
                y=df.columns[1],
                palette=palette,
                ax=ax
            )


            ax.set_title(selected_question)

            plt.xticks(rotation=45)

            st.pyplot(fig)



        elif chart_type == "horizontal_bar":

            fig, ax = plt.subplots(
                figsize=(8,5)
            )


            sns.barplot(
                data=df,
                x=df.columns[1],
                y=df.columns[0],
                ax=ax,
                palette=palette
            )


            ax.set_title(selected_question)


            st.pyplot(fig)



        elif chart_type == "pie":

            fig, ax = plt.subplots(
                figsize=(2,2)
            )


            df.set_index(
                df.columns[0]
            ).plot(
                kind="pie",
                y=df.columns[1],
                autopct='%1.1f%%',
                ax=ax
            )


            ax.set_ylabel("")


            st.pyplot(fig)



        elif chart_type == "kpi":

            value = df.iloc[0,0]

            if selected_question == "1. Retrieve all successful bookings":
                label = "No of successful bookings"
            elif selected_question == "3. Total number of cancelled rides by customers":
                label = "Cancelled rides by customers"
            elif selected_question == "9. Total booking value of successfully completed rides":
                label = "Total booking value"
            

            st.metric(
                label=label,
                value=value,
                border=True
            )
    except Exception as e:
        st.error(str(e))


