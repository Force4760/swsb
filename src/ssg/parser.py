import markdown
import re
import meta 

def parser(md, file):
    g = meta.get_meta(file)
    md = re.sub("Title\: (.)+", "", md)
    md = re.sub("Authore\: (.)+", "", md)
    md = re.sub("Date\: (.)+", "", md)
    md = re.sub("Overview\: (.)+", "", md)
    md = re.sub("(Img|Image)\: (.)+", "", md)
    return [g,markdown.markdown(md, extensions=['extra', 'admonition', 'codehilite','nl2br','wikilinks', 'fenced_code']).replace("\n", "<br/>")]
