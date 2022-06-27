instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS TODO;',
    'DROP TABLE IF EXISTS USER;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
        CREATE TABLE user( 
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL, 
            password VARCHAR(500) NOT NULL
        )        
    """,
    """
        CREATE TABLE todo(
            id INT PRIMARY KEY AUTO_INCREMENT, 
            created_by INT NOT NULL, 
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, 
            descripcion TEXT NOT NULL, 
            completed BOOLEAN NOT NULL, 
            FOREIGN KEY (created_by) REFERENCES user(id)
        )
    """
]