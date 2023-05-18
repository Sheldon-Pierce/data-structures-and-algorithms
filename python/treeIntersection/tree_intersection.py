from hashtable.hashtable import Hashtable


def tree_intersection(first_tree, second_tree):
    hashtable = Hashtable(1064)
    dupes = set()

    if first_tree.root:
        first_val = first_tree.pre_order()
        for value in first_val:
            hashtable.set(value, value)

    if second_tree.root:
        second_val = second_tree.pre_order()
        for value in second_val:
            if hashtable.has(value) and value not in dupes:
                dupes.add(value)

    return list(dupes)


