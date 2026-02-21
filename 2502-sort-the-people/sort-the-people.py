class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dictionary = zip(heights,names)
        dictionary = sorted(dictionary, key=lambda x : x[0], reverse=True)
        return [dictionary[i][1] for i in range(len(dictionary))]