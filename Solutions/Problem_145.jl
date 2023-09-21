using BenchmarkTools

function is_reversible(n::Int)
    n % 10 == 0 && return false

    num = n
    reverse_n = 0
    while num > 0
        reverse_n *= 10
        reverse_n += num % 10
        num ÷= 10
    end

    res = n + reverse_n
    while res > 0
        iseven(res % 10) && return false
        res ÷= 10
    end

    return true
end

function main()
    count(is_reversible, 1:10^9-1)
end

@btime main()
