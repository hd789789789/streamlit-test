import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ẩn header và menu của Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def main():
    st.title("Vẽ Biểu Đồ với Streamlit")

    # Nhập dữ liệu
    st.sidebar.header("Nhập dữ liệu")
    num_points = st.sidebar.number_input(
        "Số lượng điểm dữ liệu", min_value=3, max_value=20, value=5)

    categories = [f"Mục {i+1}" for i in range(num_points)]
    values = []

    for cat in categories:
        values.append(st.sidebar.number_input(f"Giá trị cho {cat}", value=10))

    df = pd.DataFrame({"Danh mục": categories, "Giá trị": values})

    # Chọn loại biểu đồ
    chart_type = st.selectbox("Chọn loại biểu đồ", [
                              "Biểu đồ cột", "Biểu đồ đường", "Biểu đồ tròn"])

    # Vẽ biểu đồ
    fig, ax = plt.subplots()

    if chart_type == "Biểu đồ cột":
        sns.barplot(x="Danh mục", y="Giá trị", data=df, ax=ax)
    elif chart_type == "Biểu đồ đường":
        ax.plot(df["Danh mục"], df["Giá trị"], marker='o', linestyle='-')
    elif chart_type == "Biểu đồ tròn":
        ax.pie(df["Giá trị"], labels=df["Danh mục"],
               autopct='%1.1f%%', startangle=90)
        ax.axis("equal")  # Đảm bảo biểu đồ tròn hiển thị đúng tỉ lệ

    st.pyplot(fig)


if __name__ == "__main__":
    main()
