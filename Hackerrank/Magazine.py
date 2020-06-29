def checkMagazine(magazine,note):
    for word in note:
        if word in magazine:
            magazine.remove(word)
        else:
            return 'No'
    return 'Yes'

magazine = 'ive got a lovely bunch of coconuts'.split()
note = 'ive got some coconuts'.split()
print(checkMagazine(magazine, note))