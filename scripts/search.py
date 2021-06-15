
'''
def search(collection,key):
    resultant=[]
    resultant.extend([ first for first in collection if first.username.upper().startswith(key.upper())])
    resultant.extend([ first for first in collection if key.upper() in first.username.upper() if first not in resultant ])
    return resultant'''

def search_for(collection,key):
    resultant=[]

    for i in range(30):
        resultant.extend(sorted([ user for user in collection if key.upper() in user.username.upper()[:i] if user not in resultant], key=lambda X:X.username))
    return resultant



