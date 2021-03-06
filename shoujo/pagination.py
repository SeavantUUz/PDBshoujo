#coding:utf-8
__all__ = ['Pagination']

class Pagination(object):
    def __init__(self,items,page=1,per_page=7):
        self.total_items = items
        self.page = page
        self.per_page = per_page

    @property
    def title(self):
        return 'page_'+str(self.page)
    
    @property
    def pages(self):
        return int((self.total - 1) / self.per_page)+1
    
    @property
    def total(self):
        return len(self.total_items)
    
    @property
    def has_prev(self):
        return self.page > 1

    @property
    def prev_title(self):
        return 'page_'+str(self.page-1)

    @property
    def prev_num(self):
        return self.page - 1

    @property
    def has_next(self):
        return self.page < self.pages

    @property
    def next_title(self):
        return 'page_'+str(self.page+1)

    @property
    def next_num(self):
        return self.page + 1

    @property
    def items(self):
        start = (self.page-1) * self.per_page
        end = self.page * self.per_page
        return self.total_items[start:end]
