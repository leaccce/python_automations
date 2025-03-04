import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv("expenses.csv")

def categorize(description):
    Food=["grocery","restaurant","food","dining","meal","snack","breakfast","lunch","dinner","brunch","coffee","tea","smoothie","juice","soda","water","alcohol","beer"]
    Housing=["rent","mortgage","utilities","hoa","homeowner","property","home","electricity"]
    Entertainment=["cafe","movie","theater","concert","amusement","park","museum","zoo","aquarium","event","game","nightclub","bar","pub","club","karaoke","bowling","arcade","casino","bet","betting","gambling","lottery","raffle","bingo","dance","party","festival","fair","carnival","parade","circus","comedy"]
    Transportation=["uber","lyft","taxi","cab","bus","train","subway","tram","ferry","trolley","shuttle","car","vehicle","gas","fuel","parking","toll","tollway","tunnel","bridge","road","highway","expressway","freeway","motorway","route","drive","ride","bike","bicycle","motorcycle","scooter","skateboard","rollerblade","skates","skis","snowboard","surfboard","kayak","canoe","raft","paddleboard","paddle","oar","row","sail","sailing","yacht","boat","ship","cruise","airplane","flight","helicopter","balloon","zeppelin","blimp","parachute","paraglide","hang","glide","skydive","bungee","jump","zip","line","zipline","cable","car","gondola","lift","chairlift","ski","lift","escalator","elevator","funicular","monorail","maglev","hyperloop","tax","fare"]
    Personal=["beauty","cosmetics","makeup","skincare","haircare","nail","clothes","cloth","apparel","gym"]
    description = description.lower()
    if any(word in description for word in Food):
        return "Food"
    elif any(word in description for word in Housing):
        return "Housing"
    elif any(word in description for word in Entertainment):
        return "Entertainment"
    elif any(word in description for word in Transportation):
        return "Transportation"
    elif any(word in description for word in Personal):
        return "Personal"
    else:
        return "Other"


df["Category"] = df["Description"].apply(categorize)
print(df)

fig = px.pie(df, values="Amount", names="Category", title="Spending by Category")
fig2 = px.line(df, x="Date", y="Amount", title="Spending Over Time")

st.title("Personal Finance Dashboard")
st.write("Upload your expenses CSV below:")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df["Category"] = df["Description"].apply(categorize)
    
    st.write("Your Expenses:", df)
    st.plotly_chart(fig)  # Pie chart
    st.plotly_chart(fig2) # Line chart