from typing import Callable, List

# Define a type alias for the conversion function signature
ConversionFuncType = Callable[[str], str]


# The Wrapper Factory
def doc_format_checker_and_converter(
    conversion_function: ConversionFuncType, valid_formats: List[str]
) -> Callable[[str, str], str]:
    """
    Wrapper factory that checks file format and applies a conversion function.

    Args:
        conversion_function: The function to call if the format is valid.
                             Expected signature: (content: str) -> str.
        valid_formats: A list of valid file extensions (without the dot).

    Returns:
        A function that performs the check and conversion.
    """

    def wrapper(filename: str, content: str) -> str:
        """
        Wrapper function that performs the check and conversion.

        Args:
            filename: The name of the file (e.g., 'report.txt').
            content: The content of the file.

        Returns:
            The converted content.

        Raises:
            ValueError: If the filename has no extension or an invalid format.
        """
        print(f"--- Running wrapper for {filename} ---")
        # Use rsplit to handle potential multiple dots, get only the last part
        parts = filename.rsplit(".", 1)
        if len(parts) < 2:
            raise ValueError("Filename does not appear to have an extension.")

        file_ext: str = parts[1]
        print(f"Detected extension: {file_ext}")
        print(f"Valid formats: {valid_formats}")

        if file_ext in valid_formats:
            print(f"Format valid. Calling: {conversion_function.__name__}")
            # Call the specific conversion function passed to the outer function
            result: str = conversion_function(content)
            return result
        else:
            print("Format invalid. Raising ValueError.")
            raise ValueError(
                f"Invalid file format: '.{file_ext}'. "
                f"Expected one of {valid_formats}"
            )

    return wrapper


# The Conversion Functions
def capitalize_content(content: str) -> str:
    """Converts content to uppercase."""
    print("--- Running capitalize_content ---")
    return content.upper()


def reverse_content(content: str) -> str:
    """Reverses the content string."""
    print("--- Running reverse_content ---")
    return content[::-1]


# --- Example Usage ---

# Create wrapper functions explicitly
process_text_document = doc_format_checker_and_converter(
    capitalize_content, ["txt", "md"]
)
process_log_file = doc_format_checker_and_converter(reverse_content, ["log"])

# --- Execution Simulation ---

print("--- Calling process_text_document('report.txt', 'hello world') ---")
try:
    result1: str = process_text_document("report.txt", "hello world")
    print(f"Result 1: {result1}\n")
except ValueError as e:
    print(f"Error 1: {e}\n")

print("--- Calling process_text_document('image.png', 'some image data') ---")
try:
    result2: str = process_text_document("image.png", "some image data")
    print(f"Result 2: {result2}\n")
except ValueError as e:
    print(f"Error 2: {e}\n")

print("--- Calling process_log_file('server.log', 'error occurred') ---")
try:
    result3: str = process_log_file("server.log", "error occurred")
    print(f"Result 3: {result3}\n")
except ValueError as e:
    print(f"Error 3: {e}\n")

print("--- Calling process_log_file('notes.txt', 'important note') ---")
try:
    result4: str = process_log_file("notes.txt", "important note")
    print(f"Result 4: {result4}\n")
except ValueError as e:
    print(f"Error 4: {e}\n")
