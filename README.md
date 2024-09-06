# Library Management System

A Python-based console application to manage a small community library. This system provides functionalities for cataloging books, managing members, handling book borrowing and returning, and generating simple reports. The project is designed to be modular and scalable, making it easy to extend.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

This project implements the following key features:

- **Book Cataloging**: 
  - Add, update, and remove books.
  - Track book details (ID, title, author, genre, and availability).
- **Member Management**: 
  - Register, update, and remove members.
  - Store information such as borrowed books.
- **Book Borrowing and Returning**: 
  - Allow members to borrow available books and return them.
  - Automatically update book availability and member borrowing history.
- **Simple Reporting**: 
  - View all currently borrowed books.
  - Generate reports on overdue books and the most frequently borrowed books.
- **Role-based Access**:
  - **Admins** can add/remove books, register members, and manage borrowing/returning for users.
  - **Regular Users** can borrow and return books.
- **Persistent Data**: 
  - Data is saved to files, ensuring that books and members are loaded automatically when the system starts.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Make sure you have the following installed:
- **Python 3.x**: Download and install it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/library_management_system.git
   cd library_management_system
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Usage

### Admin Access

Admins can:
- Add new books to the catalog.
- Remove existing books.
- Register new members.
- View reports on borrowed and overdue books.
- Borrow and return books on behalf of users.

### User Access

Regular users can:
- Borrow books from the library.
- Return borrowed books.
- View the list of books they have borrowed.

### Commands

When you run the program, you’ll be presented with a menu. Use the following commands to navigate through the system:

#### Admin Menu:
- `1` – Add a book.
- `2` – Remove a book.
- `3` – Register a new member.
- `4` – View all members.
- `5` – Borrow a book (for users).
- `6` – Return a book (for users).
- `7` – Save data and exit.

#### User Menu:
- `1` – Borrow a book.
- `2` – Return a book.
- `3` – View borrowed books.
- `4` – Save data and exit.

## Project Structure

Here is the high-level structure of the project:
```
library_management_system/
│
├── main.py           # The main entry point of the program
├── book.py           # Contains the Book class and related functions
├── member.py         # Contains the Member class and related functions
├── library.py        # Manages the core library system, including books and members
├── transaction.py    # Handles book borrowing and returning
├── data_handler.py   # Manages saving and loading data to/from files
└── README.md         # This file
```

## Contributing

If you’d like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

