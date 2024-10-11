
if true then
    print("Always ")
else
    print("Never ")
end 

b = false
if true or b then
    print("Always ")
end

b = true
if true and b then
    print("Always ")
end