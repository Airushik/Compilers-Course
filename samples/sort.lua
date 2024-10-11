ar = {3,1,5,6,2}
n = #ar
for j = 1, n do
  for i = 1, n - j do
    if ar[i] > ar[i + 1] then
      tmp = ar[i]
      ar[i] = ar[i + 1]
      ar[i + 1] = tmp
    end
  end
end
for i = 1, n do
  print('%i ', ar[i])
end
