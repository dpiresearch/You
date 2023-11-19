import requests
import os

YOU_API_KEY = os.getenv("YOU_API_KEY_HACKATHON")

#
# Print the results based on the list returned.
# Can also select elements in that list based on the format outlined in documentation
# https://documentation.you.com/api-reference/search
# https://documentation.you.com/api-reference/rag
# Works for 'search' and 'rag' endpoints for now
# The 'news' endpoint has a different response
#
def print_list_elements(my_list, spec=None):
    # Find the size of the list
    list_size = len(my_list)
    print("Size of the list:", list_size)

    # Print each element with a space
    for element in my_list:
        print("=====================================")
#        print(element['description'], end=' ')
        if spec is None:
            print(element, end=' ')
        else:
            print(element[spec], end=' ')
        # print(element, end=' ')
        print()
        print("=====================================")
        print()  # This ensures there's a newline after the last element

def get_ai_snippets_for_query(query, num_results=3):
    print("Hitting Search")
    headers = {"X-API-Key": YOU_API_KEY}
    params = {"query": query,
		"num_web_results":num_results}
    return requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        params=params,
        headers=headers,
    ).json()

def get_rag_snippets_for_query(query, num_results=3):
    print("Hitting RAG")
    headers = {"X-API-Key": YOU_API_KEY}
    params = {"query": query,
		"num_web_results":num_results}
    return requests.get(
        f"https://api.ydc-index.io/rag?query={query}",
        params=params,
        headers=headers,
    ).json()

query="Find me a computer monitor that is at least 34 inches across and is a good value.  Give me shopping links to Amazon.com"
print("Query: "+query)

#
# Hit the search endpoint
#
# results = get_ai_snippets_for_query("Name three news items of note from November 17, 2023")
results = get_ai_snippets_for_query(query)
print_list_elements(results['hits'],'url')

#
# Hit the rag endpoint
#
results = get_rag_snippets_for_query(query)
print_list_elements(results['hits'],'url')
