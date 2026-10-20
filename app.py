import streamlit as st

st.set_page_config(page_title="فاز فیدار پارسیان", layout="centered")

st.image("logo.png", width=200)
st.title("شرکت فاز فیدار پارسیان")
st.write("شماره ثبت: ۶۳۳۷۷۳")
st.subheader("خدمات مهندسی و فناوری")

st.divider()

st.write("به شرکت فاز فیدار پارسیان خوش آمدید.")
st.write("ما ارائه دهنده خدمات تخصصی مهندسی در حوزه‌های مختلف هستیم.")

st.divider()

st.header("با ما در ارتباط باشید")
name = st.text_input("نام و نام خانوادگی")
phone = st.text_input("شماره تماس")

if st.button("ارسال درخواست"):
    if name and phone:
        st.success("سپاسگزاریم! درخواست شما ثبت شد و به‌زودی با شما تماس خواهیم گرفت.")
    else:
        st.error("لطفاً نام و شماره تماس خود را وارد کنید.")

st.divider()

st.info("فاز فیدار پارسیان | برای اطلاعات بیشتر با ما تماس بگیرید")
