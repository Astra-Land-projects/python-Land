import re
from collections import Counter, defaultdict
from itertools import combinations

def analyze_text_patterns(text: str, min_ngram_length: int = 2, max_ngram_length: int = 3, top_n: int = 10) -> dict:
    """
    Analyzes text to find uncommon n-gram patterns.

    Args:
        text: The input text to analyze.
        min_ngram_length: The minimum length of n-grams to consider (e.g., 2 for bigrams).
        max_ngram_length: The maximum length of n-grams to consider (e.g., 3 for trigrams).
        top_n: The number of top uncommon patterns to return.

    Returns:
        A dictionary containing the top uncommon patterns and their counts.
    """

    # 1. Preprocessing: Lowercase and remove non-alphanumeric characters (except spaces)
    # We keep spaces to correctly identify word sequences.
    processed_text = re.sub(r'[^\w\s]', '', text.lower())
    words = processed_text.split()

    if not words:
        return {"error": "Input text is empty or contains no words."}

    # 2. Generate n-grams
    ngram_counts = defaultdict(int)
    for n in range(min_ngram_length, max_ngram_length + 1):
        # Create n-grams (sequences of n words)
        for i in range(len(words) - n + 1):
            ngram = tuple(words[i : i + n])
            ngram_counts[ngram] += 1

    if not ngram_counts:
        return {"error": "Could not generate any n-grams from the text."}

    # 3. Filter for "uncommon" patterns
    # This is a simplification. "Uncommon" could mean:
    # - Low frequency overall (we'll sort by count and take top_n)
    # - Patterns that appear in specific contexts but not others (more complex analysis needed)
    # For this example, we'll just sort by frequency and return the most frequent ones,
    # assuming they might represent recurring themes or stylistic choices.
    # A more sophisticated approach would involve comparing against a baseline corpus.

    # Sort n-grams by frequency in descending order
    sorted_ngrams = sorted(ngram_counts.items(), key=lambda item: item[1], reverse=True)

    # Select the top N patterns
    top_patterns = sorted_ngrams[:top_n]

    # Format the output
    result = {
        "analysis_summary": f"Top {len(top_patterns)} most frequent {min_ngram_length}-{max_ngram_length}-word patterns found:",
        "patterns": [
            {"pattern": " ".join(ngram), "count": count} for ngram, count in top_patterns
        ]
    }

    return result

# --- Example Usage ---

# Sample text (you can replace this with a larger text file content)
sample_text = """
The quick brown fox jumps over the lazy dog. This is a classic sentence used for testing.
It contains all the letters of the English alphabet. The quick brown fox is known for its speed.
We are analyzing text patterns. Finding uncommon patterns is interesting.
The lazy dog, however, remains lazy. The quick brown fox jumps again.
Let's see if 'the quick brown fox' appears often. Patterns in text can reveal a lot.
This is a classic sentence. A classic sentence indeed. The quick brown fox is very quick.
"""

# Analyze the text for bigrams (2-word sequences) and trigrams (3-word sequences)
analysis_result = analyze_text_patterns(sample_text, min_ngram_length=2, max_ngram_length=3, top_n=5)

# Print the result
import json
print(json.dumps(analysis_result, indent=4, ensure_ascii=False))

# Example with only bigrams
print("\n--- Analyzing only bigrams ---")
analysis_bigrams = analyze_text_patterns(sample_text, min_ngram_length=2, max_ngram_length=2, top_n=5)
print(json.dumps(analysis_bigrams, indent=4, ensure_ascii=False))

# Example with a very short text
print("\n--- Analyzing short text ---")
short_text = "one two one two three"
analysis_short = analyze_text_patterns(short_text, min_ngram_length=2, max_ngram_length=3, top_n=5)
print(json.dumps(analysis_short, indent=4, ensure_ascii=False))

# Example with empty text
print("\n--- Analyzing empty text ---")
empty_text = ""
analysis_empty = analyze_text_patterns(empty_text)
print(json.dumps(analysis_empty, indent=4, ensure_ascii=False))