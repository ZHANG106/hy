import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def cut_data():
    metadata = pd.read_csv(r'.\winequality-white.csv', header=0, engine='python', sep=';')
    each_ = metadata.groupby('quality')
    if not os.path.exists('.\\result'):
        os.makedirs('.\\result')
    for each_quality in each_:
        each_quality[1].to_csv('.\\result\\%s.csv' % each_quality[0], index=False)
    each_ = each_.mean()
    each_.reset_index(inplace=True)
    return each_


def analyse_quality():
    metadata = pd.read_csv(r'.\winequality-white.csv', header=0, engine='python', sep=';')
    for i in metadata.columns:
        sns.barplot("quality", i, data=metadata)
        plt.savefig('.\\result\\%s.png' % i)
        plt.show()
        plt.scatter(y=metadata['%s' % i], x=metadata['quality'])
        plt.xlabel('quality')
        plt.ylabel(i)
        plt.savefig('.\\result\\%s_sc.png' % i)
        plt.show()
    data = metadata.groupby('quality').mean()
    data.reset_index(inplace=True)
    corrmat = data.corr()
    corrmat_origin = metadata.corr()
    plt.subplots(figsize=(12, 9))
    corrmat.sort_values(by='quality', inplace=True)
    corrmat_origin.sort_values(by='quality', inplace=True)
    axsi = corrmat['quality']
    axsi_o = corrmat_origin['quality']
    axsi.to_csv('.\\result\\mean_colleration.csv')
    axsi_o.to_csv('.\\result\\origin_colleration.csv')
    sns.barplot(y=axsi.index, x=axsi.values, linewidth=2.5)
    plt.savefig('.\\result\\colleration.png')
    plt.show()
    plt.subplots(figsize=(12, 9))
    sns.barplot(y=axsi_o.index, x=axsi_o.values, linewidth=2.5)
    plt.savefig('.\\result\\colleration_origin_data.png')
    plt.show()
    drawdata = corrmat_origin.sort_values(by=['quality'], ascending=False)
    drawdata = drawdata.index[0:5]
    sns.set()
    sns.pairplot(metadata[drawdata], size=2.5)
    plt.show()


def to_R():
    metadata = pd.read_csv(r'.\winequality-white.csv', header=0, engine='python', sep=';')
    res = []
    ts = metadata['quality']
    data_norm = (metadata - metadata.mean()) / (metadata.std())
    data_norm['quality'] = ts
    attribut = data_norm.columns
    for i in data_norm.iterrows():
        for j in attribut:
            ligne = [eval("i[1]['%s']" % j), j, i[1].quality]
            res.append(ligne)
    res = pd.DataFrame(res, columns=['value', 'feature', 'quality'])
    res.to_csv('.\\result\\rr.csv', index=False)
    return res


if __name__ == '__main__':
    cut_data()
    analyse_quality()
    # to_R()
