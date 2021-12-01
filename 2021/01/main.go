package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

// Solve prints out solutions for the puzzle
func Solve(inputfile string) {
	input := ReadInput(inputfile)
	Part1(input)
}

// Part1 solves:
func Part1(input []int) {
	previous := 0
	increases := 0

	for _, depth := range input {
		// First loop will be 0
		if previous == 0 {
			// Initial seed of "previous" value
			previous = depth
			continue
		}

		if depth > previous {
			increases++
			log.Printf("%d (increased) -- TOTAL %d", depth, increases)
		} else {
			log.Printf("%d (decreased) -- TOTAL %d", depth, increases)
		}

		previous = depth
	}

	log.Printf("Part 1: %d", increases)
}

// Part2 solves:
func Part2() {

}

// ReadInput parses the puzzle's input.txt file
func ReadInput(fname string) []int {
	var input []int
	file, err := os.Open(fname)
	if err != nil {
		return input
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		item := scanner.Text()

		if item == "\n" {
			// Removes empty newline from end of array
			continue
		} else {
			i, err := strconv.Atoi(item)
			if err != nil {
				log.Fatal(err)
			}

			input = append(input, i)
		}
	}

	return input
}

// I include main() so that go doesn't yell about a main package having no main() function
func main() {}
