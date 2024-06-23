import os
import re
import requests
from bs4 import BeautifulSoup

# Set the base URL for the lessons
base_url = "https://metanit.com/php/tutorial/"

siteHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
response = requests.get(base_url, headers=siteHeaders)
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')

lesson_urls = []
ol_content = soup.find('ol', class_='content')
if ol_content:
    for li in ol_content.find_all('li'):
        a = li.find('a')
        if a:
            lesson_url = base_url + a['href']
            lesson_urls.append(lesson_url)
            # Вложені уроки
            sub_ol = li.find('ol', class_='subsubcontent')
            if sub_ol:
                for sub_li in sub_ol.find_all('li'):
                    sub_a = sub_li.find('a')
                    if sub_a:
                        sub_lesson_url = base_url + sub_a['href']
                        lesson_urls.append(sub_lesson_url)

skip_link = "https://metanit.com/php/tutorial///metanit.com/web/php/3.2.php"


def sanitize_filename(text):
    return re.sub(r'[\\/*?:"<>|]', "_", text)


for lesson_link in lesson_urls:
    if lesson_link == skip_link:
        continue
    response = requests.get(lesson_link, headers=siteHeaders)
    response.raise_for_status()
    lesson_soup = BeautifulSoup(response.content, 'html.parser')

    content = lesson_soup.find('div', class_='menC')
    if content:
        # Remove unwanted elements (e.g., navigation, sidebars)
        for element in content.find_all('div', class_='socBlock'):
            element.decompose()

        title_tag = content.find('h2')
        lesson_title = title_tag.get_text(
            strip=True) if title_tag else 'Untitled'

        sanitized_title = sanitize_filename(lesson_title)

        match = re.search(r'/(\d+)\.\d+\.php', lesson_link)
        chapter_number = match.group(1) if match else "unknown_chapter"
        lesson_number = lesson_link.split('/')[-1].replace('.php', '')

        chapter_dir = os.path.join(
            'metanit_lessons_php', f"Розділ {chapter_number}")
        if not os.path.exists(chapter_dir):
            os.makedirs(chapter_dir)

        html_content = content.prettify()
        html_filename = os.path.join(
            chapter_dir, f"{lesson_number}_{sanitized_title}.html")

        with open(html_filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"Lesson {lesson_link} saved as {html_filename}")

print("All lessons downloaded.")
