def find_related_urls(title):
    """
    args: title of article
    returns: links of  most related articles from trusted sources
    """
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found")  
    print(title)
    related_urls = []
    # to search 
    query1 = "ndtv: "+ title
    query2 = "timesofindia: "+title
    query3 = "hindustantimes: " + title
    for q in search(query1, tld="com", num=10, stop=1, pause=2): 
        related_urls.append(q)
        
    for r in search(query2, tld="co.in", num=10, stop=1, pause=2): 
        related_urls.append(r)
    for s in search(query3, tld="com", num=10, stop=1, pause=2): 
        related_urls.append(s)
    return related_urls