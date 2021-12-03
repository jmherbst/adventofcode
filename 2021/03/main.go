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
	Part2(input)
}

// Part1 solves:
func Part1(input []string) {
	gamma := ""
	epsilon := ""
	total := len(input)
	a := input[0]
	// b := len(a)

	for i, _ := range a {
		count := getOnesCount(input, i)
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
func Part2(input []string) {
	ox := getMatchingSignals(input, true, 0)[0]
	co2 := getMatchingSignals(input, false, 0)[0]

	oxI, _ := strconv.ParseInt(ox, 2, 64)
	co2I, _ := strconv.ParseInt(co2, 2, 64)

	log.Printf("Ox Signal: %s -- %d", ox, oxI)
	log.Printf("Co2 Signal: %s -- %d", co2, co2I)

	log.Printf("Part 2 -- Life Support Rating: %d * %d = %d", oxI, co2I, oxI*co2I)
}

func getOnesCount(input []string, position int) int {
	onesCounter := make([]int, len(input[0]))

	for _, binaryString := range input {
		for j, char := range binaryString {
			if string(char) == "1" {
				onesCounter[j]++
			}
		}
	}

	return onesCounter[position]
}

func getMatchingSignals(input []string, mostCommon bool, position int) []string {
	if len(input) == 1 {
		return input
	}

	numOfOnes := getOnesCount(input, position)

	var signal string
	length := (len(input) / 2) + (len(input) % 2)
	if numOfOnes >= length {
		if mostCommon {
			signal = "1"
		} else {
			signal = "0"
		}
	} else {
		if mostCommon {
			signal = "0"
		} else {
			signal = "1"
		}
	}

	var matchingSignals []string
	for _, binaryString := range input {

		if string(binaryString[position]) == signal {
			matchingSignals = append(matchingSignals, binaryString)
		} else {
		}
	}

	return getMatchingSignals(matchingSignals, mostCommon, position+1)
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
