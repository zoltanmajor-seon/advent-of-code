from collections import Counter


def load_input():
    with open("day_1_input.txt", "r") as f:
        lines =  f.read().split("\n")
    id_repo_1 = []
    id_repo_2 = []

    for line in lines:
        ids = line.split("   ")
        id_repo_1.append(int(ids[0]))
        id_repo_2.append(int(ids[1]))
    id_repo_1.sort()
    id_repo_2.sort()
    return id_repo_1, id_repo_2

def main():

    id_repo_1, id_repo_2 = load_input()
    print(id_repo_1, id_repo_2)
    id_counts_1 = Counter(id_repo_1)
    id_counts_2 = Counter(id_repo_2)
    print(id_counts_1)
    print(id_counts_2)
    total = 0
    for location_id, count in id_counts_1.items():
        if location_id in id_counts_2:
            total += count * location_id * id_counts_2[location_id]

    print(total)





if __name__ == "__main__":
    main()
