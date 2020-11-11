def department_productid(df):
    df['Age'].plot(kind='hist', color='teal')
    department_name = df['Department Name']

    # creating initial dataframe
    department_df = pd.DataFrame(department_name, columns=['Department Name'])
    # converting type of columns to 'category'
    department_df['department_name'] = department_df['Department Name'].astype('category')
    # Assigning numerical values and storing in another column
    department_df['department_name_ID'] = department_df['department_name'].cat.codes
    print(department_df)

    y = df['Clothing ID']
    x = department_df['department_name_ID']

    plt.plot(x, y, 'bo')
    plt.title('Dipartimento ')
    plt.xlabel('IdProdotto')
    plt.ylabel('Dipartimento')
    plt.xlim([15, 90])
    plt.show()
