import pandas as pd

df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

df = pd.concat([df1,df2,df3,df4,df5])

df.head()

df.tail()

df.dtypes

df["LojaID"] = df.["LojaID"].astype(object)

df.isnull.sum()

df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

df.dropna(inplace=True)

df["Receita"] = df["Vendas"].mul(df["Qtd"])

df.sort("Receita", ascending=False).head(20)

df.groupby("Cidade")["Receita"].sum()

#-------------------------------------------------
#datas no panda

df["Data"] = df["Data"].astype("int64")

df["Data"] = pd.to_datetime(df["Data"])

df.groupby(df["Data"].dt.year)["Receita"].sum()

df.groupby(df["Data"].dt.day)["Receita"].sum().max()

#-------------------------------------------------
#Vizualizando os dados
import matplotlib.pyplot as plt

df["LojaID"].value_counts(ascending=False)

df["LojaID"].value_counts(ascending=False).plot.bar()

df["LojaID"].value_counts(ascending=True).plot.barh();

df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

df["Cidade"].value_counts().plot.bar(title="Total Vendas por Cidade", color="Green")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")


plt.style.use("ggplot")
df.groupby(df["Data"].dt.month)["Qtde"].sum().plot(title="Produtos Vendidos", color="blue")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend();


plt.hist(df["Qtde"], color="dimgray")

x = df["Data"].dt.day
y = df["Receita"]
plt.scatter(x,y)


#Salvando os graficos em PNG
df.groupby(df["Data"].dt.month)["Qtde"].sum().plot(title="Produtos Vendidos", color="blue", marker = "o")
plt.title("Qantidade de Produtos por Vendidos X Mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.savefig("Grafico QTDE X MES.png");


#-----------------------------------------------------------
#Analiza Exploratotia


