using BenchmarkTools

function main()
    n = 100
    binomial(n + 9, 9) + binomial(n + 10, 10) - 10 * n - 2
end

@btime main()
