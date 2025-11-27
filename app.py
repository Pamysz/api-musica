import requests
import streamlit as st

def buscar_letra(banda: str, musica: str) -> str:
    try:
        #Tratamento de caracteres na URL
        bandaUrl = requests.utils.quote(banda)
        musicaUrl = requests.utils.quote(musica)

        endpoint = f"https://api.lyrics.ovh/v1/{bandaUrl}/{musicaUrl}"
        #Timeout
        response = requests.get(endpoint, timeout=10)
        if response.status_code == 200:
            return response.json().get("lyrics", "")
        return ""
    
    except requests.exceptions.RequestException:
        return ""
    except Exception:
        return ""
    

#Configuração da aba
st.set_page_config(
    page_title="Buscador de letras",
    page_icon="❤️",
    layout= "centered"
)
#Interface simples
st.image("https://i.pinimg.com/736x/fb/89/23/fb89230aabcce0b3f85d12e45273a869.jpg")
st.title("Veja a letra das suas musicas preferidas!")
st.subheader("Buscar letras")

banda = st.text_input("Digite o nome da banda: ",
                      key="banda_input")
musica = st.text_input("Digite o nome da música",
                       key="musica_input")

pesquisar = st.button("Pesquisar letra", use_container_width=True)


if pesquisar:
    #Tira os espaços
    if banda.strip() and musica.strip():
        with st.spinner("Buscando..."):
         letra_encontrada = buscar_letra(banda, musica)


        if letra_encontrada:
            st.success("Letra encontada :3")
            st.text_area("",
                         letra_encontrada,
                         height=400,
                         disabled=True)
        else:
            st.error("Letra não encontrada :C")

    else:
        st.text("Coloque banda e musica!")
