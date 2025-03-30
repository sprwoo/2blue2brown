import os

class CombinedCodeGenerator:
    def __init__(self, code_strings):
        self.code_strings = code_strings

    def generate_combined_code(self):
        import_lines = set()
        code_blocks = []

        for code in self.code_strings:
            lines = code.splitlines()
            block = []
            for line in lines:
                if line.strip().startswith("from manim import"):
                    import_lines.add(line.strip())
                else:
                    block.append(line)
            # Append the processed block (strip trailing whitespace)
            code_blocks.append("\n".join(block).strip())

        # Combine unique import lines at the top
        combined = "\n".join(sorted(import_lines)) + "\n\n"
        # Append each code block separated by two newlines
        combined += "\n\n".join(code_blocks)
        return combined

    def save_to_file(self, folder="generated_manim", filename="manim.py"):
        if not os.path.exists(folder):
            os.makedirs(folder)

        combined_code = self.generate_combined_code()
        filepath = os.path.join(folder, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(combined_code)
        return filepath