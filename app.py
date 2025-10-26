import streamlit as st
import importlib

# Função para mostar o conteúdo da página selecionada

def show_pages(page_name):
    modules = {
        'Início':'início',
        'Projetos':'projetos',
        'Dashboards':'dashboards',
        'Contato':'contatos'
    }

    module_name = modules.get(page_name)
    if module_name:
        module = importlib.import_module(module_name)

        if hasattr(module, 'run'):
            module.run()
        else:
            st.write("O módulo não tem uma função 'run' para exibir o conteúdo.")
    else:
        st.write('Página não encontrada.')

#criando aba de navegação

page = st.sidebar.selectbox(
    'Navegação',
    ['Início', 'Projetos', 'Dashboards', 'Contato']
)

#resumo

if page == 'Início':
    st.title("Portfólio de dados - Lucas Gabriel")
    st.write("""
    Olá, me chamo Lucas Gabriel. Atualmente sou estudante de Análise e Desenvolvimento de Sistemas e recentemente concluí o programa de formação em análise de dados da Edumi. 

    Minha paixão por essa área começou quando eu estava cursando o ensino médio técnico em informática no IFRN. Em determinado momento, trabalhamos com python e pandas para analisar bases de dados do governo federal, sendo possível extrair insights valiosíssimos sobre, por exemplo, quantas bolsas do PROUni eram disponibilizadas por Estado, Região ou curso. 

    Já no curso da Edumi, trabalhamos com vários cases reais, sendo um deles o da QuintoAndar. A partir da análise de planilhas foi possível obter vários dados, ajudando a identificar, por exemplo, quais tipos de anúncios tinham mais conversão em contratos fechados. Esse projeto me ajudou a entender melhor como estruturar dados para gerar insights de negócio. 

    Um dos cases que mais me deu orgulho até aqui, foi um projeto completo, desde o WebScraping até o ETL e modelagem de dados, geração de relatórios e dashboards utilizando o PowerBi. Utilizando Python e principalmente as biblioteca Requests, Pandas e Matplotlib, extrai os dados sobre câmbio do site do Banco Central e a partir disso, pude responder várias questões, como quais são as 5 maiores instituições de câmbio operando no brasil no ano de 2025 ou a evolução dessas entidades no ranking desde 2014. Me fazendo práticar sobre a coleta, tratamento e análise de grande volumes de dados, além de responder várias dúvidas sobre o mundo dos investimentos e mercado financeiro.
    """)

else:
    show_pages(page)