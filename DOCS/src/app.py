import streamlit as st
from services.blob_service import upload_blob
from services.credit_service import analyze_credit_card

def configure_interface():
    st.title("Upload de arquivo DIO - Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])


    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso!")
            credit_card_inf = analyze_credit_card(blob_url)
            show_img_and_val(blob_url, credit_card_inf)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName}")


def show_img_and_val(blob_url, credit_card_inf):
    st.image(blob_url, caption="Imagem enviada!", width="stretch")
    st.write("Resultado da verificação")
    if credit_card_inf and credit_card_inf["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_inf['card_name']}")
        st.write(f"Banco Emissor: {credit_card_inf['bank_name']}")
        st.write(f"Data de Validade: {credit_card_inf['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão inválido</h1>", unsafe_allow_html=True)
        st.write("Cartão inválido")



if __name__ == "__main__":
    configure_interface()