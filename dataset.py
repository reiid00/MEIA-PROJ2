#!/usr/bin/env python
# coding: utf-8

# In[1]:



# In[2]:


import pandas as pd


# In[4]:


dataset_prod_1 = pd.read_excel("DATASET/Produtos/Produtos/Produtos_1.xls","Produtos")
dataset_prod_2 = pd.read_excel("DATASET/Produtos/Produtos/Produtos_2.xls","Query")
dataset_prod_3 = pd.read_excel("DATASET/Produtos/Produtos/Produtos_3.xls","Query")
dataset_prod_4 = pd.read_excel("DATASET/Produtos/Produtos/Produtos_4.xls","Query")
dataset_prod_5 = pd.read_excel("DATASET/Produtos/Produtos/Produtos_5.xls","Query")
dataset_prod_6 = pd.read_excel("DATASET/Produtos/Produtos/Produtos_6.xls","Query")
dataset_prod_7 = pd.read_excel("DATASET/Produtos/Produtos/Produtos_7.xls","Query")


# In[13]:


dataset_prod_merged = pd.concat([dataset_prod_1,dataset_prod_2,dataset_prod_3,dataset_prod_4,dataset_prod_5,dataset_prod_6,dataset_prod_7])


# In[15]:


print(dataset_prod_merged)


# In[16]:


print(len(dataset_prod_merged))
size_all_prod_datasets = len(dataset_prod_1) + len(dataset_prod_2) + len(dataset_prod_4)+ len(dataset_prod_3)+ len(dataset_prod_5)+ len(dataset_prod_6)+ len(dataset_prod_7)
if len(dataset_prod_merged) == size_all_prod_datasets :
    print("Size is correct!")

if len(dataset_prod_merged.columns) == len(dataset_prod_1.columns):
    print("Number of columns is correct")

print("Concatenation was correctly made!")


# In[18]:


print(dataset_prod_merged.columns)


# In[19]:


ds_prod = dataset_prod_merged[["Código","Nome","Unidade","Referência","Data da última atualização","Nome da marca", "Complemento", "Classificação11","Classificação12","Classificação13","Classificação14","Classificação15"]]


# In[20]:


print(ds_prod.columns)


# In[29]:


ds_cl_prod = pd.read_excel("DATASET/Produtos/Produtos/Classificacoes_dos_produtos.xlsx",nrows=900)


# In[32]:


ds_cl_prod_merged = ds_cl_prod[["Classificação","Código","Nome"]]


# ds_cl_prod_11 = ds_cl_prod_merged.log[ds_cl_prod_merged['Classificação'] == 11].rename(columns={"Código":"Código_Class_11","Nome":"Nome_Class_11"})

# In[33]:


ds_cl_prod_11 = ds_cl_prod_merged.loc[ds_cl_prod_merged['Classificação'] == 11].rename(columns={"Código":"Código_Class_11","Nome":"Nome_Class_11"})
ds_cl_prod_12 = ds_cl_prod_merged.loc[ds_cl_prod_merged['Classificação'] == 12].rename(columns={"Código":"Código_Class_12","Nome":"Nome_Class_12"})
ds_cl_prod_13 = ds_cl_prod_merged.loc[ds_cl_prod_merged['Classificação'] == 13].rename(columns={"Código":"Código_Class_13","Nome":"Nome_Class_13"})
ds_cl_prod_14 = ds_cl_prod_merged.loc[ds_cl_prod_merged['Classificação'] == 14].rename(columns={"Código":"Código_Class_14","Nome":"Nome_Class_14"})
ds_cl_prod_15 = ds_cl_prod_merged.loc[ds_cl_prod_merged['Classificação'] == 15].rename(columns={"Código":"Código_Class_15","Nome":"Nome_Class_15"})


# In[34]:


print(ds_cl_prod_15)


# In[35]:


ds_prod = pd.merge(ds_prod,ds_cl_prod_11[['Código_Class_11','Nome_Class_11']], left_on='Classificação11', right_on='Código_Class_11', how='left').drop(columns=["Código_Class_11"])
ds_prod = pd.merge(ds_prod,ds_cl_prod_12[['Código_Class_12','Nome_Class_12']], left_on='Classificação12', right_on='Código_Class_12', how='left').drop(columns=["Código_Class_12"])
ds_prod = pd.merge(ds_prod,ds_cl_prod_13[['Código_Class_13','Nome_Class_13']], left_on='Classificação13', right_on='Código_Class_13', how='left').drop(columns=["Código_Class_13"])
ds_prod = pd.merge(ds_prod,ds_cl_prod_14[['Código_Class_14','Nome_Class_14']], left_on='Classificação14', right_on='Código_Class_14', how='left').drop(columns=["Código_Class_14"])
ds_prod = pd.merge(ds_prod,ds_cl_prod_15[['Código_Class_15','Nome_Class_15']], left_on='Classificação15', right_on='Código_Class_15', how='left').drop(columns=["Código_Class_15"])


# In[36]:


print(ds_prod.tail())


# In[39]:


dataset_detMov_2018_1 = pd.read_excel("DATASET/DetalheMovimentacao/DetalheMovimentacao_2018_Esportes_1.xls","Query")
dataset_detMov_2018_2 = pd.read_excel("DATASET/DetalheMovimentacao/DetalheMovimentacao_2018_Esportes_2.xls","Query")
dataset_detMov_2019_1 = pd.read_excel("DATASET/DetalheMovimentacao/DetalheMovimentacao_2019_Esportes_1.xls","Query")
dataset_detMov_2019_2 = pd.read_excel("DATASET/DetalheMovimentacao/DetalheMovimentacao_2019_Esportes_2.xls","Query")
dataset_detMov_2020_1 = pd.read_excel("DATASET/DetalheMovimentacao/DetalheMovimentacao_2020_Esportes_1.xls","Query")
dataset_detMov_2020_2 = pd.read_excel("DATASET/DetalheMovimentacao/DetalheMovimentacao_2020_Esportes_2.xls","Query")
dataset_detMov_2021_1 = pd.read_excel("DATASET/DetalheMovimentacao/DetalheMovimentacao_2021_Esportes_1.xls","Query")
dataset_detMov_2021_2 = pd.read_excel("DATASET/DetalheMovimentacao/DetalheMovimentacao_2021_Esportes_2.xls","Query")
dataset_detMov_2022 = pd.read_excel("DATASET/DetalheMovimentacao/DetalheMovimentacao_2022_Esportes.xls","Query")


# In[40]:


dataset_detMov_merged = pd.concat([dataset_detMov_2018_1,dataset_detMov_2018_2,dataset_detMov_2019_1,dataset_detMov_2019_2,dataset_detMov_2020_1,dataset_detMov_2020_2,dataset_detMov_2021_1,dataset_detMov_2021_2,dataset_detMov_2022])


# In[41]:


print(dataset_detMov_merged)


# In[42]:


dataset_detMov = dataset_detMov_merged[["Série", "Número", "Item", "Data do Movimento","Operação","Produto","Tamanho","Quantidade","Valor original"]]


# In[44]:


ds_tam_aux = pd.read_excel("DATASET/Tamanhos/Tamanhos.xls","Tamanhos")
ds_tam = ds_tam_aux.rename(columns={"Código":"Código_Tamanho","Nome":"Nome_Tamanho"})


# In[45]:


dataset_detMov = pd.merge(dataset_detMov,ds_tam, left_on='Tamanho', right_on='Código_Tamanho', how='left').drop(columns=["Código_Tamanho"])


# In[46]:


print(dataset_detMov.tail())


# In[47]:


ds_prod = ds_prod.rename(columns={"Referência":"Referência_Produto", "Complemento":"Complemento_Produto","Código":"Código_Produto","Nome":"Nome_Produto", "Unidade":"Unidade_Produto", "Data da última atualização":"DataUltimaAtualização_Produto","Nome da marca": "NomeMarca_Produto","Classificação11": "Classificação11_Produto","Classificação12": "Classificação12_Produto","Classificação13": "Classificação14_Produto","Classificação14": "Classificação16_Produto","Classificação15": "Classificação15_Produto", "Nome_Class_11": "Nome_Class_11_Produto", "Nome_Class_12": "Nome_Class_12_Produto", "Nome_Class_13": "Nome_Class_13_Produto", "Nome_Class_14": "Nome_Class_14_Produto", "Nome_Class_15": "Nome_Class_15_Produto"})

dataset_detMov = pd.merge(dataset_detMov, ds_prod, left_on='Produto', right_on='Código_Produto', how='left').drop(columns=["Código_Produto"])


# In[48]:


print(dataset_detMov.head(5))


# In[ ]:


dataset_detMov.to_excel('Dataset_Treated.xlsx', 'Data')


# In[ ]:




