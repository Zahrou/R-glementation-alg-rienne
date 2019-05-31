


def sort_queryset_list(queryset_list):
    date_list = sorted([t.date for t in queryset_list], reverse=True)
    sorted_list = []
    while len(queryset_list) != 0:
        for i in queryset_list:
            if i.date == max(date_list):
                sorted_list.append(i)
                queryset_list.remove(i)
                date_list.remove(i.date)
    return sorted_list
                
