import subprocess

section_2 = {
    'name': 'section_1',
    'username': 'yourimpartususername',
    'password': 'yourimpartuspassword',
    'direction': 'left',
    'course_url': [
        'https://a.impartus.com/ilc/#/course/830902/706',  # ACI
        'https://a.impartus.com/ilc/#/course/830905/706',  # IDS
        'https://a.impartus.com/ilc/#/course/830899/706',  # ISM
        'https://a.impartus.com/ilc/#/course/830895/706'  # ML
    ],
    # if you are on Windows, make sure you escape the paths as done here
    'destination': r'specify\\the\\desired\\path',
    'quality': '720p'
}

# Add details of other sections, if you want to download videos from their sections
section_1 = section_3 = section_4 = {'name': ''}

sections = [section_1, section_2, section_3, section_4]

for section in sections:
    print(f'-----Dowloading lectures for {section["name"]}-----')
    if section.get('course_url'):
        for course in section['course_url']:
            print(f'Dowloading lecture for course -> {course}')
            cmd = f"py -m poetry run python ilc_scrape.py -u {section['username']} -p {section['password']} -d {section['destination']} -a {section['direction']} -c {course} -q {section['quality']}"
            print(subprocess.run(cmd.split()))
