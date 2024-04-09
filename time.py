import requests

def quick_updates:
  response = requests.get("https://time.com")

  html_content = response.text
  start_string = '<li class="latest-stories__item">'
  end_string = '</li>'

  start_index = html_content.find(start_string)

  stories = []
  while start_index != -1:
    end_index = html_content.find(end_string, start_index)
    story_html = html_content[start_index:end_index]
          
    title_start_index = story_html.find('h3')
    title_end_index = story_html.find('</h3>', title_start_index)
    title = story_html[title_start_index:title_end_index].split('>')[-1].strip()

    link_start_index = story_html.find('<a href="')
    link_end_index = story_html.find('"', link_start_index + len('<a href="'))
    link = story_html[link_start_index + len('<a href="'):link_end_index]

    stories.append({"title": title, "link": link})

    start_index = html_content.find(start_string, end_index)

  return stories
  
if __name__ == "__main__":
  stories = quick_updates()
  for story in stories:
    print(f"Title: {story['title']}")
    print(f"Link: {story['link']}")
    print() 
