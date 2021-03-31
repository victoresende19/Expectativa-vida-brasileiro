# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("Life_Expectancy_Data.csv")

df.columns = ['Pais', 'Ano', 'Status', 'Expectativa_de_vida', 'Mortalidade_adulta',
                  'Mortes_infantis', 'Alcool', 'Porcentagem_de_gastos', 'Hepatite_B',
                  'Sarampo', 'IMC', 'Menores_de_cinco_anos', 'Poliomielite', 'Despesas_totais',
                  'Difteria', 'HIV_AIDS', 'PIB', 'Populacao',
                  'Magreza_1-19_anos', 'Magreza_5-9_anos',
                  'Composicao_da_renda_dos_recursos', 'Escolaridade']

df = df[(df['Pais']=='Brazil')]
#df["Alcool"] = df["Alcool"].fillna(df["Alcool"].mean())
#df["Despesas_totais"] = df["Despesas_totais"].fillna(df["Despesas_totais"].mean())
#print(df.isna().sum())



#-X = df[['Alcool', 'Escolaridade', 'Despesas_totais', 'PIB']]
#print(X.shape)

#-Y = df['Expectativa_de_vida']
#print(Y.shape)
#-model = LinearRegression() #criando a variavel pra usar reg linear

#-X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=1) #separando os dados para treino e teste
#-model.fit(X_train, Y_train)#treinando o modelo

#model.intercept_.round(2) #acessando a interceptacao da funcao (b)
#model.coef_.round(2) #acessando a inclinacao da curva da funcao (m)


#-y_test_predicted = model.predict(X_test)
#-y_test_predicted.shape
#print(type(y_test_predicted))
#print(y_test_predicted)

print(df.info())


#print("MSE: {}".format(mean_squared_error(Y_test, y_test_predicted)))
#print(model.score(X_test, Y_test))

st.sidebar.title('Menu')
paginaSelecionada  = st.sidebar.selectbox('Selecione a pagina', ['Projeto CRISP-DM', 'Entendimento de Negócio', 'Entendimento dos Dados', 'Preparação dos Dados', 'Modelagem', 'Avaliação', 'Implementação'])

if paginaSelecionada == 'Projeto CRISP-DM':
    st.markdown("<h1 style='text-align: center; color: black;'>Expectativa de vida</h1>", unsafe_allow_html=True)
    st.write("<p align='justify'> A expectativa de vida é um fator muito importante em projeções para um determinado país. Com ela é possível verificar, por exemplo, quando os cidadãos estarão em idade ativa para trabalhar. É possível também verificar um determinado período do qual o governo deverá investir mais dinheiro no setor da saúde em decorrência de uma possível grande taxa de envelhecimento da população.  <p align='justify'>", unsafe_allow_html=True) 
    st.image("expectativa de vida.png", width = 725, caption='Figura 01: Expectativa de vida')
    st.write("<p align='justify'> A Organização Mundial da Saúde (OMS) disponibilizou um conjunto de dados do estado de saúde de todos os países correspondente aos anos de 2000 a 2015. O repositório do Global Health Observatory da OMS monitora o status da saúde e muitos outros fatores relacionados a todos os países. Os conjuntos de dados são disponibilizados ao público para fins de análise de dados em saúde. <p align='justify'>", unsafe_allow_html=True)    
    st.write("<p align='justify'> O conjunto de dados relacionado à expectativa de vida e aos fatores de saúde de 193 países foi coletado no mesmo site de repositório de dados da OMS e seus dados econômicos correspondentes foram coletados no site das Nações Unidas. Entre todas as categorias de fatores relacionados à saúde, foram escolhidos apenas os fatores críticos que são mais representativos. <p align='justify'>", unsafe_allow_html=True) 
    st.write("<p align='justify'> Dessa maneira, visando explorar a perspectiva brasileira, esse estudo abordará fatores que podem ter impactado a perspectiva de vida da população brasileira nesses 15 anos de coleta de dados. Por meio de artifícios estatísticos, matemáticos e computacionais, será analisada cada variável e sua relação com a expectativa de vida, juntamente com análises sobre estilo de vida e fatores sobre enfermidade dos brasileiros. <p align='justify'>", unsafe_allow_html=True) 

    
    st.markdown("<h1 style='text-align: center; color: black;'>Metodologia CRISP-DM</h1>", unsafe_allow_html=True)
    st.write("<p align='justify'> Com o passar dos anos o avanço tecnólogico foi eminente, tal ascensão fez com o que o volume dos dados crescesse de maneira astrônomica. Sendo assim, armazenar tais dados se tornou uma tarefa vital. Com isso, a mineração de dados entra como principal atuante para extrair informações dos dados armazenados, aplicando algoritmos ou ferramenta em tal ambiente. Entretanto, como em todo processo, a mineração de dados precisa solucionar problemas por meio de diagnósticos, análises e planejamento. <p align='justify'>", unsafe_allow_html=True)
    st.write("<p align='justify'> Visando isso, o CRISP-DM entra como principal metodologia para a aplicação da mineração dos dados. O CRISP-DM (Cross Industry Standard Process for Data Mining) abrange diversas fases para concluir um projeto que envolva a mineração dos dados. Tais etapas são: 1 - Entendimento do negócio (Business Understanding), 2 - Entendimento dos dados (Data Understanding), 3 - Preparação dos dados (Data Preparation), 4 - Modelagem (Modeling), 5 - Avaliação (Evaluation), 6 - Implementação (Deployment).<p align='justify'>", unsafe_allow_html=True)
    st.image("CRISPDM.png", width = 725, caption='Figura 02: Etapas metodologia CRISP-DM')
    st.write("<p align='justify'> Dessa maneira, esse projeto irá abordar todas as etapas presente na metodologia CRISP-DM referente a cada um dos seis tópicos presentes. Para acessar cada fase, basta selecioná-las no canto superior esquerdo.<p align='justify'>", unsafe_allow_html=True) 
    
    
    #st.write("<p align='justify'> texto <p align='justify'>", unsafe_allow_html=True) 
    
elif paginaSelecionada == 'Entendimento de Negócio':
    st.markdown("<h1 style='text-align: center; color: black;'>Entendimento de Negócios</h1>", unsafe_allow_html=True)
    st.write("<p align='justify'> A etapa de entendimento de negócio é considerada crucial para essa metodologia, pois nessa fase serão feitas perguntas de negócios à fim de guiar o projeto, por meio dos objetivos, e requisitos necessários para a conclusão do projeto em uma perspectiva de negócios, servindo então como a criação de um plano para atingir os objetivos presente na pergunta de negócio.  <p align='justify'>", unsafe_allow_html=True) 
    st.image("business.png", width = 725, caption='Figura 03: Entendimento de negócio')
    st.write("<p align='justify'> A fim de entender a realidade brasileira em relação aos fatores de imunização, mortalidade, econômicos e sociais, dedicou-se a criação de perguntas norteadoras da qual serão abordadas posteriormente em análises exploratóriase guiadas por estudos estatísticos e computacionais, por meio de linguagens de programação. Sendo assim, gerou-se a seguinte pergunta norteadora: <p align='justify'>", unsafe_allow_html=True)
    st.write("<p align='justify'><ul><li><b> Pergunta de negócios: </b> Quais são as fatores de previsão que realmente afetam positivamente a expectativa de vida da nação brasileira? Com base nisso, é possível criar algum modelo que possa prever a expectativa de vida levando em consideração tais fatores? <p align='justify'> </ul>", unsafe_allow_html=True)      
    st.write("<p align='justify'> Sendo assim, após descobrir os fatores que mais interferem na expectativa de vida, o objetivo será criar um modelo de regressão linear multivariada que possa prever a expectativa de vida da população brasileira levando em consideração os respectivos fatores. <p align='justify'>", unsafe_allow_html=True) 
    st.write("<p align='justify'> Finalmente, após criada o modelo para previsão da expectativa de vida, o mesmo será avaliado por métricas que tentem calcular o erro da regressão aplicada, como por exemplo o cálculo MSE e MAE, sendo ideal valores entre 0.5 e 3.  <p align='justify'>", unsafe_allow_html=True) 
    
    #st.write("<p align='justify'> texto <p align='justify'>", unsafe_allow_html=True) 
    
elif paginaSelecionada == 'Entendimento dos Dados':
    st.markdown("<h1 style='text-align: center; color: black;'>Entendimento dos Dados</h1>", unsafe_allow_html=True)
    st.write("<p align='justify'> Essa etapa da metodologia consiste em organizar e documentar os dados disponíveis para a confecção do projeto. Sendo assim, ao final dessa fase, os dados devem estar documentados, bem como as características desses. <p align='justify'>", unsafe_allow_html=True) 
    st.write("""<p align='justify'> Os tópicos encontrados nessa etapa são: 
             <ul>
             <li> Dicionário dos dados </li>
             <li> Propriedades dos dados </li>
             <li> Explorando a base de dados </li>
             <li> Matriz de correlação </li>
             </ul><p align='justify'>""", unsafe_allow_html=True) 
    
    st.title('Dicionário dos dados')
    st.write("<p align='justify'> O dicionário de dados visa explicar as variáveis presentes na base de dados abordada neste projeto. Dessa maneira, para facilitar o trabalho de exploração de dados, decidiu-se traduzir o nome das variáveis, que originalmente vieram em inglês, para a língua portuguesa. Portanto, a base de dados detêm as seguintes variáveis: <p align='justify'>", unsafe_allow_html=True)
    st.write(""" <p align='justify'>
    <ul>
    <li> <b>País: </b>País analisado.</li>
    <li> <b>Ano: </b>Ano de avaliação.</li>
    <li> <b>Status: </b>Status de desenvolvimento do país, sendo desenvolvido ou em desenvolvimento.</li>
    <li> <b>Expectativa de vida: </b>Expectativa de vida em determinado ano.</li>
    <li> <b>Mortalidade Adulta: </b>Taxas de mortalidade de adultos de ambos os sexos.</li>
    <li> <b>Mortes Infantis: </b>Número de mortes infantis por 1000 habitantes.</li>
    <li> <b>Álcool: </b>Consumo per capito de álcool em litros de álcool puro.</li>
    <li> <b>Porcentagens de gastos: </b>Gastos com saúde sendo uma porcentagem do Produto Interno Bruto per capita (%).</li>
    <li> <b>Hepatite B: </b>Cobertura de imunização contra hepatite B (Hep.B) entre crianças de 1 ano (%).</li>
    <li> <b>Sarampo: </b>Número de casos notificados por 1000 habitantes.</li>
    <li> <b>IMC: </b>Índice de massa corporal médio de toda a população.</li>
    <li> <b>Menores de cinco anos: </b>Número de mortes de menores de cinco anos por 1000 habitantes.</li>
    <li> <b>Poliomelite: </b>Cobertura de imunização contra poliomielite (Pol.3) entre crianças de 1 ano (%).</li>
    <li> <b>Despesas totais: </b>Gastos do governo geral com saúde sendo uma porcentagem dos gastos totais do governo (%).</li>
    <li> <b>Difteria: </b>Cobertura de imunização de toxoide tetânico diftérico e coqueluche (DTP.3) entre crianças de 1 ano de idade (%).</li>
    <li> <b>HIV AIDS: </b>Mortes por 1.000 nascidos vivos HIV por AIDS (0-4 anos).</li>
    <li> <b>PIB: </b>Produto interno bruto per capita (em dólares americanos).</li>
    <li> <b>Populacao: </b>População do país determinado.</li>
    <li> <b>Magreza 1-19 anos: </b>Predominância de magreza entre crianças e adolescentes de 10 a 19 anos (%).</li>
    <li> <b>Magreza 5-9 anos: </b>Predominância de magreza entre crianças de 5 a 9 anos (em %).</li>
    <li> <b>Composicao da renda dos recursos: </b>Índice de Desenvolvimento Humano em termos de composição da renda dos recursos (índice que varia de 0 a 1).</li>
    <li> <b>Escolaridade: </b>Número de anos de escolaridade (em anos).<p align='justify'>
    </ul>""", unsafe_allow_html=True)

    st.title('Propriedades da base de dados')
    st.write("<p align='justify'> Afim de entender mais específicamente a base de dados, tornou-se necessário acessar as propriedades da mesma para observar alguns fatores de maneira inicial. <p align='justify'>", unsafe_allow_html=True)
    st.image("propriedades.png", width = 725, caption='Figura 04: Propriedades base de dados')
    st.write("<p align='justify'> Como explicado anteriormente, os dados foram coletados dos anos de 2000 até 2015, ou seja, 16 anos de coleta (Pois iniciou-se em 2000). Sendo assim, cada varíavel deveria possuir 16 observações, porém observando a figura 05, tal acontecimento não ocorre apenas para as variáveis 'Alcool' e 'Despesas Totais', que aparecem apenas com 15 observações. Sendo assim, apenas duas variáveis da base de dados apresentam valores ausentes. <p align='justify'>", unsafe_allow_html=True)
    st.title('Explorando a base de dados')
    st.write("<p align='justify'> Com o intuito de familiarizar ainda mais com os dados presentes na base de dados disponível, será feita uma breve análise exploratória para tal. Essa análise contará com artificios estatísticos e computacionais presente na linguagem Python. <p align='justify'>", unsafe_allow_html=True) 
    
    st.write("<p align='justify'> Assim sendo, para avaliar as variáveis númericas presente na base de dados, será feita uma breve investigação sobre as propriedades de estatística descritiva que cabem a cada variável:  <p align='justify'>", unsafe_allow_html=True) 
    st.write(df.describe())
    st.write("<p align='justify'> É possível perceber que a média de expectativa de vida da nação brasileira, do período dos anos de 2000 até 2015, foi de 73 anos, sendo o menor valor igual à 71 anos. Em relação à mortes infantís, a média foi de 68 crianças mortas a cada 1.000 brasileiro em todos os anos, o menor e o maior valor para essa variável foi respectivamente 42 e 111 crianças mortas a cada 1.000 brasileiros. Já em relação à escolaridade, o brasileiro em média passou 14 anos estudando, durante tal período.  <p align='justify'>", unsafe_allow_html=True) 
    
    st.write("<p align='justify'> Como sugerido anteriormente (Propriedades dos dados), será verificado a existência de dados faltantes para as variáveis 'Alcool' e 'Despesas_Totais': <p align='justify'>", unsafe_allow_html=True) 
    st.write(df.isna().sum())
    st.write("<p align='justify'> Portanto, concluí-se a existência de apenas 1 observação faltante para a variável 'Alcool' e 'Despesas_Totais', sendo necessário, possivelmente no futuro, o tratamento desse respectivo problema encontrado.<p align='justify'>", unsafe_allow_html=True) 
    
    st.write("<p align='justify'> Nesse momento, com intuito de tornar a visualização da análise exploratória mais visual, serão feitas análises por meio de gráficos gerados sobre os dados da base de dados, gráficos esses que tem como objetivo investigar os dados para o melhor entendimentos destes. <p align='justify'>", unsafe_allow_html=True) 
    
    st.header('Expectativa de vida')
    st.write("<p align='justify'> Sendo assim, avaliando a distribuição das observações presente na variável expectativa de vida por ano, tem-se o seguinte gráfico: <p align='justify'>", unsafe_allow_html=True) 
    sct = plt.figure()
    sns.scatterplot(x='Ano', y='Expectativa_de_vida', data=df)
    st.pyplot(sct)
    st.write("<p align='justify'> Pode-se perceber que, de maneira majoritária, ao passar os anos, a expectativa de vida dos brasileiros foi aumentando gradativamente, o que pode ser considerado um bom indicador de evolução para um país. Tal gráfico também pode acusar uma correlação positiva entre as variáveis, algo que será avaliado posteriormente. <p align='justify'>", unsafe_allow_html=True)
    
    st.header('Mortes Infantís')    
    st.write("<p align='justify'> Como o escopo do projeto é avaliar variáveis que impactam positivamente à expectativa de vida, será avaliado a variáção das observações para a variável Mortes Infantís com intuito de descartar tal variável. Então gerou-se o seguinte boxplot: <p align='justify'>", unsafe_allow_html=True) 
    sct_mtInfBX = plt.figure()
    sns.boxplot(x='Mortes_infantis', data=df, orient='h')
    st.pyplot(sct_mtInfBX)
    st.write("<p align='justify'> Visualizando o boxplot, entende-se que o número de mortes de crianças a cada 1.000 brasileiros se concentrou no valor entre 50 à 83 mortes. No período da coleta dos dados, metade dos anos avaliados tiveram valores para tal variável menores ou igual à 63 mortes de crianças a cada 1.000 brasileiros. <p align='justify'>", unsafe_allow_html=True) 
    st.write("<p align='justify'> Com intuito de ter noção sobre a correlação da variável mortes intantís com a expectativa de vida, desenvolveu-se tal gráfico: <p align='justify'>", unsafe_allow_html=True) 
    sct_mtInfSct = plt.figure()
    sns.scatterplot(x='Expectativa_de_vida', y='Mortes_infantis', data=df)
    st.pyplot(sct_mtInfSct)
    st.write("<p align='justify'> É possível perceber que, quando o número de mortes intantis a cada 1.000 brasileiros é alto, a expectativa de vida da nação brasileira apresenta-se baixa, indicando uma correlação negativa, que será confirmado posteriormente. Dessa maneira, possívelmente essa variável não se encaixará no modelo de regressão, uma vez que o escopo do projeto prevê apenas variáveis que impactem positivamente na expectativa de vida.<p align='justify'>", unsafe_allow_html=True)     
    
    
    st.header('Escolaridade')
    st.write("<p align='justify'> A escolaridade é um dos fatores que, de acordo com estudos, mais impacta positivamente à expectativa de vida de uma população. Dessa maneira, a quantidade de anos de estudo por ano da população brasileira se desenvolve no seguinte gráfico: <p align='justify'>", unsafe_allow_html=True) 
    sct_Esc = plt.figure()
    sns.scatterplot(x='Ano', y='Escolaridade', data=df)
    st.pyplot(sct_Esc)
    st.write("<p align='justify'> É possível concluir variáções de tendência dos dados. No período de 2000 até 2003 a nação brasileira parecia estar aumentando gradativamente os anos de estudos, porém de 2004 até 2008 essa evolução decaiu-se ano à ano, voltando a crescer apenas em 2009, porém de maneira mais tímida. E então alcançou-se os melhores valores apenas em 2014 e 2015. <p align='justify'>", unsafe_allow_html=True) 
    st.write("<p align='justify'> Avaliando o impacto dos anos de estudo na expectativa de vida, tem-se o gráfico: <p align='justify'>", unsafe_allow_html=True) 
    sct_EstExp = plt.figure()
    sns.scatterplot(x='Escolaridade', y='Expectativa_de_vida', data=df)
    st.pyplot(sct_EstExp)
    st.write("<p align='justify'> Observando o gráfico anterior concluí-se que não há uma tendência linear tão clara como esperado entre os dados de tais variáveis, porém a correlação entre tais será avaliada posteriormente para confirmar tal hipótese. <p align='justify'>", unsafe_allow_html=True) 
    
    #st.write("<p align='justify'> texto <p align='justify'>", unsafe_allow_html=True) 
    
    st.header('Matriz de Correlação')
    st.write("<p align='justify'> A avaliação da correlação entre as variáveis pode ser considerada um dos processos mais importantes na escolha das variáveis que irão alimentar o modelo de regressão. Tal análise mostra-se muito eficiente para descobrir o impacto, seja positivo ou negativo, de um fator em relação aos outros presentes na base de dados. Assim sendo, a matriz de correlação para a base de dados do projeto é dada por: <p align='justify'>", unsafe_allow_html=True)     
    st.image("matriz_corre.png", width=None, caption='Figura 05: Matriz de correlação')
    st.write("<p align='justify'> Para uma melhor compreensão do leitor, de acordo com Karl Pearson a correlação de variáveis entre si varia de -1 a 1, podendo ser considerada uma correlação positiva quando aproximado ou igual à 1, correlação negativa quanto aproximado ou igual à -1 e correlação neutra entre as variáveis quando igual à 0. <p align='justify'>", unsafe_allow_html=True) 
    st.write("<p align='justify'> Então, após avaliação na exploração dos dados, pode-se comfirmar que a variável mortes intantis possui correlação negativa em relação à expectativa de vida. Sendo assim, a mesma não será levada em consideração para o modelo de regressão, uma vez que ela impacta negativamente. <p align='justify'>", unsafe_allow_html=True) 
    st.write("<p align='justify'> Já, em relação à escolaridade, a correlação com a expectativa de vida foi de 0.11, o que pode ser considerada uma correlação positiva, porém fraca. Sendo assim, como cogitado anteriormente, a correlação da escolaridade com a expectativa de vida não possuí caráter neutro. <p align='justify'>", unsafe_allow_html=True) 
    st.write("<p align='justify'> Por fim, um fator curioso é a correlação do alcool com a expectativa de vida, a correlação entre as duas variáveis é de caráter positivo forte igual à 0.7. Tal fenomêno pode ser explicado pois, a correlação do alcool com o PIB também é positivamente forte (sendo igual à 0.77), o que faz sentido, pois quando a população possui dinheiro, muitas pessoas decidem por gastar com lazer, ou seja, o alcool. Da mesma maneira, o PIB também possui boa correlação com a expectativa de vida. Portanto, as três variáveis possuem correlação positivamente forte entre si. <p align='justify'>", unsafe_allow_html=True)   
    
    st.write("<p align='justify'> Portanto, após a exploração dos dados via estatística descritiva, gráficos e análise de correlação, concluí-se a etapa de entendimento dos dados, podendo seguir para fase de Preparação dos dados. <p align='justify'>", unsafe_allow_html=True) 
    
elif paginaSelecionada == 'Preparação dos Dados':
    st.markdown("<h1 style='text-align: center; color: black;'>Preparação dos Dados</h1>", unsafe_allow_html=True)
    st.write("<p align='justify'> A etapa de preparação dos dados consiste em preparar os dados para a aplicação da modelagem no futuro. Sendo assim, nessa etapa serão aplicados, caso necessário, a seleção, limpeza, construção e integração dos dados. Entretanto, visando o escopo do projeto, será aplicada apenas a seleção e limpeza dos dados.  <p align='justify'>", unsafe_allow_html=True) 
    st.header('Seleção dos dados')
    st.write("<p align='justify'> Nesse tópico serão selecionadas as variáveis que possivelmente irão alimentar a modelagem, ou seja, dados que relevantes para o modelo. <p align='justify'>", unsafe_allow_html=True) 
    
    st.write("<p align='justify'> Com intuito de selecionar as variáveis que impactam positivamente a expecativa de vida, e, como avaliado anteriormente, a correlação das variáveis se desenvolve como visto na seguinte imagem: <p align='justify'>", unsafe_allow_html=True) 
    st.image("matriz_corre.png", width=None, caption='Figura 06: Matriz de correlação')
    st.write("""<p align='justify'> Portanto, as variáveis que possuem correlação positiva, ou seja, impactam positivamente a expectativa de vida e que fazem sentido para o projeto, são:
             <ul>
             <li> Alcool </li>
             <li> Despesas Totais  </li>
             <li> PIB </li>
             <li> Escolaridade </li>
             </ul> 
             <p align='justify'>""", unsafe_allow_html=True)
             
    df = df[['Alcool', 'Despesas_totais', 'PIB', 'Escolaridade']]
    
    st.write("<p align='justify'> Então, após a seleção dos dados ser concluída, a base de dados molda-se da seguinte maneira, (Sendo apenas uma amostra das cinco últimas observações de cada variável selecionada): <p align='justify'>", unsafe_allow_html=True)  
    st.write(df.head(5))
             
    st.header('Limpeza dos dados')
    st.write("<p align='justify'> A etapa de limpeza dos dados se desenvolve por limpar, caso necessário, as variáveis selecionadas para aplicar posteriormente no modelo do projeto, ou seja, o modelo de regrssão. <p align='justify'>", unsafe_allow_html=True) 
    st.write("<p align='justify'> Como avaliado na fase de entendimento dos dados, as únicas variáveis que possuem dados faltantes são: Alcool e Despesas Totais. Dessa maneira, como as mesmas possuem apenas uma observação faltante, será preenchido com a média total da respectiva variável. Sendo assim, após preencher os dados faltantes com as respectivas médias, é possível avaliá-las novamente: <p align='justify'>", unsafe_allow_html=True)
    df["Alcool"] = df["Alcool"].fillna(df["Alcool"].mean())
    df["Despesas_totais"] = df["Despesas_totais"].fillna(df["Despesas_totais"].mean())
    st.write(df.isna().sum())
    #st.write("<p align='justify'> texto <p align='justify'>", unsafe_allow_html=True)     
    
    st.write("<p align='justify'> Portanto a fase de preparação dos dados está concluída, uma vez que a etapa de seleção e limpeza dos dados foram finalizadas. Sendo assim, agora será aplicado o modelo de previsão por meio de regressão multivariada no próximo tópico: Modelagem. <p align='justify'>", unsafe_allow_html=True)
    
elif paginaSelecionada == 'Modelagem':
    st.markdown("<h1 style='text-align: center; color: black;'>Modelagem</h1>", unsafe_allow_html=True)    
    st.write("<p align='justify'> A etapa de modelagem dos dados tem como entregue a escolha e a construção do algorítmo visando resolver a questão discutida inicialmente na etapa de entendimento do negócio. <p align='justify'>", unsafe_allow_html=True) 
    st.write("<p align='justify'> Portanto, nesse projeto será utilizado o modelo de regressão linear múltipla, pois o objetivo do projeto é prever um valor para expectativa de vida usando variáveis que possam impactar positivamente. A aplicação da regressão multivariada será feita por meio do software Python usando principalmente a biblioteca scikit-learn. <p align='justify'>", unsafe_allow_html=True)  
    st.write("""<p align='justify'> Os tópicos encontrados nessa etapa são: 
         <ul>
         <li> Regressão Linear Múltipla </li>
         <li> Scikit-learn </li>
         <li> Modelo de Regressão Linear Múltipla </li>
         </ul><p align='justify'>""", unsafe_allow_html=True) 
         
    st.header('Regressão Linear Múltipla')
    st.write("<p align='justify'> Regressão múltipla é uma coleção de técnicas estatísticas para construir modelos que descrevem de maneira razoável relações entre várias variáveis explicativas de um determinado processo. Ou seja, de maneira simples, o modelo de regressão faz a atribuição de um valor contínuo a um elemento. <p align='justify'>", unsafe_allow_html=True)      
    st.write('O modelo estatístico para a regressão multivariada é representada pela seguinte fórmula:')
    
    st.latex('Yi=β0+β1xi1+β2xi2+...+βpxip+ϵi,   i=1,...,n,')
    
    st.write("""<p align='justify'> <ul> 
         <li> Sendo x valores das variáveis explicativas, ou seja, constantes </li>
         <li> Sendo β os parâmetros ou coeficientes de regressão </li> 
         <li> Sendo ϵi erros aleatórios independentes </li>
         </ul> <p align='justify'>""", unsafe_allow_html=True)
    
    st.write("<p align='justify'> E então pode ser convertido em um vetor: <p align='justify'>", unsafe_allow_html=True)
    st.latex('Y = Xb + e')
    
    st.header('Previsão Expectativa de vida - Scikit-learn')
    st.write("<p align='justify'> A biblioteca Scikit-learn é uma das principais bibliotecas na linguagem python para machine learning. Nela, é possível encontrar ferramentas simples e extremamente eficientes para análises preditivas, como regressões por exemplo.  <p align='justify'>", unsafe_allow_html=True)     
    st.write("<p align='justify'> Dessa maneira, será necessário trabalhar com as variáveis independentes que são as escolhidas para o modelo: Alcool, Despesas Totais, PIB e Escolaridade para prever um valor contínuo da expectativa de vida. Sendo assim, os dados necessitam ser separados em treino e teste para no futuro seja avaliada a regressão. Portanto, a base de dados, será separa em 70% treino e 30% para os posteriores testes(Erro médio quadrático e Erro médio Absoluto). <p align='justify'>", unsafe_allow_html=True) 
    
    
    st.header('Modelo de Regressão Linear Múltipla')
    st.write("<p align='justify'> Portanto será separada como variável X as variáveis independentes (preditoras) e variável Y a variável dependente (alvo): <p align='justify'>", unsafe_allow_html=True)  
    df["Alcool"] = df["Alcool"].fillna(df["Alcool"].mean())
    df["Despesas_totais"] = df["Despesas_totais"].fillna(df["Despesas_totais"].mean())
    
    
    st.write('Variáveis Independentes (X):')
    X = df[['Alcool', 'Escolaridade', 'Despesas_totais', 'PIB']]
    st.write(X)

    st.write('Variável Dependente (Y):')
    Y = df['Expectativa_de_vida']
    st.write(Y)
    
    
    st.write("<p align='justify'> Consequentemente, agora os dados serão separados em treino e teste, tanto para X quanto para Y. Como explicado anteriormente, o modelo utilizado nesse projeto será separado em 70% dos dados para treino e 30% dos dados para testar o modelo em si. <p align='justify'>", unsafe_allow_html=True)      
    
    model = LinearRegression() #criando a variavel pra usar reg linear
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=1) #separando os dados para treino e teste
    
    model.fit(X_train, Y_train)#treinando o modelo
    
    st.write("<p align='justify'> Acessar os valores de interceptção e inclinação da reta pode se mostrar algo muito útil. De maneira simples, cada variável independente terá um eixo no plano cartesiano, e então será feita a tentativa para acessar quando a linha de regressão corta o eixo Y e qual a inclinação da reta, sendo efetuado esse procedimento para todas as 4 variáveis em relação à expectativa de vida. <p align='justify'>", unsafe_allow_html=True) 
    st.write('Interceptação eixo Y: ',model.intercept_.round(2)) #acessando a interceptacao da funcao (b)
    st.write('Inclinação da reta de regressão para cada uma das 4 variáveis: ',model.coef_.round(2)) #acessando a inclinacao da curva da funcao (m)
    
    st.write("<p align='justify'> Com o modelo definitivamente separado em treino e teste e finalizada a etapa de treinamento, é possível seguir para a próxima fase de avaliação da regressão criada. <p align='justify'>", unsafe_allow_html=True)      
    st.write("<p align='justify'> texto <p align='justify'>", unsafe_allow_html=True)    


elif paginaSelecionada == 'Avaliação':
    st.markdown("<h1 style='text-align: center; color: black;'>Avaliação</h1>", unsafe_allow_html=True)   
    st.write("<p align='justify'> A fase de avaliação serve como a perícia do objetivo alcançado, avaliando se o modelo criado possui as características requisitadas na fase de entendimento do negócio. <p align='justify'>", unsafe_allow_html=True)    
    st.write("<p align='justify'> Sendo assim, como designado anteriormente, o modelo de previsão da expectativa de vida utilizando regressão linear múltipla deve possuir valores entre 0.5 e 3 para as métricas de Erro médio Quadrático (MSE) e Erro médio Absoluto (MAE). <p align='justify'>", unsafe_allow_html=True)    
    st.write("""<p align='justify'> Portanto, tais métricas podem ser explicadas da seguinte maneira:
             <ul>
             <li> <b> Erro Médio Quadrático (MSE):</b> Mede a distância média quadrada entre os dados reais e os dados previstos. Aqui, erros maiores são bem anotados (melhores do que MAE). </li>
             <li> <b> Erro Médio Absoluto (MAE):</b> Mede a distância média absoluta entre os dados reais e os dados previstos, mas falha em punir grandes erros de previsão.</li>
             </ul><p align='justify'>""", unsafe_allow_html=True)  
             
    st.write("<p align='justify'> Sendo assim, após a aplicação do modelo de regressão linear multivariada para a previsão de um valor contínuo da expectativa de vida da população brasileira, gerou-se os seguintes valores para tais métricas: <p align='justify'>", unsafe_allow_html=True)    
    
    df["Alcool"] = df["Alcool"].fillna(df["Alcool"].mean())
    df["Despesas_totais"] = df["Despesas_totais"].fillna(df["Despesas_totais"].mean())
    
    X = df[['Alcool', 'Escolaridade', 'Despesas_totais', 'PIB']]
    
    Y = df['Expectativa_de_vida']
    
    model = LinearRegression() #criando a variavel pra usar reg linear
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=1) #separando os dados para treino e teste
    model.fit(X_train, Y_train)#treinando o modelo
    
    y_test_predicted = model.predict(X_test)
    #y_test_predicted.shape
    
    st.write("<p align='justify'> <b> Erro Médio Quadrático (MSE) do modelo: </b> <p align='justify'>", unsafe_allow_html=True) 
    st.write(mean_squared_error(Y_test, y_test_predicted))
    
    st.write("<p align='justify'> <b> Erro Médio Absoluto (MAE) do modelo: </b> <p align='justify'>", unsafe_allow_html=True)
    st.write(mean_absolute_error(Y_test, y_test_predicted))
    #print(model.score(X_test, Y_test))
    
    
    st.write("<p align='justify'> Portanto, percebe-se que o requisito para tais métricas foi atingido, uma vez que elas estão no intervalo de 0.5 e 3. Sendo assim o modelo de previsão da expectativa de vida dado algumas variáveis que impactam positivamente está concluído e válidado. <p align='justify'>", unsafe_allow_html=True)
    st.write("<p align='justify'> Dessa maneira, a finalização do projeto está apenas na fase de implementação do modelo via biblioteca streamlit programada em Python.  <p align='justify'>", unsafe_allow_html=True)
    #st.write("<p align='justify'> texto <p align='justify'>", unsafe_allow_html=True)     
    
elif paginaSelecionada == 'Implementação':
    st.markdown("<h1 style='text-align: center; color: black;'>Implementação</h1>", unsafe_allow_html=True)    
    st.write("<p align='justify'> A fase de implementação é a última na metodologia de projeto de mineração de dados do CRISP-DM. Essa fase tem como objetivo iniciar a produção do modelo de alguma forma, porém sempre monitorando-o para que cada erro seja corrigido o mais breve possível. <p align='justify'>", unsafe_allow_html=True)
    st.write("<p align='justify'> Dessa maneira, a implementação do modelo criado nesse projeto será por meio da biblioteca Streamlit programada em Pytho. Com o uso do Streamlit é possível criar um ambiente interativo com o usuário, para que ele forneça os valores para as variáveis preditoras e o modelo retorne um valor contínuo para a variável alvo, no caso a expectativa de vida. <p align='justify'>", unsafe_allow_html=True)
    #st.write("<p align='justify'> texto <p align='justify'>", unsafe_allow_html=True)    
    
    st.title('Previsão Expecativa de vida')
    st.write('Preencha os dados de cada variável (Basta arrastar a bolinha vermelha de cada nível):')
    
    df["Alcool"] = df["Alcool"].fillna(df["Alcool"].mean())
    df["Despesas_totais"] = df["Despesas_totais"].fillna(df["Despesas_totais"].mean())
    print(df.isna().sum())
    
    
    
    X = df[['Alcool', 'Escolaridade', 'Despesas_totais', 'PIB']]
    #print(X.shape)
    
    Y = df['Expectativa_de_vida']
    #print(Y.shape)
    model = LinearRegression() #criando a variavel pra usar reg linear
    
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state=1) #separando os dados para treino e teste
    model.fit(X_train, Y_train)#treinando o modelo
    
    #model.intercept_.round(2) #acessando a interceptacao da funcao (b)
    #model.coef_.round(2) #acessando a inclinacao da curva da funcao (m)
    
    
    y_test_predicted = model.predict(X_test)
    #y_test_predicted.shape
    #print(type(y_test_predicted))
    #print(y_test_predicted)
    
    PredAlcool = st.slider('Alcool - Consumo per capito de álcool em litros de álcool puro (População): ', min_value=0.0, max_value=30.0)
    #PredIMC = st.slider('IMC: Índice de massa corporal médio de toda a população: ', min_value=0, max_value=100)
    #PredComp = st.slider('Composicao da renda dos recursos - Índice de Desenvolvimento Humano em termos de composição da renda dos recursos (População): ', min_value=0.0, max_value=1.0)
    PredEscolaridade = st.slider('Escolaridade - Número de anos de escolaridade (População): ', min_value=0, max_value=70)
    PredPIB = st.slider('PIB - PIB per capita (em dólares americanos): ', min_value=0, max_value=10000)
    PredDespesas = st.slider('Despesas Totais Saúde - Gastos do governo geral com saúde sendo uma porcentagem dos gastos totais do governo (em %): ')
    #PredPopulacao = st.slider('Populacao total', min_value=0, max_value=2000000)
    #PredMorteInfantil = st.slider('Mortes Infantís: Número de mortes infantis por 1000 habitantes.')
    #PredMortInf = st.slider('Número de mortes infantis por 1000 habitantes: ', min_value=0, max_value=1000)
    
    
    new_array = np.array([PredAlcool, PredEscolaridade, PredDespesas, PredPIB]).reshape(-1, 4)
    st.write('Expectativa de vida da nação brasileira (após o preenchimento dos dados): ', model.predict(new_array))
    



