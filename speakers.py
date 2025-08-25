import argparse
import csv
import json
import requests
import urllib.parse
import urllib.request
from pathlib import Path
from pprint import pprint
from datetime import datetime


DOMAIN = 'https://cfp.pycon.org.il'
SPEAKERS_URL_PATH = '/api/events/{event}/speakers/'
TALKS_URL_PATH = '/api/events/{event}/submissions/'


def save_json(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def get_speaker_answers(speaker):

    QA_MAP = {
        'Company': 'company',
        'Phone number': 'phone_number',
        'Role': 'role',
        'Facebook': 'facebook',
        'Github': 'github',
        'LinkedIn': 'linkedin',
        'Twitter': 'twitter',
        'Do you intend to change the speaker identity?': 'change_identity',
        'Expected experience level of participants': 'experience_level',
        'Target audience': 'target_audience',
        'Other (target audience)': 'target_audience_other',
        'I agree to allow PyCon Israel 2025 to publish my video(s) under Creative Commons Attribution (CC BY) license.': 'agree_to_publish',
        'I am aware of the requirement to participate in dry runs, and will do my best to make myself available': 'dry_run',
    }

    answers = {}
    for a in speaker['answers']:
        try:
            answers[QA_MAP[a['question']['question']['en']]] = a['answer']
        except KeyError:
            answers[QA_MAP[a['question']['question']['he']]] = a['answer']
    return answers


def get_data(endpoint, token, verbose=False):
    url = endpoint + "?" + urllib.parse.urlencode({'limit': 10000, 'questions': 'all'})

    if verbose:
        print(f"Fetching {url}")

    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error fetching data from '{endpoint}' code '{response.status_code}'")
        return {}
    elif verbose:
        print("Success")

    speakers = []
    for speaker in response.json()['results']:
        speaker['answers'] = get_speaker_answers(speaker)
        speakers.append(speaker)

    if verbose:
        print(f"Count: {response.json().get('count', 0)}")
        print(f"Next: {response.json().get('next', 0)}")
        print(f"Previous: {response.json().get('previous', 0)}")

        stats = {}
        for speaker in speakers:
            for a in speaker['answers']:
                stats[a] = stats.get(a, 0) + 1
        pprint(stats)

    return speakers


def fetch_handler(event, item_type, token, verbose=False):

    if item_type == 'speakers':
        url = SPEAKERS_URL_PATH.format(event=event)
    elif item_type == 'talks':
        url = TALKS_URL_PATH.format(event=event)
    else:
        raise ValueError(f"Unknown item type: {item_type}")

    print(f"Fetching data from '{DOMAIN}{url}'...")
    data = get_data(f"{DOMAIN}{url}", token, verbose=verbose)
    return data


def speaker_is_fake(speaker):
    email = speaker['email']
    return email.startswith('cfp+') and email.endswith('@pycon.org.il')


def filter_speakers(speakers, talks, exclude_workshops=False):

    accepted_talks = [t['code'] for t in talks if t['state'] == 'confirmed']
    keynote_talks = [
        t['code'] for t in talks
        if t['state'] == 'confirmed' and 'Keynote' in t['submission_type'].values()
    ]
    workshops = [
        t['code'] for t in talks
        if any('workshop' in ty for ty in t['submission_type'].values())
    ]

    accepted = []
    for speaker in speakers:
        for talk in speaker['submissions']:
            if talk in accepted_talks and not speaker_is_fake(speaker):
                if talk in keynote_talks:
                    speaker['keynote'] = True
                if exclude_workshops and talk in workshops:
                    continue
                accepted.append(speaker)

    print('-----')
    print(f"Accepted talks: {len(accepted_talks)}")
    print(f"Keynote talks: {len(keynote_talks)}")
    print('-----')
    print(f"Speakers: {len(accepted)}")
    # print(f"Accepted speakers: {accepted}")

    return accepted


UPDATE_TIME=datetime.now().astimezone()

SPEAKERS_HEADER_EN = f"""Title: Speakers
Slug: speakers
Template: page
Lang: en
page_number: 17
modified: {UPDATE_TIME}
"""

SPEAKERS_HEADER_HE = f"""Title: דוברות ודוברים
Slug: speakers
Template: page
Lang: he
page_number: 17
modified: {UPDATE_TIME}
"""

SPEAKERS_CONTENT="""
<style>
    body {{
        font-family: Arial, sans-serif;
    }}
    section.site-content > container {{
        max-width: 80%;
    }}
    .speaker-container {{
        # display: flex;
        # flex-wrap: wrap;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, max-content));
        gap: 20px;
        justify-content: center;
        padding: 20px;
    }}
    .speaker-card {{
        width: 300px;
        /*           avatar  bio  info-pad     name           role         social */
        height: calc(300px + 80px + 20px + 1.2em + 20px + 3.2em + 10px + 1.25em + 20px);
        border: 1px solid #ddd;
        border-radius: 10px;
        overflow: hidden;
        position: relative;
        background-color: #fff;
        text-align: center;
        transition: transform 0.3s;
        display: flex;
        flex-direction: column;
    }}
    .speaker-card.keynote {{
        /* background: lightyellow; */
    }}
    .avatar {{
        width: 300px;
        height: 300px;
        object-fit: cover;
    }}
    .info {{
        padding: 10px;
    }}
    .name {{
        font-size: 1.2em;
        margin: 10px 0;
    }}
    .role {{
        color: #666;
        margin: 5px 0;
    }}
    .social-links {{
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 10px 0;
    }}
    .social-links a {{
        text-decoration: none;
        color: #000;
        font-size: 1.25em;
        transition: color 0.3s;
    }}
    .social-links a:hover {{
        color: #007bff; /* Change to your desired hover color */
    }}
    .biography {{
        max-height: 80px;
        overflow: hidden;
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 10px;
        background: rgba(0, 0, 0, 0.8);
        color: #fff;
        transition: max-height 0.3s, opacity 0.3s;
        box-sizing: border-box;
    }}
    .biography:hover {{
        max-height: 200px; /* Adjust based on how much you want to show */
        overflow-y: auto;
    }}
</style>

<div class="speaker-container keynote">{keynotes}</div>
<div class="speaker-container">{speakers}</div>

"""
SPEAKER_CARD = """
    <div class="speaker-card {speaker_class}">
        <img src="{avatar}" class="avatar">
        <div class="info">
            <div class="name">{name}</div>
            <div class="role">{role}</div>
            <div class="social-links">{social_links}</div>
        </div>
        <div class="biography">
            <p>{bio}</p>
        </div>
    </div>
"""


def fix_twitter(url):
    new_url = url.replace('http://', 'https://').lower()
    if 'https' in new_url:
        return new_url
    if new_url:
        return f"https://twitter.com/{new_url}"
    return ''


def fix_github(url):
    new_url = url.replace('http://', 'https://').lower()
    if 'https' in new_url:
        return new_url
    if new_url:
        return f"https://github.com/{new_url}"
    return ''


def fix_linkedin(url):
    new_url = url.replace('http://', 'https://').lower()
    if 'https' in new_url:
        return new_url
    if new_url:
        return f"https://linkedin.com/in/{new_url}"
    return ''

def fix_facebook(url):
    return url


SOCIAL_ICONS = {
    'twitter': ('fab fa-twitter', fix_twitter),
    'github': ('fab fa-github', fix_github),
    'linkedin': ('fab fa-linkedin', fix_linkedin),
    'facebook': ('fab fa-facebook', fix_facebook),
}


def generate_speakers_page(speakers):

    speakers_list = []
    keynotes_list = []
    for speaker in speakers:
        avatar = speaker['avatar'] if speaker['avatar'].strip() else '{static}/images/PyConIL.png'
        role = speaker['answers']['role'] if 'role' in speaker['answers'] else ''
        company = speaker['answers']['company'] if 'company' in speaker['answers'] else ''

        social_links = []
        for social, value in speaker['answers'].items():
            if social in SOCIAL_ICONS:
                stype = SOCIAL_ICONS[social][0]
                url = SOCIAL_ICONS[social][1](value)
                social_links.append(f'<a href="{url}" target="_blank"><i class="{stype}"></i></a>')

        social_links_html = '\n'.join(social_links)
        speaker_class = ""
        the_list = speakers_list
        if speaker.get('keynote'):
            speaker_class = "keynote"
            the_list = keynotes_list
        the_list.append(SPEAKER_CARD.format(
            avatar=avatar,
            name=speaker['name'].title(),
            role=f"{role}<br/>{company}",
            bio=speaker['biography'],
            social_links=social_links_html,
            speaker_class=speaker_class,
        ))

    keynotes_html = '\n'.join(keynotes_list)
    speakers_html = '\n'.join(speakers_list)

    return SPEAKERS_CONTENT.format(
        keynotes=keynotes_html,
        speakers=speakers_html,
    )


def get_args():
    parser = argparse.ArgumentParser(description='Get PyCon speakers as csv')
    parser.add_argument('event', type=str, help="Event name (pretalx slug)")
    parser.add_argument('-t', '--token', required=True, help="API token")
    parser.add_argument('-o', '--output', type=str, help="Output speakers md file")
    parser.add_argument('-f', '--force', action='store_true', help="Force download")
    parser.add_argument('-v', '--verbose', action='store_true')
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    speakers = fetch_handler(args.event, 'speakers', args.token, verbose=args.verbose)
    talks = fetch_handler(args.event, 'talks', args.token, verbose=args.verbose)

    accepted_speakers = filter_speakers(speakers, talks)
    # output = Path('speakers.json')
    # save_json(accepted_speakers, output)

    md_content = generate_speakers_page(accepted_speakers)
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(SPEAKERS_HEADER_EN + md_content)
        p = Path(args.output)
        stem_he = p.stem + "_he"
        with open(p.with_stem(stem_he), 'w', encoding='utf-8') as f:
            f.write(SPEAKERS_HEADER_HE + md_content)
    else:
        print(md_content)

