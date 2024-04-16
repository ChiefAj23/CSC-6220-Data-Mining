#Abhijeet Solanki
#T00221273
#Class: CSC-6220
#Date: 04/15/2024
#Homework#3-Q2(b) : Apriori Algorithm to find frequent itemsets within a list of transactions

# Apriori Algorithm to find frequent itemsets within a list of transactions
def apriori(transactions, min_support):
    item_count = {}
    for transaction in transactions:
        for item in transaction:
            item_count[item] = item_count.get(item, 0) + 1

    support_count_threshold = min_support * len(transactions)
    frequent_itemsets = {1: {frozenset([item]): count
                             for item, count in item_count.items()
                             if count >= support_count_threshold}}
# Function to generate the itemsets for the next level from the current itemsets
    def generate_next_level(current_level_itemsets):
        next_level = set()
        for itemset1 in current_level_itemsets:
            for itemset2 in current_level_itemsets:
                if len(itemset1.union(itemset2)) == len(itemset1) + 1:
                    next_level.add(itemset1.union(itemset2))
        return next_level

    k = 1
    while frequent_itemsets[k]:
        candidate_itemsets = generate_next_level(frequent_itemsets[k])
        counts = {itemset: 0 for itemset in candidate_itemsets}
        for transaction in transactions:
            for itemset in candidate_itemsets:
                if itemset.issubset(transaction):
                    counts[itemset] += 1

        k += 1
        frequent_itemsets[k] = {itemset: count for itemset, count in counts.items() if count >= support_count_threshold}
        if not frequent_itemsets[k]:
            del frequent_itemsets[k]
            break

    return frequent_itemsets

# Define the transactions
given_transactions = [
    {'M', 'O', 'N', 'K', 'E', 'Y'},
    {'D', 'O', 'N', 'K', 'E', 'Y'},
    {'M', 'A', 'K', 'E'},
    {'M', 'U', 'C', 'K', 'Y'},
    {'C', 'O', 'O', 'K', 'I', 'E'}
]

# Set the minimum support percentage given in the question
min_support_percentage = 0.6

frequent_itemsets_by_stage = apriori(given_transactions, min_support_percentage)

for stage, itemsets in frequent_itemsets_by_stage.items():
    print(f"Stage {stage} - {len(itemsets)} Frequent {stage}-itemset(s):")
    for itemset in itemsets:
        print(f"  Itemset: {set(itemset)}, Support count: {itemsets[itemset]}")
    print("\n" + "-"*80 + "\n")

