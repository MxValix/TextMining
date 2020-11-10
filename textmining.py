import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

if __name__ == '__main__':
    excel_name = 'textmining.xlsx'
    df = pd.read_excel(excel_name)
    print(df)

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

    plt.figure(figsize=(15, 15))
    df.groupby(['Department Name', pd.cut(df['Age'], np.arange(0, 100, 10))]) \
        .size() \
        .unstack(0) \
        .plot.bar(stacked=True)
    plt.show()

    z = df.groupby(by=['Department Name'], as_index=False).count().sort_values(by='Class Name', ascending=False)

    plt.figure(figsize=(10, 10))
    sns.set_style("whitegrid")
    ax = sns.barplot(x=z['Department Name'], y=z['Class Name'], data=z, palette='plasma')
    plt.xlabel("Department Name")
    plt.ylabel("Count")
    plt.title("Counts Vs Department Name")
    plt.show()


    x = df['Clothing ID']
    y = df['Age']

    plt.plot(x, y, 'bo')
    plt.title('Età per prodotto')
    plt.xlabel('IdProdotto')
    plt.ylabel('Età')

    plt.show()

    df.groupby('Clothing ID')['Rating'].std()

    df['Age'].plot(kind='hist', color='teal')
    department_name = df['Department Name']

    # creating initial dataframe
    department_df = pd.DataFrame(department_name, columns=['Department Name'])
    # converting type of columns to 'category'
    department_df['department_name'] = department_df['Department Name'].astype('category')
    # Assigning numerical values and storing in another column
    department_df['department_name_ID'] = department_df['department_name'].cat.codes
    print(department_df)

    x = df['Clothing ID']
    y = department_df['department_name_ID']

    plt.plot(x, y, 'bo')
    plt.title('Dipartimento ')
    plt.xlabel('IdProdotto')
    plt.ylabel('Dipartimento')
    plt.xlim([15,90])
    plt.show()

    df.groupby(['Rating', pd.cut(df['Age'], np.arange(0, 100, 10))]) \
        .size() \
        .unstack(0) \
        .plot.bar(stacked=True)
    plt.show()


