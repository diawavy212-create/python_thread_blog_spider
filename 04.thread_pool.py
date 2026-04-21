import concurrent.futures
import blog_spider
#craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls=pool.map(blog_spider.craw,blog_spider.urls)
    htmls=list(zip(blog_spider.urls,htmls))
    for url,html in htmls:
        print(url,len(html))
#f"https://www.cnblogs.com/sitehome/p/{page}"
print("craw over")

#parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures={}     #建立future 与 url 关系
    for url,html in htmls:
        future=pool.submit(blog_spider.parse,html)
        futures[future]=url

    #for future ,url in futures.items():
        #print(url,future.result())

    #不按顺序
    for future in concurrent.futures.as_completed(futures):
        url=futures[future]
        print(url, future.result())
