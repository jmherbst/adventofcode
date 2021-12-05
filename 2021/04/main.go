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
	Part1(input)
	Part2(input)
}

var Reset = "\033[0m"
var Green = "\033[32m"

type board struct {
	board   [][]int
	bingoed [][]bool
	winning bool
}

func newBoard() board {
	b := board{}
	return b
}

func createRow(row []int) map[int]bool {
	rowMap := map[int]bool{}
	for _, i := range row {
		rowMap[i] = false
	}
	return rowMap
}

func addRow(b board, row []int) board {
	a := []bool{false, false, false, false, false}
	b.board = append(b.board, row)
	b.bingoed = append(b.bingoed, a)

	return b
}

func markBoardWithHit(b board, num int) board {
	for i, row := range b.board {
		for j, v := range row {
			if v == num {
				b.bingoed[i][j] = true
				return b
			}
		}
	}

	return b
}

func getUnmarkedNumbers(b board) int {
	unmarked := 0
	for i, row := range b.board {
		for j, v := range row {
			if b.bingoed[i][j] == false {
				unmarked += v
			}
		}
	}
	return unmarked
}
func checkSliceForBingo(row []bool) bool {
	for _, v := range row {
		if !v {
			return false
		}
	}
	return true
}

func checkBoardForBingo(b board) bool {
	// checking each row
	for i, _ := range b.board {
		if checkSliceForBingo(b.bingoed[i]) {
			return true
		}
	}

	prettyPrint(b)
	// checking each column
	for i := 0; i < len(b.board); i++ {
		col := make([]bool, 0, len(b.board))

		for j := 0; j < len(b.board); j++ {
			col = append(col, b.bingoed[j][i])
		}

		if checkSliceForBingo(col) {
			return true
		}

	}

	return false
}

func getBingoNumbers(input []string) []int {
	return getIntArray(input)
}

func getRowNumbers(input []string) []int {
	return getIntArray(input)
}

func getIntArray(input []string) []int {
	numbers := []int{}
	for _, i := range input {
		num, err := strconv.Atoi(string(i))
		if err != nil {
			log.Fatal(err)
		}
		numbers = append(numbers, num)
	}
	return numbers
}

func prettyPrint(b board) {
	log.Printf("--------------\n")
	for i, row := range b.board {
		keys := make([]string, len(row))
		index := 0
		for k, v := range row {
			keys[index] = strconv.Itoa(v)
			if b.bingoed[i][k] {
				keys[index] = Green + keys[index] + Reset
			}
			index++
		}
		log.Printf("%s\n", strings.Join(keys, " "))
	}
	log.Printf("--------------\n")
}

// Part1 solves:
func Part1(input []string) {
	boards := []board{}
	numberInput := strings.Split(input[0], ",")
	numbers := getBingoNumbers(numberInput)

	input = input[1:]
	for _, row := range input {
		row := strings.TrimSpace(row)

		if row == "" {
			// Removes empty newlines
			continue
		}

		boardRow := getRowNumbers(strings.Split(strings.Join(strings.Fields(row), " "), " "))

		var currentBoard board
		if len(boards) == 0 || len(boards[len(boards)-1].board) == 5 {
			boards = append(boards, newBoard())
		}

		currentBoard = boards[len(boards)-1]

		currentBoard = addRow(currentBoard, boardRow)

		boards[len(boards)-1] = currentBoard
	}

	for _, num := range numbers {
		for i, b := range boards {
			boards[i] = markBoardWithHit(b, num)
			if checkBoardForBingo(boards[i]) {
				log.Printf("Bingo! %d\n", num)
				prettyPrint(boards[i])

				sum := getUnmarkedNumbers(boards[i])
				log.Printf("Sum of unmarked numbers: %d", sum)
				log.Printf("Unmarked * Number: %d", sum*num)
				return
			}
		}

	}
}

// Part2 solves:
func Part2(input []string) {
	boards := []board{}
	numberInput := strings.Split(input[0], ",")
	numbers := getBingoNumbers(numberInput)

	input = input[1:]
	for _, row := range input {
		row := strings.TrimSpace(row)

		if row == "" {
			// Removes empty newlines
			continue
		}

		boardRow := getRowNumbers(strings.Split(strings.Join(strings.Fields(row), " "), " "))

		var currentBoard board
		if len(boards) == 0 || len(boards[len(boards)-1].board) == 5 {
			boards = append(boards, newBoard())
		}

		currentBoard = boards[len(boards)-1]

		currentBoard = addRow(currentBoard, boardRow)
		currentBoard.winning = false

		boards[len(boards)-1] = currentBoard
	}

	for _, num := range numbers {
		count := 0
		for i, b := range boards {
			if b.winning {
				continue
			}
			b = markBoardWithHit(b, num)
			if checkBoardForBingo(b) {
				log.Printf("Bingo! %d\n", num)
				prettyPrint(b)

				sum := getUnmarkedNumbers(b)
				log.Printf("Sum of unmarked numbers: %d", sum)
				log.Printf("Unmarked * Number: %d", sum*num)

				b.winning = true
				count++

			}
			boards[i] = b

			// prettyPrint(boards[i])
		}

		log.Printf("Num %d -- Winning Boards: %d", num, count)
	}

	// for i, b := range boards {
	// 	log.Printf("Board(%d): %b", i, b.winning)
	// }

	return
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
