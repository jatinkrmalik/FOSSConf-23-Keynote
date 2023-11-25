# Keep it simple, silly! 

class SimpleFileProcessor:
    def __init__(self):
        self.processed_files = {}  # Simple dictionary for file storage

    def process_file(self, file_path):
        if file_path in self.processed_files:
            return self.processed_files[file_path]

        # Basic file processing logic
        processed_data = self._simple_file_processing(file_path)
        self.processed_files[file_path] = processed_data
        return processed_data

    def _simple_file_processing(self, file_path):
        # Basic file processing logic
        # ... (details of processing)
        return processed_data

# Usage
processor = SimpleFileProcessor()
data = processor.process_file("example.txt")
