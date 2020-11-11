import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#import secondary as sec


def open_dataset():
    excel_name = 'textmining.xlsx'
    df = pd.read_excel(excel_name)
    print(df)
    return df


def many_trials():
    df
    df.std()
    df.head()
    df.tail()
    df.describe()
    df['Clothing ID']
    df.groupby('Clothing ID')['Age'].mean()
    df.groupby('Clothing ID')['Age'].max()
    min_age = df['Age'].min()
    max_age = df['Age'].max()
    df.groupby('Clothing ID')['Age'].std()
    df.groupby('Clothing ID')['Rating'].mean()
    df.groupby('Clothing ID')['Rating'].std()
    df['Clothing ID'].unique()
    pd.unique(df['Clothing ID']).tolist()
    df.groupby('Clothing ID')['Rating'].std()


# età per prodotto: età e idProdotto
def age_plot():
    x = df['Clothing ID']
    y = df['Age']
    plt.plot(x, y, 'bo')
    plt.title('Età per prodotto')
    plt.xlabel('IdProdotto')
    plt.ylabel('Età')
    plt.legend(['Age'])
    plt.show()


def department_age_plot():
    plt.figure(figsize=(15, 15))
    a = df.groupby(['Department Name', pd.cut(df['Age'], np.arange(0, 100, 10))])
    a.size().unstack(0).plot.bar(stacked=True)
    plt.show()


def counts_department_plot():
    z = df.groupby(by=['Department Name'], as_index=False)
    z = z.count().sort_values(by='Class Name', ascending=False)
    plt.figure(figsize=(10, 10))
    sns.set_style("whitegrid")
    ax = sns.barplot(x=z['Department Name'], y=z['Class Name'], data=z, palette='plasma')
    plt.xlabel("Department Name")
    plt.ylabel("Count")
    plt.title("Counts Vs Department Name")
    plt.show()


def rating_age_plot():
    b = df.groupby(['Rating', pd.cut(df['Age'], np.arange(0, 100, 10))])
    b.size().unstack(0).plot.bar(stacked=True)
    plt.show()


def reviewlength_plot():
    df['Review Text'] = df['Review Text'].astype(str)
    df['Review Length'] = df['Review Text'].apply(len)
    plt.figure(figsize=(10, 10))
    sns.boxplot(x='Rating', y='Review Length', data=df)
    plt.show()


def clothing_recommended_boxplot():
    plt.figure(figsize=(10, 10))
    y_data = 'Clothing ID'
    sns.boxplot(x='Recommended IND', y=y_data, data=df)
    plt.ylim(500, 1300)
    plt.show()


if __name__ == '__main__':
    df = open_dataset()
    sns.pairplot(df, hue="Department Name")
    plt.savefig('pairplot.png')
    plt.show()
    #plt.show()
    # many_trials()
    # age_plot()
    # department_age_plot()
    # counts_department_plot()
    # rating_age_plot()
    # reviewlength_plot
    # clothing_recommended_boxplot()


    # department_productid()


    # plt.figure(figsize=(15, 15))
    # sns.set_theme(style="whitegrid")
    # ax = sns.boxplot(x="Age", y="Recommended IND",
    #              data=df, palette="Set3")
    # plt.show()
    #df1 = pd.DataFrame(df, columns=['Age', 'Rating'])
    #ax = sns.boxplot(data=df1, orient="h", palette="Set2")
    #plt.show()








