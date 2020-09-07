def merge(list1, list2):
  result_list = []
  i = j = 0
  len_l1 = len(list1)
  len_l2 = len(list2)
  while i < len_l1 and j < len_l2:
    if list1[i] < list2[j]:
      result_list.append(list1[i])
      i += 1
    else:
      result_list.append(list2[j])
      j += 1
  result_list = result_list + [item for item in list1[i:]]
  result_list = result_list + [item for item in list2[j:]]
  return result_list

if __name__ == "__main__":
  l1 = [1, 4,5,6,7,9]
  l2 = [3,5,7,9,12,23]
  print(merge(l1, l2))
