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
    distances = []
    for i in range(len(id_repo_1)):
        distances.append(abs(id_repo_1[i] - id_repo_2[i]))
    print(distances)
    distance = sum(distances)
    print(distance)


if __name__ == "__main__":
    main()
