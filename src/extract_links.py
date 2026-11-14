import re

def extract_markdown_images(text: str) -> List[tuple(str,str)]:
   return re.findall(r'\!\[(.+?)\]\((.+?)\)', text)

def extract_markdown_links(text:str) -> List[tuple(str,str)]:
    matches = re.findall(r'\[(.+?)\]\((.+?)\)', text)
    print(matches)
    return matches
   
