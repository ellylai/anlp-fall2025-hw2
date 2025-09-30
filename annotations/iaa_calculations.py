import Levenshtein
import krippendorff

def parse_data(file):
    a1 = []
    a2 = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            cols = line.strip("\n").split("\t")
            a1.append(cols[1].split(";"))
            a2.append(cols[2].split(";"))
    a = [a1, a2]
    return a

def normalized_lev(a, b):
    max_len = max(len(a), len(b))
    if max_len == 0:
        return 0.0
    return Levenshtein.distance(a, b) / max_len

def set_distance(set1, set2):
    if not set1 or not set2:
        return 1.0
    # asym distance: set1 to set2
    d1 = [min(normalized_lev(s1, s2) for s2 in set2) for s1 in set1]
    # asym distance: set2 to set1
    d2 = [min(normalized_lev(s2, s1) for s1 in set1) for s2 in set2]
    return (sum(d1) + sum(d2)) / (len(d1) + len(d2))

def annotation_disagreement(a, b):
    return set_distance(a, b)


annotations = parse_data("annotations.txt") # doesn't exist yet!!

alpha = krippendorff.alpha(
    reliability_data=annotations,
    level_of_measurement=None,
    distance_fn=annotation_disagreement
)

print("IAA Calculations", alpha)