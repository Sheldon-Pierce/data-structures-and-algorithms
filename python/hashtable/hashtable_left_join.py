def left_join(synonyms, antonyms):
    keys = synonyms.keys()
    result = []

    for key in keys:
        result.append([key, synonyms.get(key), antonyms.get(key)])
    print(result)
    return result
