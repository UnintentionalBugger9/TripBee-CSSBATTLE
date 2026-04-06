import re

def process_file(filepath, replacements):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all Unsplash links
    urls = re.findall(r'https://images\.unsplash\.com/photo-[^"\'>\s\)]+', content)
    
    print(f"{filepath} has {len(urls)} urls.")
    
    # For each URL found, replace it with the next one from the replacements list
    num_replacements = min(len(urls), len(replacements))
    for i in range(num_replacements):
        content = content.replace(urls[i], replacements[i], 1)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Replaced {num_replacements} urls in {filepath}.")

# HOME
home_replacements = [
    "home/2.png", "home/3.png", "home/4.png", "home/5.png",
    "home/6.png", "home/7.png", "home/8.png", "home/9.png",
    "home/10.png", "home/11.png", "home/12.png", "home/13.png",
    "home/14.png", "home/19.png", "home/6d721080189c34129e373d8b62696940aa244976.png",
    "home/15.png", "home/16.png", "home/17.png", "home/18.png"
]
process_file('d:/internship/stuff/python/home.html', home_replacements)

# ABOUT US
about_replacements = [
    "about_us/about1.png", "about_us/about2.png", "about_us/about3.png", "about_us/about4.png",
    "about_us/15.png", "about_us/16.png", "about_us/17.png", "about_us/18.png"
]
process_file('d:/internship/stuff/python/aboutUs.html', about_replacements)

# BLOG
blog_replacements = [
    "blog/20.png",
    "blog/1.jpg", "blog/2.jpg", "blog/3.jpg", "blog/4.jpg", "blog/5.jpg", 
    "blog/6.jpg", "blog/7.jpg", "blog/8.jpg", "blog/9.jpg",
    "blog/11.png", "blog/12.png", "blog/13.png", "blog/14.png", "blog/15.png", "blog/17.png"
]
process_file('d:/internship/stuff/python/blog.html', blog_replacements)

print("Done replacing.")
