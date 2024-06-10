# Write your solution here
def find_words(search_term: str):
    output = []
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n", "")            
            if "*" in search_term:
                if search_term[0] == "*":
                    if word.endswith(search_term[1:]):
                        output.append(word)
                else:
                    if word.startswith(search_term[:len(search_term)-1]):
                        output.append(word)
            elif "." in search_term:
                if len(search_term) == len(word):
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            break
                    else:
                        output.append(word)
            else:
                if word == search_term:
                    output.append(word)

    return output

if __name__ == "__main__":
    '''print(find_words("*vokes"))
    print(find_words("okes*"))
    print(find_words("reson*"))
    print(find_words("cat"))
    print(find_words("ca."))
    print(find_words("c.d."))'''
    print(find_words("a...e"))