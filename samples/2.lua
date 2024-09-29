function sort(a)
  n = #a
  for j = 1, n do
    for i = 1, n - j do
      if a[i] > a[i + 1] then
        tmp = a[i]
        a[i] = a[i + 1]
        a[i + 1] = tmp
      end
    end
  end
  return a
end

ar = {3,1,5,6,2}
ar = sort(ar)
for i = 1, #ar do
  print(ar[i])
end