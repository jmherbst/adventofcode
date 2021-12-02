package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

// Solve prints out solutions for the puzzle
func Solve(inputfile string) {
	input := ReadInput(inputfile)
	// Part1(input)
	Part2(input)
}

// Part1 solves:
func Part1(input []string) {
	horizontal := 0
	depth := 0

	for _, line := range input {
		instruction := strings.Fields(line)
		direction := instruction[0]
		x, _ := strconv.Atoi(instruction[1])

		switch direction {
		case "forward":
			horizontal += x
		case "down":
			depth = depth + x
		case "up":
			if x > depth {
				log.Printf("%d is greater than %d", x, depth)
			}

			depth = depth - x
		}

		log.Printf("%s -- %d", direction, x)
		log.Printf("Coordinates: %d, %d -- Multiplied: %d", horizontal, depth, horizontal*depth)
	}

	log.Printf("Coordinates: %d, %d -- Multiplied: %d", horizontal, depth, horizontal*depth)

}

// Part2 solves:
func Part2(input []string) {
	horizontal := 0
	depth := 0
	aim := 0

	for i, line := range input {
		if i > 10 {

		}
		instruction := strings.Fields(line)
		direction := instruction[0]
		x, _ := strconv.Atoi(instruction[1])

		switch direction {
		case "forward":
			horizontal += x
			depth = depth + (aim * x)
		case "down":
			aim = aim + x
		case "up":
			aim = aim - x
		}

		log.Printf("%s -- %d", direction, x)
		log.Printf("Coordinates: %d, %d -- Aim: %d -- Multiplied: %d", horizontal, depth, aim, horizontal*depth)
	}

	log.Printf("Coordinates: %d, %d -- Aim: %d -- Multiplied: %d", horizontal, depth, aim, horizontal*depth)
}

// ReadInput parses the puzzle's input.txt file
func ReadInput(fname string) []string {
	var input []string
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
			input = append(input, item)
		}
	}

	return input
}

// I include main() so that go doesn't yell about a main package having no main() function
func main() {
}
