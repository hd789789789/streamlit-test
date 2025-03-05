import streamlit as st


def main():
    st.title("Thông tin người sử dụng 1")

    # Nhập thông tin người dùng
    user_name = st.text_input("Nhập tên người dùng:", "Guest")
    user_email = st.text_input("Nhập email:", "guest@example.com")

    st.write(f"### Xin chào, {user_name}!")
    st.write(f"📧 Email: {user_email}")

    # Input tăng giảm số lượng
    quantity = st.number_input(
        "Chọn số lượng:", min_value=0, max_value=100, value=1, step=1)

    st.write(f"Bạn đã chọn số lượng: **{quantity}**")

    # Nút xác nhận
    if st.button("Xác nhận"):
        st.success(
            f"Thông tin đã được lưu: {user_name} - {user_email} - Số lượng: {quantity}")


if __name__ == "__main__":
    main()
