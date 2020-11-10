import matplotlib.pyplot as plt
import pandas as pd

def age_plot():
    x = df['Clothing ID']
    y = df['Age']
    plt.plot(x, y, 'bo')
    plt.title('Età per prodotto')
    plt.xlabel('IdProdotto')
    plt.ylabel('Età')
    plt.legend(['Age'])
    plt.show()


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
    age_plot()

    df.groupby('Clothing ID')['Rating'].std()

    df['Age'].plot(kind='hist', color='teal')
    department_name = df['Department Name']

    frequency = df['Department Name'].value_counts()
    print("Frequenza department:\n", frequency)
    print(df['Department Name'].count(), " tot. dipartimento")

    frequency = df['Class Name'].value_counts()
    print("Frequenza class name:\n", frequency)
    print(df['Class Name'].count(), " tot. class name")

    # valutazioni da 1 a 5, valutazione migliore in base alla macrocategoria
    #rating_mean = df.groupby('Department Name')['Rating'].mean()

    #dipartimento = rating_mean[0]
    #valutazione = rating_mean[1]

    #plt.plot(dipartimento,valutazione)
    #plt.show()


    # creating initial dataframe
    department_df = pd.DataFrame(department_name, columns=['Department Name'])
    # converting type of columns to 'category'
    department_df['department_name'] = department_df['Department Name'].astype('category')
    # Assigning numerical values and storing in another column
    department_df['department_name_ID'] = department_df['department_name'].cat.codes
    print(department_df, " dipartimento ID")
    y = df['Clothing ID']
    x = department_df['department_name_ID']
    department_final = department_df.groupby('department_name')['department_name_ID']
    plt.plot(x, y, 'bo')
    plt.title('Dipartimento')
    plt.xlabel('Nome dipartimento')
    plt.ylabel('idProdotto')
    plt.xlim([15, 100])
    plt.legend(['line plot 1'])
    plt.show()

