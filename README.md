# Rick and Morty CLI

![Run Python Tests](https://github.com/keegean/is4010-mcgorrkj-labs/actions/workflows/tests.yml/badge.svg)

A command-line tool to fetch character information from the public Rick and Morty API.

## 🚀 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/keegean/is4010-mcgorrkj-labs.git
    cd is4010-mcgorrkj-labs
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

The tool provides three commands to get information about Rick and Morty characters.

### Get a Random Character

Fetches a random character and displays their key details.

```bash
python -m src.main random
```

### Get a Character by ID

Fetches a specific character by their ID number.

```bash
python -m src.main id 19
```

**Example Output:**

```
Name: Ant-Man (ID: 19)
Status: Dead
Species: Human
Origin: unknown
```

### Get Characters by Status

Lists the first few characters matching a given status.

```bash
python -m src.main status dead
```

**Example Output:**

```
Characters with status 'dead':
- Abradolf Lincler
- Adjudicator Rick
- Agency Director
- Alan Rails
- Albert Einstein
```