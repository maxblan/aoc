using DelimitedFiles

map = readdlm("Day3/input.txt")

trees = 0

collSteps =[]
rowSteps = [[1,1],[3,1],[5,1],[7,1],[1,2]]

result = Int32[]

for i in rowSteps
    coll = 1
    for x in map[1:i[2]:end]

        if (x[coll] == '#')
            global trees += 1
        end

        if (coll + i[1]) > (lastindex(x))
            coll = 0 + ((i[1] + coll) - (lastindex(x)) )
        else    
             coll += i[1]
        end
    end
    append!(result,[trees])
    global trees=0
end

final = 1
for n in result
    global final *= n
end    

println("Path's Results: ",result)
println("Absolute Result: ", final)