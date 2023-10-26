using BenchmarkTools

cache = Dict{UInt64,Float64}()
function solve(r1::T, r2::T, r3::T, r4::T, cur_r::T) where {T<:Integer}
    # ri is the number of ranks with i cards left

    key = hash([r1, r2, r3, r4, cur_r])
    if haskey(cache, key)
        return cache[key]
    end

    if r1 == 0 && r2 == 0 && r3 == 0 && r4 == 0
        cache[key] = 0
        return 0
    end

    total_cards_left = r1 + 2r2 + 3r3 + 4r4
    res = 0
    if r1 > 0
        cur = solve(r1 - 1, r2, r3, r4, 0)
        if cur_r == 1
            cur *= (r1 - 1) / r1
        end
        res += (cur + 1) * r1 / total_cards_left
    end

    if r2 > 0
        cur = solve(r1 + 1, r2 - 1, r3, r4, 1)
        if cur_r == 2
            cur *= (r2 - 1) / r2
        end
        res += (cur + 1) * 2r2 / total_cards_left
    end

    if r3 > 0
        cur = solve(r1, r2 + 1, r3 - 1, r4, 2)
        if cur_r == 3
            cur *= (r3 - 1) / r3
        end
        res += (cur + 1) * 3r3 / total_cards_left
    end

    if r4 > 0
        cur = solve(r1, r2, r3 + 1, r4 - 1, 3)
        res += (cur + 1) * 4r4 / total_cards_left
    end

    cache[key] = res
    return res
end

# initially, 4 cards left for each rank, so r4 = 13
println(round(solve(0, 0, 0, 13, -1), digits=8))
@btime round(solve(0, 0, 0, 13, -1), digits=8)
