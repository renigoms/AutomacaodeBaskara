# minha solução
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist2 = plist[:8:]
plist2.remove("'")
plist2.pop(0)
plist2.insert(2, plist2.pop(3))
plist2.extend([plist2.pop(), plist2.pop()])
new_phrase = ''.join(plist2[:])
print(plist2)
print(new_phrase)
# solução do livro:
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])
print(plist)
print(new_phrase)
