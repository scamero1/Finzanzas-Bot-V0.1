from openai import OpenAI
import streamlit as st
msg = []
base = ("Alex es un asistente financiero inteligente diseñado para ayudar a los usuarios a gestionar sus finanzas personales de manera eficiente. Mediante algoritmos avanzados de aprendizaje automático, Alex analiza ingresos, gastos y hábitos de consumo para ofrecer recomendaciones personalizadas y mejorar la toma de decisiones financieras")
client = OpenAI(api_key="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")
st.title("Alex")

if "msg" not in st.session_state:
 st.session_state["msg"] = [{"role":"assistant", "content":"¡Hola! 👋 Soy Alex, tu asistente financiero personal. Estoy aquí para ayudarte a gestionar tu dinero de manera inteligente, optimizar tus gastos y alcanzar tus metas financieras. 💰📊Dime, ¿en qué puedo ayudarte hoy? 🚀"}]

for msg in st.session_state["msg"]:
 st.chat_message(msg["role"]).write(msg["content"])

if userInput:= st.chat_input():
 st.session_state["msg"].append({"role":"user", "content": userInput})
 st.chat_message("user").write(userInput)
 responder = client.responses.create(
  model="gpt-4o-mini",
  store=True,
  instructions=base,
  input= st.session_state["msg"],
  max_output_tokens= 1000,
 )
 respuesta = responder.output_text
 st.session_state["msg"].append({"role":"assistant", "content":responder.output_text})
 st.chat_message("assistant").write(responder.output_text) 
 





