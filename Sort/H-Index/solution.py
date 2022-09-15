def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citation) - idx:
            return idx
    return len(citations)