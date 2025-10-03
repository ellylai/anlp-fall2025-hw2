from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score

def evaluate(responses, ref_responses):
    a, r, p, f = calculate(responses, ref_responses)
    print("Accuracy:", a)
    print("Recall:", r)
    print("Precision:", p)
    print("F1 Score:", f)

def calculate(responses, ref_responses):
    with open(ref_responses, 'r') as f_in:
        content = f_in.readlines()

    i = 0
    acc = 0
    recall = 0
    precision = 0
    f1 = 0
    for line in content:
        acc += accuracy_score(line, responses[i])
        r, p, f, _ = precision_recall_fscore_support(line, responses[i])
        recall += r
        precision += p
        f1 += f
        i += 1
    
    return acc / float(i), recall / float(i), precision / float(i), f1 / float(i)