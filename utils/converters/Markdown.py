import re

class Markdown:

  __formattedFile = []
  __analyzing = []

  
  def __processSingleLine(self, line):
    if(self.__isHeading(line)):
      self.__process("p")
      self.__analyzing.append(re.sub("(#{1,6})", "", line).strip())
      self.__process("h" + str(len(re.split("\s", line)[0])))
    elif(self.__isHeading2(line)):
      self.__process("h1")
    elif(self.__isBlankLine(line)):
      self.__process("p")
    else:
      self.__analyzing.append(line)

  def __isHeading(self, line):
    return re.match("^(#{1,6})(\s)+", line) != None

  def __isHeading2(self, line):
    if(len(self.__analyzing) == 1 and re.match("^[\=]+$", line) != None):
      return True
    return False

  def __isBlankLine(self, line):
    return re.match("^[\n]", line) != None

  def __convertAttribute(self, markdown, tag):
    lineIndex1 = -1
    wordIndex1 = -1
    lineIndex2 = -1
    wordIndex2 = -1
    for lIndex in range(len(self.__analyzing)):
      words = re.split("\s", self.__analyzing[lIndex])
      for wIndex in range(len(words)):
        if(lineIndex1 == -1):
          if(re.match("^[\\" + markdown + "][\S]", words[wIndex])):
            lineIndex1 = lIndex
            wordIndex1 = wIndex
        if(lineIndex1 >= 0):
          if(re.match("[\S]+[\\" + markdown + "][\.\,\;\:]*$", words[wIndex])):
            lineIndex2 = lIndex
            wordIndex2 = wIndex
            break
        wIndex += 1
      if(lineIndex2 >= 0):
        break
    if(lineIndex2 >= 0):
      newLine1 = re.split("\s", self.__analyzing[lineIndex1])
      newLine1[wordIndex1] = re.sub("^\\" + markdown, "<" + tag + ">", newLine1[wordIndex1])
      self.__analyzing[lineIndex1] = " ".join(newLine1)
      newLine2 = re.split("\s", self.__analyzing[lineIndex2])
      newLine2[wordIndex2] = re.sub("\\" + markdown, "</" + tag + ">", newLine2[wordIndex2])
      self.__analyzing[lineIndex2] = " ".join(newLine2)
      return True
    return False

  def __convertFormat(self):
    while self.__convertAttribute("_", "em"): continue
    while self.__convertAttribute("*{2,2}", "strong"): continue
    while self.__convertAttribute("`", "code"): continue

  def __convertParagraph(self, tag):
    if(len(self.__analyzing) > 0):
      self.__analyzing[0] = "<" + tag + ">" + self.__analyzing[0]
      self.__analyzing[-1] = "".join(self.__analyzing[-1].split("\n")) + "</" + tag + ">"

  def __process(self, tag):
    self.__convertFormat()
    self.__convertParagraph(tag)
    self.__formattedFile.extend(self.__analyzing)
    self.__analyzing.clear()

  def toHTML(self, filepath):
    f = open(filepath, "r")
    lines = f.readlines()
    for line in lines:
      self.__processSingleLine(line)
    for li in self.__formattedFile:
      print(li)