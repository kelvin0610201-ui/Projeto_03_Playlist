import streamlit as st 

generos = {
    'Trap' : {
        'Matuê' : 'https://www.youtube.com/watch?v=ZPcG9PCfagM',
        'Teto' : 'https://www.youtube.com/watch?v=7AlAYttGnAg'
    },
    'Sertanejo' : {
        'Gusttavo Lima' : 'https://www.youtube.com/watch?v=hEBjnXXWgKU',
        'Luan Santana' : 'https://youtu.be/MKY9bmNrSP0?si=dUUtEfwt9NBlQvbQ'
    },
    'Pagode' : {
        'Zeca Pagodinho' : 'https://www.youtube.com/watch?v=oTREAvZbmME',
        'Brunno Gabryel' : 'https://youtu.be/T3Y6RRSDm4o?si=VUMS-Ng05G3pNnKa'
    },
    'Eletronica' : {
        'Alok' : 'https://www.youtube.com/watch?v=JVpTp8IHdEg',
        'Linkin Park' : 'https://youtu.be/kXYiU_JCYtU?si=l07J_kl_V6PUNG69'
    }
}

st.sidebar.title('KMV Musicas')
st.sidebar.image('logo.png')

genero = st.sidebar.selectbox('Selecione um genero musical', generos.keys())
artista = st.sidebar.selectbox('Selecione um artista', generos[genero].keys())

st.title(artista)
video, sobre = st.tabs(['video', 'sobre o artista'])

with video:
    st.video(generos[genero][artista])



with sobre:
    if artista == 'Matuê':
        st.markdown('''
        "Matuê é um cantor e compositor brasileiro, considerado um dos principais "
        "nomes do trap nacional. Ele ganhou grande destaque com o álbum "
        "'Máquina do Tempo' e é cofundador da gravadora 30PRAUM."
        ''')

    elif artista == 'Teto':
        st.markdown('''
        "Teto é um cantor e compositor de trap brasileiro, conhecido como um dos "
        "grandes fenômenos do gênero no país. Ele faz parte da gravadora 30PRAUM "
        "e emplacou diversos sucessos logo no início de sua carreira."
        ''')

    elif artista == 'Gusttavo Lima':
        st.markdown('''
        "Gusttavo Lima é um cantor, compositor e instrumentista brasileiro de música "
        "sertaneja. Conhecido como 'O Embaixador', é um dos artistas mais ouvidos "
        "do país, acumulando recordes de público e acessos."
        ''')

    elif artista == 'Luan Santana':
        st.markdown('''
        "Luan Santana é um cantor e compositor brasileiro de música sertaneja e pop. "
        "Surgiu como um fenômeno jovem nos anos 2010 e se consolidou como um dos "
        "artistas mais premiados e influentes da música brasileira moderna."
        ''')

    elif artista == 'Zeca Pagodinho':
        st.markdown('''
        "Zeca Pagodinho é um cantor e compositor brasileiro, um dos maiores nomes "
        "da história do samba e do pagode. Com décadas de carreira, é conhecido "
        "por seu carisma irreverente e por crônicas musicais do subúrbio carioca."
        ''')

    elif artista == 'Bruno Gabryel':
        st.markdown('''
        "Bruno Gabryel é um cantor e compositor brasileiro da nova geração. "
        "Vem conquistando seu espaço na cena musical com seu estilo único, "
        "criando conexões através de suas letras e melodias marcantes."
        ''')


    elif artista == 'Alok':
                st.markdown('''
            "Alok é um DJ, produtor musical e empresário brasileiro. "
            "ele é um dos artistas de música eletrônica mais conhecidos do mundo "
            "e já se apresentou em diversos festivais internacionais."
        ''')
            
    elif artista == 'Linkin Park':
        st.markdown('''
        "Linkin Park é uma renomada banda de rock norte-americana formada na Califórnia. "
        "Famosos por misturar rock alternativo, nu metal e elementos eletrônicos, "
        "marcaram gerações com álbuns icônicos como 'Hybrid Theory' e 'Meteora'."
        ''')