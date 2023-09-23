function num_divisors(n::Int)
    result = 1
    limit = isqrt(n)
    for i in 2:limit
        e = 0
        while n % i == 0
            e += 1
            n /= i
        end
        result *= e + 1
    end

    if n > 1
        result *= 2
    end

    return result
end


function main()
    n = 2
    f(x) = (num_divisors(x^2) + 1) ÷ 2
    while f(n) <= 1000
        n += 1
    end
    println(n)
end

main()