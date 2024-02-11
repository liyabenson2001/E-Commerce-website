from django import template

register=template.Library()

@register.filter(name='chunks')
def chunks(lst_data,chunk_size):
    chunk=[]
    i=0
    for data in lst_data:
        chunk.append(data)
        i= i+1
        if i==chunk_size:
            yield chunk
            i=0
            chunk=[]
    yield chunk
