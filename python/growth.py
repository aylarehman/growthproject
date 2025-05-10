import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="★")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to your growth journey")
st.write("Growth is not about speed, but about steady steps—each challenge faced, every lesson learned, and every setback overcome brings you closer to becoming the person you're meant to be. Keep pushing forward!")

# Quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts.—Winston Churchill")

# Challenge input
st.header("What's your challenge today?")
user_input = st.text_input("Describe the challenge you are facing:")

# Condition for user input
if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("⚡Tell us about your challenge to get started.")

# Reflecting section (fixed indentation)
st.header("Reflect on your learning")
reflection = st.text_area("Write your reflections here:")

# Condition for reflection input
if reflection:
    st.success("🚀Great insight! Success is not just reaching the peak, but embracing the climb that got you there. 🚀")
else:
    st.info("Reflection on past experience help you to grow! Share your difficulties")


# Achievements 
st.header("Celebrate your wins!🎉🏅")
achievement =st.success("💪Share something you have recently accomplished:{achievement}")

if achievement:
      st.success(f"🏆Amazing! you achieved:{achievement}")


else:
      st.info("Big or small, every achievement counts!😊🔥")

      # Footer
st.write("- - -")
st.write("🚀Keep believing in yourself. Grwoth is a journey , not a destination!")
st.write("©️ Created by Ayla Rehman **")
