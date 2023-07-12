```python
from scrapy import Item, Field

class RedditScraperItem(Item):
    # define the fields for your item here like:
    title = Field()
    url = Field()
    upvotes = Field()
    comments = Field()
    subreddit = Field()
```