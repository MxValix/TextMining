import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from utils import show_values_on_bars, open_dataset


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

def rating_age_box_plot():
    sns.set(rc={'figure.figsize': (11, 6)})
    sns.boxplot(x='Rating', y='Age', data=df)
    plt.title('Rating Distribution per Age')
    plt.show()


def review_length_plot():
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


def pair_plot_department():
    sns.pairplot(df, hue="Department Name")
    plt.savefig('pairplot.png')
    plt.show()


def missing_values_plot():
    # the amount of missing values per feature
    sns.set(rc={'figure.figsize': (11, 4)})
    pd.isnull(df).sum().plot(kind='bar')
    plt.ylabel('Number of missing values')
    plt.title('Missing Values per Feature');
    plt.show()


def distribution_ratings():
    sns.set(rc={'figure.figsize': (6, 6)})
    plt.title('Distribution of Ratings')
    sns.countplot(x='Rating', data=df)
    plt.show()


def distribution_of_reviews(column, title):
    plt.figure(figsize=(20, 20))
    plt.xticks(rotation=45)
    sns.countplot(x=column, data=df)
    plt.title(title)
    file_name = title + '.png'
    plt.savefig(file_name)
    plt.show()


def recommended_items(color_1, color_2, column, title):
    recommended = df[df['Recommended IND'] == 1]
    not_recommended = df[df['Recommended IND'] == 0]
    plt.figure(figsize=(20, 20))
    sns.countplot(x=recommended[column], data=df, color=color_1, alpha=0.8, label="Recommended")
    sns.countplot(x=not_recommended[column], data=df, color=color_2, alpha=0.8, label="Not Recommended")
    plt.title(title)
    plt.legend()
    file_name = title + '.png'
    plt.savefig(file_name)
    plt.show()


def recommended_fun():
    # Recommended in Division
    color_1 = "orange"
    color_2 = "red"
    column = 'Division Name'
    title = "Recommended Items in each Division"
    recommended_items(color_1, color_2, column, title)

    # Recommended in Department
    color_1 = "green"
    color_2 = "aquamarine"
    column = 'Department Name'
    title = "Recommended Items in each Department"
    recommended_items(color_1, color_2, column, title)

    # Recommended in Class
    color_1 = "violet"
    color_2 = "fuchsia"
    column = 'Class Name'
    title = "Recommended Items in each Class"
    recommended_items(color_1, color_2, column, title)


def frequency_count_class():
    # retrieve class name frequency (top 50)
    plt.subplots(figsize=(9, 5))
    z = sns.countplot(y="Class Name", data=df, order=df["Class Name"].value_counts()[:50].index)
    show_values_on_bars(z, "h", 0.3)
    plt.title("Frequency Count of Class Name")
    plt.xlabel("Count")
    plt.show()


if __name__ == '__main__':
    df = open_dataset()
    # many_trials()
    # age_plot()
    # department_age_plot()
    # counts_department_plot()
    # rating_age_plot()
    # rating_age_box_plot()
    # review_length_plot
    # clothing_recommended_boxplot()

    # pair_plot_department()
    missing_values_plot()
    distribution_ratings()
    distribution_of_reviews('Division Name', "Reviews in each Division")
    distribution_of_reviews('Department Name', "Reviews in each Department")
    distribution_of_reviews('Class Name', "Reviews in each Class")
    recommended_fun()
    frequency_count_class()
