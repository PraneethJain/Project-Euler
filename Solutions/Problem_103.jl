using BenchmarkTools
using Combinatorics

function check(S)
    len = length(S)
    for set in permutations(S)
        for i = 1:len-1
            first, second = set[1:i], set[i+1:len]
            Bsubsets = collect(combinations(first))
            Csubsets = collect(combinations(second))
            for B in Bsubsets
                for C in Csubsets
                    sumB = sum(B)
                    sumC = sum(C)
                    if sumB == sumC
                        return false
                    end
                    if length(B) > length(C) && sumB <= sumC
                        return false
                    end
                end
            end
        end
    end
    return true
end

function main()
    previous = [11, 18, 19, 20, 22, 25]
    n = length(previous)
    b = n % 2 == 0 ? (previous[n÷2] + previous[n÷2+1]) ÷ 2 : previous[n÷2+1]
    pushfirst!(previous, 0)
    original = [i + b for i in previous]
    max = Inf
    ans = []
    for x1 = -3:3
        for x2 = -3:3
            for x3 = -3:3
                for x4 = -3:3
                    for x5 = -3:3
                        for x6 = -3:3
                            for x7 = -3:3
                                current = copy(original)
                                current[1] += x1
                                current[2] += x2
                                current[3] += x3
                                current[4] += x4
                                current[5] += x5
                                current[6] += x6
                                current[7] += x7
                                if length(Set(current)) != 7
                                    continue
                                end
                                sumA = sum(current)
                                if check(current) && sumA < max
                                    ans = current
                                    max = sumA
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    return join(ans)
end

@btime main()
