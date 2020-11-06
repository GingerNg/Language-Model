from utils import file_utils
if __name__ == "__main__":
    data = file_utils.readFile("./glove/vectors.txt", encoding="utf-8")
    lines = data.split("\n")
    word_count = len(lines)
    word_dim = len(lines[0].split()[1:])
    print(word_count, word_dim)
    out = open("industry_vec.txt", 'w')
    out.write(str(word_count)+" "+str(word_dim)+"\n")
    out.write(data)
