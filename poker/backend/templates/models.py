from .utils import get_db_connection

def create_tables():
    conn = get_db_connection()
    print("Success")
    cursor = conn.cursor()

    # Create users table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        )
        """
    )

    # Create game table (assuming 'Game' is a review of a game)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS game (
            review_id INT AUTO_INCREMENT PRIMARY KEY,
            number_of_stars INT NOT NULL,
            review_text TEXT,
            date_written DATE NOT NULL,
            album_id INT,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
        """
    )

    # Create tutorial table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tutorial (
            tutorial_id INT AUTO_INCREMENT PRIMARY KEY,
            description TEXT NOT NULL,
            image VARCHAR(255),
            step_number INT NOT NULL
        )
        """
    )

    conn.commit()
    cursor.close()
    conn.close()

create_tables()
