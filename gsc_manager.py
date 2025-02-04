import streamlit as st
import requests

# Web App URLs for Google Apps Scripts
TOKEN_SCRIPT_WEBHOOK = "https://script.google.com/macros/s/1dl-hkVcgu-Uo8p0QCMYJFSLF3cHYwvVbs6HCLOPrgjZtmgdwF3ZLDkIc/exec"
SHEET_ID_SCRIPT_WEBHOOK = "https://script.google.com/macros/s/1hwQ7J-bT28_pFIvxppARnu6DHOVAUETglIyDmm5teFy16rUU8IjjqEHk/exec"

st.title("🔑 GSC Manager - Tokens & Sheets ID")

# Section 1: Update Access & Refresh Tokens
st.header("🔄 Update GSC Tokens")
access_token = st.text_input("Enter New Access Token", type="password")
refresh_token = st.text_input("Enter New Refresh Token", type="password")

if st.button("Save Tokens"):
    if not access_token or not refresh_token:
        st.error("❌ Please fill in both fields!")
    else:
        token_data = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
        response = requests.post(TOKEN_SCRIPT_WEBHOOK, json=token_data)

        if response.status_code == 200:
            st.success("✅ Tokens Updated Successfully!")
        else:
            st.error(f"❌ Error: {response.text}")

# Section 2: Update Google Sheets ID
st.header("📄 Update Google Sheets ID")
sheet_id = st.text_input("Enter New Google Sheets ID")

if st.button("Save Google Sheets ID"):
    if not sheet_id:
        st.error("❌ Please enter a valid Google Sheets ID!")
    else:
        sheet_data = {
            "sheet_id": sheet_id
        }
        response = requests.post(SHEET_ID_SCRIPT_WEBHOOK, json=sheet_data)

        if response.status_code == 200:
            st.success("✅ Google Sheets ID Updated Successfully!")
        else:
            st.error(f"❌ Error: {response.text}")
