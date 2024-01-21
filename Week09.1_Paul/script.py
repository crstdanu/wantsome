import argparse


def main():
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(
        description='A simple example of argparse.')

    # Add positional argument
    parser.add_argument('name', type=str, help='Your name')
    parser.add_argument('Firstname', type=str,
                        help='Your firstname. Ex: Mihai')

    # Add optional argument with a default value
    parser.add_argument('--greeting', type=str,
                        default='Hello', help='Greeting message')

    # Add optional argument with choices
    parser.add_argument(
        '--language', choices=['english', 'spanish'], default='english', help='Language')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values using dot notation
    greeting = args.greeting
    name = args.name
    firstname = args.Firstname
    language = args.language

    # Display the greeting message
    if language == 'english':
        print(f'{greeting}, {name} {firstname}!')
    elif language == 'spanish':
        print(f'Hola, {name} {firstname}!')


if __name__ == "__main__":
    main()
