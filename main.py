import json

file = "D:/ISJ/ING4/algo/gce-code/datas.json"

# Datas registration

# res = "D:/ISJ/ING4/algo/gce-code/res.txt"

# with open(res, "r") as f:
#     content = f.read().splitlines()
#     content = [line for line in content if line != ""]

# i = 0
# for line in content:
#     data = datas = {}

#     chaine = line.split(" # ")
#     nom = chaine[0]
#     papers = chaine[1].split(",")
#     data["passed_paper"] = len(papers)

#     score = {}
#     for paper in papers:
#         paper = paper.split("-")
#         item = paper[0]
#         score_item = paper[1]
#         score[item] = score_item
#     data["score"] = score

#     with open(file, 'r') as f:
#         datas = json.load(f)

#     with open(file, "w", encoding="utf-8") as f:
#         datas[nom] = data
#         json.dump(datas, f, indent=4, ensure_ascii=False)
#     i += 1
#     print(f"---------[ Élève n. {i} enrégistré. ]---------")


datas = {}
with open(file, 'r') as f:
    datas = json.load(f)


def gce_method(dataset):
    """Classement selon le GCE

    Args:
        dataset (dict): liste des résultats
        {
            "<Student's name>": {
            "passed_paper": 5,
            "score": {
                "BIO": "D", 
                "CHE": "C",
                "FMA": "D",
                "PHY": "D",
                "PMM": "C"
            }
        }
    """
    items = {}
    result = []
    for key, value in dataset.items():
        items[key] = value.get("passed_paper", 0)

    # Trie par valeur décroissante du dictionnaire
    items = dict(sorted(items.items(), key=lambda item: item[1], reverse=True))
    for key in items.keys():
        result.append(key)
    print(result)


def decloisonement(datas):
    """Classement en utilisant le décloisement simple

    Args:
        datas (dict): Liste des résultats
        {
            "<Student's name>": {
            "passed_paper": 5,
            "score": {
                "BIO": "D",
                "CHE": "C",
                "FMA": "D",
                "PHY": "D",
                "PMM": "C"
            }
        }
    """
    items = scores = {}
    probas = {
        "A": 0.05,
        "B": 0.10,
        "C": 0.20,
        "D": 0.25,
        "E": 0.40
    }
    
    proba = {k:v*4 for k,v in probas}

    for key, values in datas.items():
        scores[key] = [i for i in values.get("score").values()]
    
    for key, value in scores.items():
        items[key] = 0
        items[key] += value.count("A") * proba["A"]
        items[key] += value.count("B") * proba["B"]
        items[key] += value.count("C") * proba["C"]
        items[key] += value.count("D") * proba["D"]
        items[key] += value.count("E") * proba["E"]

    # Trie par valeur décroissante du dictionnaire
    items = dict(sorted(items.items(), key=lambda item: item[1], reverse=True))
    
    return(items)
    
    
def decloisonement_mean(dataset):
    """Décloisonement avec classement basé sur les moyennes.

    Args:
        dataset (dict): Liste des résultats
        {
            "<Student's name>": {
            "passed_paper": 5,
            "score": {
                "BIO": "D",
                "CHE": "C",
                "FMA": "D",
                "PHY": "D",
                "PMM": "C"
            }
        }
    """
    items = decloisonement(dataset)
    
    for key, value in datas.items():
        items[key] /= value.get("passed_paper")
    
    print(items)


if __name__ == "__main__":
    # Méthode 1
    print("\n-------------[ GCE ]--------------\n")
    gce_method(datas)
    print("\n")

    # Méthode 2
    print("---------[ Décloisonement ]---------\n")
    print(decloisonement(datas))
    print("\n")
    
    # Méthode 4
    print("-----[ Décloisonement Moyenne ]-----\n")
    decloisonement_mean(datas)
    print("\n")