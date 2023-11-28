import re


def get_tds(html):
    output = []
    for match in re.finditer(r'<td.*td>', html):
        output.append(match.group())
    return output


def strip_style(target_string):
    for match in re.finditer(r'<[^>]*>', target_string):
        target_string = target_string.replace(match.group(), "")
    return target_string


print(strip_style("<td adfapi asdhh al>this</td>"))
