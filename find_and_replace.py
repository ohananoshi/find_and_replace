# Function: find_and_replace
# Author: Guilherme Arruda
# Created in: 12/07/2024
# Last updated: 13/07/2024
# Github: https://github.com/ohananoshi/find_and_replace

#libs
import re

#dictionaries
EXAMPLE_DICT = {
    "old_word1": "new_word1",
    "old_word2": "new_word2"
}

#functions

def find_and_replace(content: str, conversion_dict: dict):
    """
    Replaces the words found with those in the dictionary.
    
    Args:
    content (str): The content where the keywords will be searched for.
    conversion_dict (dict): A dictionary where the keys are the words
    to be found and the values their replacements.
    
    Returns:
    str: The content with the replaced words.
    """
    
    # Create a regular expression to find the words
    pattern = re.compile(
        r"\b(" + "|".join(re.escape(key) for key in conversion_dict.keys()) + r")\b", 
        re.IGNORECASE
    )
    
    def replace(match):
        """
        Replaces the type of the word found with the corresponding
        one in the conversation dictionary.
        
        Args:
        match (re.Match): Matching object found by the regular expression.
        
        Returns:
        str: If found in the dictionary, the new word. If not,
        the old word is kept.
        """
        old_word = match.group(0)
        new_word = conversion_dict.get(old_word.lower(), old_word)
        return new_word

    # Replace all data types found in the content
    converted_content = pattern.sub(replace, content)
    
    return converted_content