class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counter1, counter2 = Counter(word1), Counter(word2)
        list1, list2 = list(counter1.values()), list(counter2.values())
        list1.sort(), list2.sort()
        print(list1, list2)
        if set(counter1.keys()) == set(counter2.keys()) and list1 == list2:
            return True
        return False
