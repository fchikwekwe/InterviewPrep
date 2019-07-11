

def markdownparser(markdown):
  index = 0 
  char = markdown[index]
  
  while index < len(markdown) and not char.isspace():
    print(markdown)
    if char != '#':
      # invalid markdown because a non-space character is seen too early
      return markdown
    index += 1
    char = markdown[index]
    
  if index == len(markdown):
    # invalid because markdown is all # characters 
    print("length", markdown)
    return markdown
   
  return translate(index, markdown)

def translate(index, markdown):
    """
    Input: string containing validated markdown
    """
    just_text = markdown[index+1:]
    print(just_text)

    return '<h' + str(index) + '>' + just_text + '</h' + str(index) + '>'


print(markdownparser('####### Snow White and the Seven Hashtags'))
