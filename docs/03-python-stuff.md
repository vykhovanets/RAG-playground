- remove duplicates
```Python
old_lst = [...]
duplicate_indices = []

for i, _ in enumerate(new_lst)
	if any(is_same(new_lst, old_lst) for elem in old_lst)
		duplicate_indices.append(i)

def rm_by_index_inplace(list, indices):
    for i in sorted(indices, reverse=True):
        del list[i]
```

