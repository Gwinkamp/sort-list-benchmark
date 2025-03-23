#include <vector>

int find_smallest_element(std::vector<int> &arr)
{
  int smallest_element = arr[0];
  size_t smallest_idx = 0;

  for (size_t i = 1; i < arr.size(); ++i)
  {
    int item = arr[i];
    if (item < smallest_element)
    {
      smallest_element = item;
      smallest_idx = i;
    }
  }

  return smallest_idx;
}

std::vector<int> selection_sort(std::vector<int> arr)
{
  if (arr.empty())
  {
    return arr;
  }

  std::vector<int> sorted_arr;
  sorted_arr.reserve(arr.size());

  while (!arr.empty())
  {
    int smallest_idx = find_smallest_element(arr);
    sorted_arr.push_back(arr[smallest_idx]);
    arr.erase(arr.begin() + smallest_idx);
  }

  return sorted_arr;
}