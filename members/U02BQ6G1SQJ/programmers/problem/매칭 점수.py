# 시험 당시 작성한 코드 : 없음

# 부스트캠프 이후 작성 코드
import re;

class PageNode:
    def __init__(self, url = "", externalLinkList = [], baseFraction = [0, 0], linkFraction = [0, 0]):
        self.url = url;
        self.externalLinkList = externalLinkList;
        self.baseFraction = baseFraction;
        self.linkFraction = linkFraction;
        
    def printPageNode(self):
        print("url :", self.url);
        print("externalLinkList :", self.externalLinkList);
        print("baseFraction :", self.baseFraction);
        print("linkFraction :", self.linkFraction);
        return None;

def printPageList(pageList : list) -> None:
    for curPage in pageList:
        curPage.printPageNode();
        print();
    
    print();
    return None;
    
def getURL(curStr : str, attributeStr : str) -> str:
    wordList = curStr.split();
                
    # print(wordList);

    for curWord in wordList:
        if (attributeStr in curWord):
            # print(curWord);
            
            return curWord.split("\"")[1];
    
    return "";

def compareFraction(a : list, b : list) -> int:
    return ((a[0] * b[1]) - (a[1] * b[0]));

def addFraction(a : list, b : list) -> list:
    if (a == [0, 0]):
        return b;
    
    if (b == [0, 0]):
        return a;
    
    return [(a[0] * b[1]) + (a[1] * b[0]), a[1] * b[1]];

def setLinkScore(pageList : list, pageDict : dict) -> None:
    for curPage in pageList:
        for curExternalLink in curPage.externalLinkList:
            if (curExternalLink in pageDict.keys()):
                externalPage = pageList[pageDict[curExternalLink]];
                externalPage.linkFraction = addFraction(externalPage.linkFraction, [curPage.baseFraction[0], len(curPage.externalLinkList)]);
        
    return None;

def solution(word : str, pages : list) -> int:
    (answer, maxMatchFraction, pageList, pageDict) = (0, [0, 1], [], dict());
    
    for curPage in pages:
        """
        (url, externalLinkList, baseScore, isBody) = ("", [], 0, False);
        
        for curStr in curPage.split("\n"):
            if ("<meta " in curStr):
                url = getURL(curStr, "content=");
            elif ("<a " in curStr):
                externalLinkList.append(getURL(curStr, "href="));
            elif (curStr == "<body>"):
                isBody = True;
            elif (curStr == "</body>"):
                isBody = False;
                
            if (isBody):
                baseScore += [k.lower() for k in re.split("[^a-zA-Z]", curStr)].count(word.lower());
                
            # print(url);
            # print(externalLinkList);
        """
        
        (url, externalLinkList, baseScore, isBody) = ("", [], 0, False);
        
        for curStr in re.split("<|>", curPage):
            if (curStr.startswith("meta ")):
                url = getURL(curStr, "content=");
            elif (curStr.startswith("a href=")):
                externalLinkList.append(getURL(curStr, "href="));
            elif (curStr == "body"):
                isBody = True;
            elif (curStr == "/body"):
                isBody = False;
                
            if (isBody):
                baseScore += [k.lower() for k in re.split("[^a-zA-Z]", curStr)].count(word.lower());
                
            # print(url);
            # print(externalLinkList);
            
        pageDict[url] = len(pageList);
        pageList.append(PageNode(url, externalLinkList, [baseScore, 1], [0, 0]));

    setLinkScore(pageList, pageDict);
    
    for pageIdx in range(len(pageList)):
        curMatchFraction = addFraction(pageList[pageIdx].baseFraction, pageList[pageIdx].linkFraction);
        
        if (compareFraction(maxMatchFraction, curMatchFraction) < 0):
            (answer, maxMatchFraction) = (pageIdx, curMatchFraction);
    
    # printPageList(pageList);
    # print(pageDict);
    
    return answer;
