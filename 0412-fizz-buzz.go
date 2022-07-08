func fizzBuzz(n int) []string {
	res := []string{}
	for i := 1; i <= n; i++ {
		d3 := i%3 == 0
		d5 := i%5 == 0
		if d3 && d5 {
			res = append(res, "FizzBuzz")
		} else if d3 {
			res = append(res, "Fizz")
		} else if d5 {
			res = append(res, "Buzz")
		} else {
			res = append(res, fmt.Sprintf("%d", i))
		}
	}
	return res
}
