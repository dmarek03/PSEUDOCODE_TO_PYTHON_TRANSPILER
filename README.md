# PSEUDOCODE_TO_PYTHON_TRANSPILER
# Pseudocode to Python Transpiler

Pseudocode to Python Transpiler is an innovative tool designed to automatically convert pseudocode into equivalent Python code. It facilitates rapid prototyping and testing of algorithms originally written in pseudocode, making programming more accessible and efficient.

## Features

- **Localized Syntax**: Write pseudocode and convert it seamlessly into Python.
- **Compilation**: Translates pseudocode into Python scripts.
- **Execution**: Optionally execute the compiled Python scripts directly.
- **Error Handling**: Detailed syntax error reporting for pseudocode.
- **Extensibility**: Modular design allows for easy extension with new features and translations.

## Supported Structures
The following pseudocode structures are supported by the transpiler:

### Data Types
- INTEGER
- REAL
- CHAR
- STRING
- BOOLEAN
- ARRAY

### Control Structures
- IF...THEN...ELSE...ENDIF
- WHILE...DO...ENDWHILE
- FOR...TO...STEP...NEXT
- REPEAT...UNTIL
- CASE...OF...ENDCASE

### Input/Output
- INPUT
- OUTPUT

### Functions and Procedures
- FUNCTION...RETURNS...ENDFUNCTION
- PROCEDURE...ENDPROCEDURE
- CALL

### Operators
- Arithmetic: `+`, `-`, `*`, `/`
- Comparison: `=`, `<>`, `<`, `<=`, `>`, `>=`
- Logical: `AND`, `OR`, `NOT`

### Built-in Functions
- LENGTH
- LCASE
- UCASE
- SUBSTRING
- ROUND
- RANDOM

### File Handling
- OPENFILE
- READFILE
- WRITEFILE
- CLOSEFILE

### Comments
- Single-line: `//`
- Multi-line: `*** ... ***`


## Project Structure

```
pseudocode-to-python-transpiler/
├── grammar/                 # ANTLR grammar 
├── grammar_utils/           # File generated from ANTLR
├── input_files/             # Examples files written in pseudocode
├── output_files/            # Generated Python scripts from pseudocode
├── pseudocode_specification # Pseudcode rules
├── translator               # Entry point for the Pseudocode to Python CLI tool
├── .gitignore               # Git ignore rules
├── LICENSE                  # Copying and reusing rules
├── README.md                # Project documentation 
```

## Requirements

- **Python**: Version 3.10+
- **ANTLR**: For generating parsers from the grammar files

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/dmarek03/PSEUDOCODE_TO_PYTHON_TRANSPILER.git
   cd PSEUDOCODE_TO_PYTHON_TRANSPILER
   ```


## Usage

### Command-line Arguments

Run the Pseudocode to Python CLI tool using:

```bash
python translator.py [options]
```

| Argument   | Description                                | Required | Default      |
|------------|--------------------------------------------|----------|--------------|
| `--file`   | Path to the input pseudocode script.        | Yes      | N/A          |
| `--output` | Path to save the compiled Python script.    | No       | ./output     |
| `--run`    | Execute the compiled script after compilation. | No       | False        |

### Example

Compile a pseudocode script:

```bash
python translator.py --file input_files/input.pseudo --output output_files/output.py
```

Compile and execute a script:

```bash
python translator.py --file input_files/input --run
```

## Examples

**Input (Pseudocode)**:

```
DECLARE x: INTEGER
INPUT x
IF x < 10 THEN
    OUTPUT "Liczba mniejsza niż 10"
ELSE
    OUTPUT "Liczba większa lub równa 10"
ENDIF
```

**Output (Python)**:

```python
x = int(input('Enter data: '))
if x < 10:
    print("Liczba mniejsza niż 10")
else:
    print("Liczba większa lub równa 10")
```

**Input (Pseudocode)**:
```
DECLARE Limit: INTEGER

INPUT Limit

DECLARE IsPrime : ARRAY[Limit] OF BOOLEAN

FOR Number ← 2 TO Limit
    IsPrime[Number] ← TRUE
NEXT Number

FOR Number ← 2 TO Limit
    IF IsPrime[Number] = TRUE
      THEN

        OUTPUT Number


        FOR Multiple ← 2 TO DIV(Limit, Number)
            IsPrime[Number * Multiple] ← FALSE
        NEXT Multiple
    ENDIF
NEXT Number
```

**Output (Python)**:
```python
Limit = int(input("Enter data: "))
IsPrime = [False for _ in range(Limit)]
for Number in range(2, Limit):
    IsPrime[Number] = True
for Number in range(2, Limit):
    if IsPrime[Number] == True:
        print(f"{Number}")
        for Multiple in range(2, (Limit // Number)):
            IsPrime[(Number * Multiple)] = False
```

**Input (Psedudocode)**:
```
// Declaration and implementation of function calculating factorial of given number
FUNCTION Factorial(Num:INTEGER) RETURNS INTEGER
    IF Num = 0 OR Num = 1
      THEN
        RETURN 1
      ELSE
        RETURN Num * Factorial(Num - 1)
    ENDIF
ENDFUNCTION

// Getting number from user
INPUT Number
Number ← INTEGER(Number)

OUTPUT Factorial(Number)
```
**Output (Python)**:
```python
# Declaration and implementation of function calculating factorial of given number
def Factorial(Num: int) -> int:
    if Num == 0 or Num == 1:
        return 1
    else:
        return Num * Factorial((Num - 1))


# Getting number from user
Number = input("Enter data: ")
Number = int(Number)
print(Factorial(Number))
```

**Input (Pseudocode)**:
```
OUTPUT "Enter a number: "
INPUT NumA

OUTPUT "Enter another number: "
INPUT NumB

NumA ← REAL(NumA)
NumB ← REAL(NumB)

OUTPUT "Enter operator: "
INPUT Operator


CASE OF Operator
  "add": OUTPUT NumA + NumB
  "sub": OUTPUT NumA - NumB
  "mul": OUTPUT NumA * NumB
  "div": OUTPUT NumA / NumB
  "mod": OUTPUT MOD(NumA, NumB)
  OTHERWISE: OUTPUT "Unknown operator"
ENDCASE
```

**Output (Python)**:
```python
print("Enter a number: ")
NumA = input("Enter data: ")
print("Enter another number: ")
NumB = input("Enter data: ")
NumA = float(NumA)
NumB = float(NumB)
print("Enter operator: ")
Operator = input("Enter data: ")
match Operator:
    case "add":
        print((NumA + NumB))
    case "sub":
        print((NumA - NumB))
    case "mul":
        print((NumA * NumB))
    case "div":
        print((NumA / NumB))
    case "mod":
        print((NumA % NumB))
    case _:
        print("Unknown operator")

```


## Technologies Used

- **Python**: Core language for implementation.
- **ANTLR**: Grammar-based parser generation.

## License

The project is released under the MIT License.

**Note**: Ensure the pseudocode is correctly formatted and adheres to the supported syntax to avoid translation errors.
