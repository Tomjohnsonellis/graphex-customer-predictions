import streamlit as st

st.title("Sedora: Securing Sales")

st.header("A warm welcome to you all.")
"We've done things a bit differently today, we hope you enjoy."

st.title("Our goal: Understand what causes our customers to make a purchase.")
st.subheader("With this knowledge, we will be able to make better choices in how we secure sales")
st.markdown("This project was made possible thanks to [Graphext](https://www.graphext.com/), project viewable [here](https://public.graphext.com/dffcd513f605860d/index.html) let's begin.")

st.write("Immediately we found that there is a clear divide in behaviours")
st.image("sale.png")
st.write("Something definitely separates the buyers from the window-shoppers, but what?")
st.write("We'll get the most basic thing out the way, yes, seasons are important. Revolutionary information.")
st.image("annualvolume.png")

st.write("Graphext does some grunt work for us, tries to work out what's important")
st.image("instant.png")
st.write("However, us humans are still needed to make sense out of this.")
st.write("These factors look impressive, but are actually just google analytics stuff, not too useful for us. ")
if st.checkbox("Would you like to learn what some those are?"):
    "Page values: How much revenue is generated by a webpage"
    "Exit rates: How often a particular page is the last one in a browsing session"
    "Bounce rates: How often a user leaves the site (bounces) after viewing a webpage"

st.header("Human Analysis")
st.write("After we looked through the different factors manually we came across these two insights:")
st.write("Out with the old, in with the new")
st.image("loyalty.png")
st.write("If they want it, they want it now")
st.image("attention.png")






st.header("Prediction Accuracy")
st.write("Here's how the model performs when making predictions")
st.image("accuracy.png")

st.header("Thanks for listening, questions?")



