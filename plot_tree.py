from sklearn.tree import export_graphviz
from subprocess import call
from IPython.display import Image


def plot_tree(tree, x_labels, out_name='tree_from_forest', class_names=""):

    # Export a tree from the forest
    export_graphviz(tree, out_name+'.dot', rounded = True, 
                    feature_names=x_labels, max_depth = 8, 
                    filled = True, class_names = class_names)
    call(['dot', '-Tpng', out_name+'.dot', '-o', out_name+'.png', '-Gdpi=200'])
    return Image(out_name+'.png')
