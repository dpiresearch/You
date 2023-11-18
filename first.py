import requests
import os

YOU_API_KEY = os.getenv("YOU_API_KEY")

def print_list_elements(my_list):
    # Find the size of the list
    list_size = len(my_list)
    print("Size of the list:", list_size)

    # Print each element with a space
    for element in my_list:
        print("=====================================")
#        print(element['description'], end=' ')
        print(element, end=' ')
        print()
        print("=====================================")
        print()  # This ensures there's a newline after the last element

def get_ai_snippets_for_query(query):
#    headers = {"X-API-Key": "5447f8dd-ba5a-406a-944a-d1ba07b0002e<__>1ODmHdETU8N2v5f4K7rDr9X0"}
    headers = {"X-API-Key": YOU_API_KEY}
    params = {"query": query,
		"num_web_resuts":3}
    return requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        params=params,
        headers=headers,
    ).json()

# results = get_ai_snippets_for_query("Name three news items of note from November 17, 2023")
results = get_ai_snippets_for_query("Find me a computer monitor that is at least 34 inches across and is a good value.  Give me shopping links to Amazon.com")
print_list_elements(results['hits'])
