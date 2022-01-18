import goslate

def translator(sentance, language="en"):
  gs = goslate.Goslate()
  result = gs.translate(sentance, language)
  return result

print(translator("This is nice", "it"))
