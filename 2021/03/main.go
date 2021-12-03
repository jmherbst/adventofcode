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
	a := Part2(input)
	log.Printf("Part 2 -- Solution: %s", a)
}

// Part1 solves:
func Part1(input []string) {
	gamma := ""
	epsilon := ""
	total := len(input)

	// for _, binaryString := range input {
	// 	for j, char := range binaryString {
	// 		if string(char) == "1" {
	// 			onesCounter[j]++
	// 		}
	// 	}
	// }

	onesCounter := getOnesCount(input)

	for _, count := range onesCounter {
		if count > (total / 2) {
			gamma = gamma + "1"
			epsilon = epsilon + "0"
		} else {
			gamma = gamma + "0"
			epsilon = epsilon + "1"
		}
	}

	gammaI, _ := strconv.ParseInt(gamma, 2, 64)
	epsilonI, _ := strconv.ParseInt(epsilon, 2, 64)

	log.Printf("Gamma %s -- %d", gamma, gammaI)
	log.Printf(("Epsilon %s -- %d"), epsilon, epsilonI)

	log.Printf("Part 1 -- Power Consumption: %d * %d = %d", gammaI, epsilonI, gammaI*epsilonI)
}

// Part2 solves:
func Part2(input []string) []string {
	// To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position,
	//     and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
	// To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position,
	//     and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
	onesCounter := make([]int, len(input[0]))
	ox := ""
	c02 := ""
	total := len(input)

	log.Printf("Part 2 -- Life Support Rating: %d * %d = %d", oxI, c02I, oxI*c02I)

}

func getOnesCount(input []string) []int {
	onesCounter := make([]int, len(input[0]))

	for _, binaryString := range input {
		for j, char := range binaryString {
			if string(char) == "1" {
				onesCounter[j]++
			}
		}
	}

	return onesCounter
}

func getMostCommon(count int, total int) string {
	if count >= (total / 2) {
		return "1"
	} else {
		return "0"
	}
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
