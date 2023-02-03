import re
from typing import List, Tuple

def get_top_k(results: List[str], sources: List[dict], top_k: int = 2) -> Tuple[list]:
    return results[:top_k], sources[:top_k]

def build_prompt(results: List[str], query: str) -> str:
    cleaned_results = [re.sub(' +'," ",r) for r in results]
    context = "\n".join(["*"+r.replace("\n"," ") for r in cleaned_results])
    
    prompt = f"""Answer the question as truthfully as possible using the provided context, and if the answer is not contained within the text below, say "I cannot answer."
    
    Context

    {context}

    Q: {query}
    A: """
    return prompt

def lambda_handler(event, context):

    snippets = event.get('snippets')
    query = event.get('query')

    results = []
    sources = []

    for k in snippets.keys():
        _res, _src = get_top_k(snippets[k]['results'], snippets[k]['sources'])
        results+=_res
        sources+=_src

    prompt = build_prompt(results, query)

    resp = {'prompt':prompt}
    return resp
    
    




    